ALTER TABLE `skeytla`.`ordmyndir_and_reversed` 
ADD INDEX `ordmnr_ordm_idx` USING BTREE (`ordmynd` ASC) ;

ALTER TABLE `skeytla`.`ordmyndir_and_reversed` 
ADD INDEX `ordmnr_rev_idx` USING BTREE (`ordmynd_reversed` ASC) ;

ALTER TABLE `skeytla`.`ordmyndir_and_reversed` 
ADD INDEX `ordmnr_ordm_rev_idx` USING BTREE (`ordmynd` ASC, `ordmynd_reversed` ASC) ;
