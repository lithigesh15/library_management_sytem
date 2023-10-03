-- MySQL dump 10.13  Distrib 5.5.56, for Win32 (AMD64)
--
-- Host: localhost    Database: lib
-- ------------------------------------------------------
-- Server version	5.5.56

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

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `uname` char(100) DEFAULT NULL,
  `passwd` char(100) DEFAULT NULL,
  `ques` char(100) DEFAULT NULL,
  `ans` char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('LDN','sagar@123','Team code?','tkinter@123'),('lithigesh','12345','DOB','15-11-2005'),('Karthikeyan','2468','DOB','08-02-2006'),('kavin','12345','what is your name','kavin'),('KISHANTH','2005','WHATS YOUR NAME','2006');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `sno` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `name` char(100) DEFAULT NULL,
  `author` char(100) DEFAULT NULL,
  `publisher` char(100) DEFAULT NULL,
  `genre` char(100) DEFAULT NULL,
  `copies` int(11) DEFAULT NULL,
  `avb_copies` int(11) DEFAULT NULL,
  `date_` date DEFAULT NULL,
  `status` char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (0,1000,'0','0','0','0',1,0,'2022-05-21','yes'),(1,1001,'Harry Potter','JK Rowling','ARK','Fantasy',10,9,'2022-05-21','yes'),(2,1011,'JEE Champion','G Thewani','MTG','Educational',5,4,'2022-05-21','yes'),(3,1016,'NEET Champion','S Thewani','MTG','Educational',24,23,'2022-05-21','yes'),(4,1040,'Avengers Assemble','StanLee','Marvel Studios','Comics',160,159,'2022-05-21','yes'),(5,1200,'Man Of Steel','','DC Comics','Comics',10,9,'2022-05-21','yes'),(6,1210,'calculus','G Tewani','Cencage','Educational',2,1,'2022-05-21','yes'),(7,1212,'Organic Chemistry','K S Verma','GRB','Educational',8,7,'2022-05-21','yes'),(8,1220,'The Immortal','Stephen Splender','Manchester Guardian','Action and Adventure',13,1,'2022-08-12','yes'),(9,1233,'Ponniyin Selvan','Kalki','Tamil Novels','Biography',25,1,'2022-08-12','yes'),(10,1258,'The Silent Patient','Alex Michael','New York Times','Crime & Mystery',10,1,'2022-08-12','yes'),(11,1268,'Wrath Of The Storm - 1','John Keats','Scholastic Inc.','Fantasy',1,1,'2022-08-12','yes'),(12,1269,'Wrath Of The Storm -2','John Keats','Scholastic Inc.','Fantasy',1,1,'2022-08-12','yes'),(13,1270,'Wrath Of The Storm -3','John Keats','Scholastic Inc.','Fantasy',1,1,'2022-08-12','yes'),(14,1271,'Wings Of Fire','Abdul Kalam','Sangam Books Ltd.','Autobiography',20,1,'2022-08-12','yes'),(15,1291,'Abraham Lincolin','Lord Chanwood','AB books Ltd.','Autobiography',20,1,'2022-08-12','yes'),(16,1311,'The Road and The Lamp','B Singh','Notion Press','Horror',10,1,'2022-08-12','yes'),(17,1321,'Ghost Of the Silent Hills','Krishan','FP Publications','Horror',10,1,'2022-08-12','yes'),(18,1331,'The Red Badge Of Courage','Crane Stephen','General Press','Fiction',30,1,'2022-08-12','yes'),(19,1361,'Humour at the Workplace','Marco Marwin','Rupa & Co','Humor and Satire',25,1,'2022-08-12','yes'),(20,1386,'Black Humour','NR Veronica','LAP Publishers','Humor and Satire',1,1,'2022-08-12','yes'),(21,1387,'A Web Of Tragedy','Cheryl T','Cheryl T .Long','Tragedy',23,1,'2022-08-12','yes'),(22,1410,'Modern Weapons','Martin J','Chartwell Books','Lifestyle',5,1,'2022-08-12','yes'),(23,1415,'SciFi97','Unknown','American Inst. Of Physics','Sci-Fi',1,1,'2022-08-12','yes'),(24,1416,'Anne Frank','Anne Frank','Words Power','Biography',25,1,'2022-08-12','yes'),(25,1441,'Poli SciFi','Unknown','Taylor & Francis Ltd.','Sci-Fi',1,1,'2022-08-12','yes'),(26,1442,'The Memoirs Of Sherlock Holmes','Arthur Doyle','LDN Books','Memoirs',5,1,'2022-08-12','yes');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_b`
--

DROP TABLE IF EXISTS `issue_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue_b` (
  `s_id` int(11) DEFAULT NULL,
  `b_id` int(11) DEFAULT NULL,
  `issue_d` date DEFAULT NULL,
  `return_d` date DEFAULT NULL,
  `status` char(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_b`
--

LOCK TABLES `issue_b` WRITE;
/*!40000 ALTER TABLE `issue_b` DISABLE KEYS */;
/*!40000 ALTER TABLE `issue_b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `sno` int(11) NOT NULL,
  `s_id` int(11) DEFAULT NULL,
  `name` char(100) DEFAULT NULL,
  `class` char(25) DEFAULT NULL,
  `batch` int(11) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (1,1201,'Brindha','XII-B',2022),(2,1202,'Ponnishree','XII-B',2022),(3,1203,'Athish','XII-B',2022),(4,1204,'Karvanan','XII-B',2022),(5,1205,'Kishanth','XII-B',2022),(6,1206,'Kishore','XII-B',2022),(7,1207,'Niranjan','XII-B',2022),(8,1208,'Sabariram','XII-B',2022),(9,1209,'Thayananth','XII-B',2022),(10,1210,'Thiruvengadam','XII-B',2022),(11,1211,'Preethika','XII-B',2022),(12,1212,'Suvisha','XII-B',2022),(13,1213,'Ashwin','XII-B',2022),(14,1214,'Deep Nandha','XII-B',2022),(15,1215,'Dharshan','XII-B',2022),(16,1216,'Dharun','XII-B',2022),(17,1217,'Kavin','XII-B',2022),(18,1218,'Kaviyarasu','XII-B',2022),(19,1219,'Kishanth','XII-B',2022),(20,1220,'Lithigesh','XII-B',2022),(21,1221,'Narain Karthigeyan','XII-B',2022),(22,1222,'Pranesh Balaji','XII-B',2022),(23,1223,'Sachin','XII-B',2022),(24,1224,'Sanjai Kumar','XII-B',2022),(25,1225,'Sanjay Rithik','XII-B',2022),(26,1226,'Sri Sanjith','XII-B',2022),(27,1227,'Shoban Chiddarth','XII-B',2022),(28,1228,'Sujith','XII-B',2022),(29,1229,'Yashwanth Kumar','XII-B',2022);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-23 14:59:35
