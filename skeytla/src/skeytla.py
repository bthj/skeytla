#!/usr/bin/env python
#
# 2010 bthj.is

import tornado.httpserver
import tornado.ioloop
import tornado.database
import tornado.web
import os.path

from tornado.options import define, options
from tornado.database import OperationalError

define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="skeytla database host")
define("mysql_database", default="skeytla", help="skeytla database name")
define("mysql_user", default="skeytla", help="skeytla database user")
define("mysql_password", default="", help="skeytla database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/rim", RimHandler),
            (r"/stem", StemHandler)
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
        limit = self.get_argument("limit", None)
        if limit is None:
            limit = self.max_result_rows
        if upphaf is None and endir is not None:
            rimord = self.query("select * from ordmyndir_and_reversed "
                                   "where ordmynd_reversed like %s "
                                   "order by ordmynd asc limit %s", 
                                   ('%s%%' % endir[::-1]), int(limit))
        elif upphaf is not None and endir is not None:
            rimord = self.query("select * from ordmyndir_and_reversed "
                                   "where ordmynd like %s and ordmynd_reversed like %s "
                                   "order by ordmynd asc limit %s",
                                   ('%s%%' % upphaf), ('%s%%' % endir[::-1]), int(limit))
        elif upphaf is not None and endir is None:
            rimord = self.query("select * from ordmyndir_and_reversed "
                                   "where ordmynd like %s "
                                   "order by ordmynd asc limit %s",
                                    ('%s%%' % upphaf), int(limit))
        self.render("rim.json", rimord=rimord)
        
    def query(self, query, *parameters):
        try:
            return self.db.query(query, *parameters)
        except OperationalError:
            try:
                return self.db.query(query, *parameters)
            except OperationalError:
                raise
            

class StemHandler(BaseHandler):
    def get(self):
        beygingarmynd = self.get_argument("b", None)
        if beygingarmynd is not None:
            ordstofnar = self.db.query("select distinct id, uppflettiord, ordflokkur "
                                       "from bin where beygingarmynd = %s", beygingarmynd)
        self.render("stem.json", stems=ordstofnar)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
