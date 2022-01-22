-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ssisdb
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `colleges`
--

DROP TABLE IF EXISTS `colleges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colleges` (
  `collegeCode` varchar(100) NOT NULL,
  `collegeName` varchar(100) NOT NULL,
  PRIMARY KEY (`collegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colleges`
--

LOCK TABLES `colleges` WRITE;
/*!40000 ALTER TABLE `colleges` DISABLE KEYS */;
INSERT INTO `colleges` VALUES ('CASS','COLLEGE OF ARTS AND SOCIAL SCIENCES'),('CBAA','COLLEGE OF BUSINESS ADMINISTRATION & ACCOUNTANCY'),('CCS','COLLEGE OF COMPUTER STUDIES'),('COET','COLLEGE OF ENGINEERING AND TECHNOLOG'),('CON','COLLEGE OF NURSING'),('CSM','COLLEGE OF SCIENCE AND MATHEMATICS');
/*!40000 ALTER TABLE `colleges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `courseCode` varchar(100) NOT NULL,
  `courseName` varchar(100) NOT NULL,
  `courseCollege` varchar(100) NOT NULL,
  PRIMARY KEY (`courseCode`),
  KEY `courseCollege` (`courseCollege`),
  KEY `courseName` (`courseName`) /*!80000 INVISIBLE */,
  CONSTRAINT `course_lbfk_1` FOREIGN KEY (`courseCollege`) REFERENCES `colleges` (`collegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('BSCS','BACHELOR OF SCIENCE IN COMPUTER SCIENCE','CCS'),('BSE','BACHELOR OF SCIENCE MAJOR IN ENTREPRENEURSHIP','CBAA'),('BSIT','BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY','CCS'),('BSM','BACHELOR OF SCIENCE IN MATHEMATICS','CSM'),('BSME','BACHELOR OF SCIENCE IN METALLURGICAL ENGINEERING','COET'),('BSP','BACHELOR OF SCIENCE IN PSYCHOLOGY','CASS');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `stud_id` varchar(100) NOT NULL,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `yearLevel` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `image` varchar(500) NOT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('2022-0001','Jannessa','Gucor','BSCS','2','Female','https://res.cloudinary.com/jannessag/image/upload/v1642547136/2022-0001.jpg'),('2022-0002','Houtarou','Oreki','BSCS','1','Male','https://res.cloudinary.com/jannessag/image/upload/v1642547604/2021-0002.jpg'),('2022-0003','Yumeko','Jabami','BSCS','1','Female','https://res.cloudinary.com/jannessag/image/upload/v1642548607/2022-0003.jpg'),('2022-0004','Mai','Sakurajima','BSE','4','Female','https://res.cloudinary.com/jannessag/image/upload/v1642765792/2022-0004.jpg'),('2022-0005','ADWDA','SDAWDAWD','BSP','1','Male','https://res.cloudinary.com/jannessag/image/upload/v1642820587/2022-0005.jpg');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-22 12:18:34
