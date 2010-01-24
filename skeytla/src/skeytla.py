#!/usr/bin/env python
#
# 2010 bthj.is

import tornado.httpserver
import tornado.ioloop
import tornado.database
import tornado.web
import os.path

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="skeytla", help="blog database name")
define("mysql_user", default="skeytla", help="blog database user")
define("mysql_password", default="", help="blog database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/rim", RimHandler)
        ]
        settings = dict(
            title=u"Skeytla",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        
        self.db = tornado.database.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    max_result_rows = 100

class HomeHandler(BaseHandler):
    def get(self):
        self.render("home.html")

class RimHandler(BaseHandler):
    def get(self):
        upphaf = self.get_argument("u", None)
        endir = self.get_argument("e", None)
        if upphaf is None and endir is not None:
            rimord = self.db.query(''.join(["select * from ordmyndir ",
                                   "where ordmynd like %s limit ", 
                                   str(self.max_result_rows)]), ('%%%s' % endir))
        elif upphaf is not None and endir is not None:
            rimord = self.db.query(''.join(["select * from ordmyndir ",
                                   "where ordmynd like %s and ordmynd like %s limit ",
                                   str(self.max_result_rows)]), 
                                   ('%s%%' % upphaf), ('%%%s' % endir))
        elif upphaf is not None and endir is None:
            rimord = self.db.query(''.join(["select * from ordmyndir ",
                                   "where ordmynd like %s limit ",
                                   str(self.max_result_rows)]), ('%s%%' % upphaf))            
        self.render("rim.json", rimord=rimord)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
