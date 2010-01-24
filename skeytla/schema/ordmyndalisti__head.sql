-- To create the database:
--   CREATE DATABASE skeytla;
--   GRANT ALL PRIVILEGES ON skeytla.* TO 'skeytla'@'localhost' IDENTIFIED BY 'kveddu';
--
-- To reload the tables:
--   mysql --user=skeytla --password=leyndo --database=skeytla < ordmyndalisti.sql

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
-- ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS ordmyndir;
CREATE TABLE ordmyndir (
  ordmynd varchar(40)
);

INSERT INTO ordmyndir VALUES ('a');
INSERT INTO ordmyndir VALUES ('a-einkunn');
INSERT INTO ordmyndir VALUES ('a-einkunna');
INSERT INTO ordmyndir VALUES ('a-einkunnanna');
