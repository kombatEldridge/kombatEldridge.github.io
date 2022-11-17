CREATE DATABASE IF NOT EXISTS 'multilayer';
USE 'multilayer';

--
-- Table structure for table 'conditions'
--

DROP TABLE IF EXISTS 'conditions';
CREATE TABLE 'conditions' (
  'expID' int NOT NULL,
  'coreSize' double DEFAULT NULL,
  'sio2Size' double DEFAULT NULL,
  'shellSize' double DEFAULT NULL,
  'outerBoolean' text,
  PRIMARY KEY ('expID')
);

--
-- Dumping data for table 'conditions'
--

INSERT INTO 'conditions' VALUES {...};

--
-- Table structure for table 'results'
--

DROP TABLE IF EXISTS 'results';
CREATE TABLE 'results' (
  'expID' int DEFAULT NULL,
  'lambda' double DEFAULT NULL,
  'qEXT' double DEFAULT NULL,
  'qSCA' double DEFAULT NULL,
  'qABS' double DEFAULT NULL,
  'eSQU' double DEFAULT NULL,
  KEY 'expID' ('expID'),
  CONSTRAINT 'results_ibfk_1' FOREIGN KEY ('expID') REFERENCES 'conditions' ('expID')
);

--
-- Dumping data for table 'results'
--

INSERT INTO 'results' VALUES {...};