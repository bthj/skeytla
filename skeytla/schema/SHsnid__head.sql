-- To create the database:
--   CREATE DATABASE skeytla;
--   GRANT ALL PRIVILEGES ON skeytla.* TO 'skeytla'@'localhost' IDENTIFIED BY 'kveddu';
--
-- To reload the tables:
--   mysql --user=skeytla --password=leyndo --database=skeytla < SHsnid.sql

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";

DROP TABLE IF EXISTS bin;
CREATE TABLE bin (
  uppflettiord varchar(40),
  id int,
  ordflokkur varchar(60),
  hluti varchar(5),
  beygingarmynd varchar(40),
  greiningarstrengur varchar(40)
);

INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunn','NFET');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnin','NFETgr');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunn','ÞFET');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnina','ÞFETgr');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunn','ÞGFET');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunninni','ÞGFETgr');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnar','EFET');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnarinnar','EFETgr');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnir','NFFT');
INSERT INTO bin VALUES ('a-einkunn',332505,'kvk','alm','a-einkunnirnar','NFFTgr');
