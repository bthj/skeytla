-- To create the database:
--   CREATE DATABASE skeytla;
--   GRANT ALL PRIVILEGES ON skeytla.* TO 'skeytla'@'localhost' IDENTIFIED BY 'kveddu';
--
-- To reload the tables:
--   mysql --user=skeytla --password=kveddu --database=skeytla < ordmyndalisti_and_reverse.sql

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
-- ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS ordmyndir_and_reversed;
CREATE TABLE ordmyndir_and_reversed (
  ordmynd varchar(40),
  ordmynd_reversed varchar(40)
);

INSERT INTO ordmyndir_and_reversed VALUES ('a','a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunn','nnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunna','annuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnanna','annannuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnar','rannuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnarinnar','rannirannuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnin','ninnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnina','aninnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunninni','inninnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnir','rinnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnirnar','ranrinnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnum','munnuknie-a');
INSERT INTO ordmyndir_and_reversed VALUES ('a-einkunnunum','mununnuknie-a');
