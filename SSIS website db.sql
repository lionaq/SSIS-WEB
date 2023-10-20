CREATE DATABASE  IF NOT EXISTS `mydb`;
USE `mydb`;


DROP TABLE IF EXISTS `college_table`;
CREATE TABLE `college_table` (
  `college_code` varchar(10) NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`college_code`),
  UNIQUE KEY `collegeCode_UNIQUE` (`college_code`)
);

DROP TABLE IF EXISTS `course_table`;

CREATE TABLE `course_table` (
  `course_code` varchar(10) NOT NULL,
  `course` varchar(80) NOT NULL,
  `college_code` varchar(10) NOT NULL,
  PRIMARY KEY (`course_code`),
  UNIQUE KEY `courseCode_UNIQUE` (`course_code`),
  KEY `fk_idx` (`college_code`),
  CONSTRAINT `fk1` FOREIGN KEY (`college_code`) REFERENCES `college_table` (`college_code`) ON DELETE CASCADE ON UPDATE CASCADE
);


DROP TABLE IF EXISTS `student_table`;
CREATE TABLE `student_table` (
  `student_id` varchar(9) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  `year_level` int NOT NULL,
  `gender` varchar(7) NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `studentID_UNIQUE` (`student_id`),
  KEY `fk_idx` (`course_code`),
  CONSTRAINT `fk` FOREIGN KEY (`course_code`) REFERENCES `course_table` (`course_code`) ON DELETE CASCADE ON UPDATE CASCADE
);