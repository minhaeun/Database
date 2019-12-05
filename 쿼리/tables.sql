create database library default CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
use library;

CREATE TABLE `area` (
  `area_no` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(32) NOT NULL,
  PRIMARY KEY (`area_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `book` (
  `book_unique_no` int(11) NOT NULL AUTO_INCREMENT,
  `book_no` int(11) DEFAULT NULL,
  `condition` varchar(10) NOT NULL,
  PRIMARY KEY (`book_unique_no`),
  FOREIGN KEY (`book_no`) REFERENCES `book_detail` (`book_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `book_detail` (
  `book_no` int(11) NOT NULL AUTO_INCREMENT,
  `area_no` int(11) DEFAULT NULL,
  `title` varchar(50) NOT NULL,
  `publisher` varchar(32) NOT NULL,
  `published_date` datetime DEFAULT NULL,
  `author` varchar(32) NOT NULL,
  PRIMARY KEY (`book_no`),
  FOREIGN KEY (`area_no`) REFERENCES `area` (`area_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rental` (
  `rental_no` int(11) NOT NULL AUTO_INCREMENT,
  `user_no` int(11) DEFAULT NULL,
  `book_unique_no` int(11) DEFAULT NULL,
  `rental_date` datetime DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  `return_date` datetime DEFAULT NULL,
  `note` varchar(50) NOT NULL,
  PRIMARY KEY (`rental_no`),
  FOREIGN KEY (`user_no`) REFERENCES `user` (`user_no`),
  FOREIGN KEY (`book_unique_no`) REFERENCES `book` (`book_unique_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `request` (
  `request_no` int(11) NOT NULL,
  `user_no` int(11) DEFAULT NULL,
  `title` varchar(50) NOT NULL,
  `publisher` varchar(32) NOT NULL,
  `author` varchar(32) NOT NULL,
  `request_date` datetime DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  PRIMARY KEY (`request_no`),
  FOREIGN KEY (`user_no`) REFERENCES `user` (`user_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `reservation` (
  `reservation_no` int(11) NOT NULL AUTO_INCREMENT,
  `user_no` int(11) DEFAULT NULL,
  `book_no` int(11) DEFAULT NULL,
  `reservation_date` datetime DEFAULT NULL,
  `state` varchar(10) NOT NULL,
  PRIMARY KEY (`reservation_no`),
  FOREIGN KEY (`user_no`) REFERENCES `user` (`user_no`),
  FOREIGN KEY (`book_no`) REFERENCES `book_detail` (`book_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
  `user_no` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(32) NOT NULL,
  `user_name` varchar(32) NOT NULL,
  `phonenum` varchar(12) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`user_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;