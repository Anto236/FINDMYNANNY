-- MySQL dump 10.13  Distrib 5.7.8-rc, for Linux (x86_64)
--
-- Host: localhost    Database: findmynanny
-- ------------------------------------------------------
-- Server version	5.7.8-rc

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Drop database
DROP DATABASE IF EXISTS findmynanny;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS findmynanny;
CREATE USER IF NOT EXISTS 'fmn_dev'@'localhost' IDENTIFIED BY 'fmn_dev_pwd';
GRANT ALL PRIVILEGES ON `findmynanny`.* TO 'fmn_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'fmn_dev'@'localhost';
FLUSH PRIVILEGES;

USE findmynanny;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` VALUES 
('521a55f4-7d82-47d9-b54c-a76916479501', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'Nakuru'),
('521a55f4-7d82-47d9-b54c-a76916479502', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'Eldoret'),
('521a55f4-7d82-47d9-b54c-a76916479503', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'Kisumu'),
('521a55f4-7d82-47d9-b54c-a76916479504', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'Nyeri'), 
('521a55f4-7d82-47d9-b54c-a76916479505', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'Mombasa');

--
-- Table structure for table `nannies`
--

DROP TABLE IF EXISTS `nannies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `nannies` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `address` varchar(128) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `hourly_rate` varchar(128) NOT NULL,
  `years_of_experience` varchar(128) NOT NULL,
  `city_id` varchar(60) NOT NULL,
  `image` LONGBLOB,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_city_id` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cities`
--


INSERT INTO `nannies` VALUES
('521a55f4-7d82-47d9-b54c-a76916479506', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'email1@gmail.com', 'password1', 'Daisy', 'Auma', 'Address 1', '0700000001', '$10', '5', '521a55f4-7d82-47d9-b54c-a76916479501', LOAD_FILE('/var/lib/mysql-files/nannies/daisy.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479507', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'email2@gmail.com', 'password2', 'Jack', 'Auma', 'Address 2', '0700000002', '$15', '3', '521a55f4-7d82-47d9-b54c-a76916479502', LOAD_FILE('/var/lib/mysql-files/nannies/jack.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479508', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'email3@gmail.com', 'password3', 'Joy', 'Auma', 'Address 3', '0700000003', '$18', '7', '521a55f4-7d82-47d9-b54c-a76916479503', LOAD_FILE('/var/lib/mysql-files/nannies/joy.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479509', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'email4@gmail.com', 'password4', 'Juma', 'Auma', 'Address 4', '0700000004', '$20', '6', '521a55f4-7d82-47d9-b54c-a76916479504', LOAD_FILE('/var/lib/mysql-files/nannies/juma.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479510', '2017-03-25 19:42:40', '2017-03-25 19:42:40', 'email5@gmail.com', 'password5', 'Shiku', 'Auma', 'Address 5', '0700000005', '$5', '8', '521a55f4-7d82-47d9-b54c-a76916479505', LOAD_FILE('/var/lib/mysql-files/nannies/shiku.jpg'));

DROP TABLE IF EXISTS `families`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `families` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128),
  `last_name` varchar(128),
  `address` varchar(128) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `preferred_payment_method` varchar(128) NOT NULL,
  `image` LONGBLOB,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cities`
--


INSERT INTO `families` VALUES

('521a55f4-7d82-47d9-b54c-a76916479511', '2023-06-02 12:00:00', '2023-06-02 12:00:00', 'email6@gmail.com', 'password6', 'Evon', 'Ouma', 'Address 1', '0700000001', 'M-Pesa', LOAD_FILE('/var/lib/mysql-files/families/evon.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479512', '2023-06-02 12:00:00', '2023-06-02 12:00:00', 'email7@gmail.com', 'password7', 'Faith', 'Ouma', 'Address 2', '0700000002', 'PayPal', LOAD_FILE('/var/lib/mysql-files/families/faith.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479513', '2023-06-02 12:00:00', '2023-06-02 12:00:00', 'email8@gmail.com', 'password8', 'Grace', 'Ouma', 'Address 3', '0700000003', 'Cash', LOAD_FILE('/var/lib/mysql-files/families/grace.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479514', '2023-06-02 12:00:00', '2023-06-02 12:00:00', 'email9@gmail.com', 'password9', 'Mercy', 'Ouma', 'Address 4', '0700000004', 'Credit Card', LOAD_FILE('/var/lib/mysql-files/families/mercy.jpg')),
('521a55f4-7d82-47d9-b54c-a76916479515', '2023-06-02 12:00:00', '2023-06-02 12:00:00', 'email10@gmail.com', 'password10', 'Stacey', 'Ouma', 'Address 5', '0700000005', 'M-Pesa', LOAD_FILE('/var/lib/mysql-files/families/stacey.jpg'));


DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `reviews` (
  `review_id` varchar(60) NOT NULL,
  `family_id` varchar(60) NOT NULL,
  `nanny_id` varchar(60) NOT NULL,
  `rating` varchar(10) NOT NULL,
  `comments` varchar(1024) NOT NULL,
  PRIMARY KEY (`review_id`),
  CONSTRAINT `fk_family_id` FOREIGN KEY (`family_id`) REFERENCES `families` (`id`),
  CONSTRAINT `fk_nanny_id` FOREIGN KEY (`nanny_id`) REFERENCES `nannies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cities`
--

INSERT INTO `reviews` VALUES
('521a55f4-7d82-47d9-b54c-a76916479516', '521a55f4-7d82-47d9-b54c-a76916479511', '521a55f4-7d82-47d9-b54c-a76916479506', '5', 'Great nanny, highly recommended.'),
('521a55f4-7d82-47d9-b54c-a76916479517', '521a55f4-7d82-47d9-b54c-a76916479512', '521a55f4-7d82-47d9-b54c-a76916479507', '4', 'Good experience, punctual and friendly.'),
('521a55f4-7d82-47d9-b54c-a76916479518', '521a55f4-7d82-47d9-b54c-a76916479513', '521a55f4-7d82-47d9-b54c-a76916479508', '3', 'Average service, could have been better.'),
('521a55f4-7d82-47d9-b54c-a76916479519', '521a55f4-7d82-47d9-b54c-a76916479514', '521a55f4-7d82-47d9-b54c-a76916479509', '5', 'Exceptional nanny, very skilled and caring.'),
('521a55f4-7d82-47d9-b54c-a76916479520', '521a55f4-7d82-47d9-b54c-a76916479515', '521a55f4-7d82-47d9-b54c-a76916479510', '2', 'Disappointed with the service, not recommended.');

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `bookings` (
  `id` VARCHAR(60) NOT NULL,
  `family_id` VARCHAR(60) NOT NULL,
  `nanny_id` VARCHAR(60) NOT NULL,
  `start_date` DATETIME NOT NULL,
  `end_date` DATETIME NOT NULL,
  `job_description` VARCHAR(1024) NOT NULL,
  `status` VARCHAR(60) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`id`),
  FOREIGN KEY (`family_id`) REFERENCES `families`(`id`),
  FOREIGN KEY (`nanny_id`) REFERENCES `nannies`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cities`
--


INSERT INTO `bookings` VALUES
('521a55f4-7d82-47d9-b54c-a76916479521', '521a55f4-7d82-47d9-b54c-a76916479512', '521a55f4-7d82-47d9-b54c-a76916479507', '2023-06-03 09:00:00', '2023-06-03 18:00:00', 'House cleaning for a day', 'accepted'),
('521a55f4-7d82-47d9-b54c-a76916479522', '521a55f4-7d82-47d9-b54c-a76916479513', '521a55f4-7d82-47d9-b54c-a76916479508', '2023-06-04 15:00:00', '2023-06-04 20:00:00', 'Dog walking for a few hours', 'rejected'),
('521a55f4-7d82-47d9-b54c-a76916479523', '521a55f4-7d82-47d9-b54c-a76916479514', '521a55f4-7d82-47d9-b54c-a76916479509', '2023-06-05 10:00:00', '2023-06-05 16:00:00', 'Babysitting for a few hours', 'pending'),
('521a55f4-7d82-47d9-b54c-a76916479524', '521a55f4-7d82-47d9-b54c-a76916479515', '521a55f4-7d82-47d9-b54c-a76916479510', '2023-06-06 08:00:00', '2023-06-08 12:00:00', 'Full-time nanny service for 3 days', 'accepted'),
('521a55f4-7d82-47d9-b54c-a76916479525', '521a55f4-7d82-47d9-b54c-a76916479511', '521a55f4-7d82-47d9-b54c-a76916479507', '2023-06-07 14:00:00', '2023-06-07 17:00:00', 'Babysitting for a few hours', 'pending');
