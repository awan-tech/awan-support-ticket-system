DROP DATABASE IF EXISTS awan_ticket_system;

CREATE DATABASE IF NOT EXISTS awan_ticket_system;
USE awan_ticket_system;

CREATE TABLE IF NOT EXISTS `Admins` (
	`admin_id` int NOT NULL AUTO_INCREMENT,
	`admin_name` varchar(255) NOT NULL,
	`admin_role` varchar(255) NOT NULL,
	`admin_account` varchar(255) NOT NULL,
	`admin_password` varchar(255) NOT NULL,
	PRIMARY KEY (`admin_id`)
);

CREATE TABLE IF NOT EXISTS `Tickets` (
	`ticket_id` int NOT NULL AUTO_INCREMENT,
	`admin_id` int NOT NULL,
	`customer_id` int NOT NULL,
	`service_id` int NOT NULL,
	`ticket_title` varchar(255) NOT NULL,
	`urgency` int,
	`created_at` DATETIME NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (`ticket_id`)
);

CREATE TABLE IF NOT EXISTS `Customers` (
	`customer_id` int NOT NULL AUTO_INCREMENT,
	`customer_name` varchar(255) NOT NULL,
	`customer_level` varchar(255) NOT NULL,
	`customer_mail` varchar(255) NOT NULL,
	`customer_company` varchar(255) NOT NULL,
	`customer_account` varchar(255) NOT NULL,
	`customer_password` varchar(255) NOT NULL,
	PRIMARY KEY (`customer_id`)
);

CREATE TABLE IF NOT EXISTS `Services` (
	`service_id` int NOT NULL AUTO_INCREMENT,
	`service_type` varchar(255) NOT NULL,
	`service_name` varchar(255) NOT NULL,
	PRIMARY KEY (`service_id`)
);

CREATE TABLE IF NOT EXISTS `Ticket_Status` (
	`ticket_id` int NOT NULL,
	`ticket_status` varchar(255) NOT NULL,
	PRIMARY KEY (`ticket_id`)
);

CREATE TABLE IF NOT EXISTS `Ticket_Contents` (
	`content_id` int NOT NULL AUTO_INCREMENT,
	`ticket_id` int NOT NULL,
	`ticket_content` varchar(10000) NOT NULL,
	`owner` varchar(255),
	`created_at` DATETIME NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY (`content_id`)
);

CREATE TABLE IF NOT EXISTS `Ticket_Images` (
	`image_id` int NOT NULL AUTO_INCREMENT,
	`content_id` int NOT NULL,
	`image_url` varchar(500),
	PRIMARY KEY (`image_id`)
);

ALTER TABLE `Tickets` ADD CONSTRAINT `Tickets_fk0` FOREIGN KEY (`admin_id`) REFERENCES `Admins`(`admin_id`);

ALTER TABLE `Tickets` ADD CONSTRAINT `Tickets_fk1` FOREIGN KEY (`customer_id`) REFERENCES `Customers`(`customer_id`);

ALTER TABLE `Tickets` ADD CONSTRAINT `Tickets_fk2` FOREIGN KEY (`service_id`) REFERENCES `Services`(`service_id`);

ALTER TABLE `Ticket_Status` ADD CONSTRAINT `Ticket_Status_fk0` FOREIGN KEY (`ticket_id`) REFERENCES `Tickets`(`ticket_id`);

ALTER TABLE `Ticket_Contents` ADD CONSTRAINT `Ticket_Contents_fk0` FOREIGN KEY (`ticket_id`) REFERENCES `Tickets`(`ticket_id`);

ALTER TABLE `Ticket_Images` ADD CONSTRAINT `Ticket_Images_fk0` FOREIGN KEY (`content_id`) REFERENCES `Ticket_Contents`(`content_id`);