-- Table to store settings - Needs additional columns for avg, smooth and range info (should this be a seperate table linked by ID?
CREATE TABLE `cccp` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `siteID` INTEGER UNSIGNED NOT NULL,
  `ownerID` INTEGER UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` DATETIME  NOT NULL DEFAULT '0000-00-00 00:00:00'
  `isPublic` TINYINT(1)  NOT NULL,
  `path` TEXT  NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `cccp_siteID` FOREIGN KEY `cccp_siteID` (`siteID`)
    REFERENCES `sites` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cccp_ownerID` FOREIGN KEY `cccp_ownerID` (`ownerID`)
    REFERENCES `users` (`ID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Query to fetch list info
SELECT u.username as owner, c.name as name, c.ID as ID, c.ownerID as ownerID, c.time as time FROM cccp c, users u WHERE c.ownerID=u.ID AND c.siteID=:siteID;

-- Dummy setting for testing load
INSERT INTO cccp (`siteID`,`ownerID`,`name`,`isPublic`,`path`) VALUES (1,1,'Demo',1,'/home/jmr/Documents/TempFiles/CCCP/cccpCompress.gz');
