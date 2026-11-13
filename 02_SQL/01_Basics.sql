SHOW DATABASES; #To check the databases present

USE WORLD;   # to use the data base world
SELECT DATABASE();
SHOW TABLES;   #to see the tables present in the database

SELECT * FROM city; # To display all the data from the table
SELECT ID, Name FROM city WHERE CountryCode='NLD'; 

#--------------------------------------------
# LET'S CREATE A DATABASE AND TABLE INSIDE IT 
#--------------------------------------------
SHOW DATABASES;
CREATE DATABASE college_db;
USE college_db;

#Creating table in college_db

CREATE TABLE students(
       student_id INT PRIMARY KEY,
	   name VARCHAR(50),
       age INT,
       department VARCHAR(50),
       cgpa FLOAT 
);

#Insert values
INSERT INTO students 
VALUES
(1,"Aman",20,"CSE",7.8),
(2,"Aradhya",21,"CSE AIML",7.5),
(3,"Aanya",19,"MECHANICAL",6.0),
(4,"Diya",21,"CSE AIDS",7.0),
(5,"Ankush",22,"CSE",8.8);

SELECT * FROM students; #Display all students
SELECT student_id, name FROM students; # display only name and id

CREATE TABLE student_info(
     stu_id INT PRIMARY KEY,
     first_name VARCHAR(50),
     last_name CHAR(30),
     goal NVARCHAR(255),
     deadline DATETIME
);
SELECT * FROM student_info;
ALTER TABLE student_info ADD department VARCHAR(50);

INSERT INTO student_info (stu_id, first_name, last_name, goal, deadline, department)
VALUES
(1, "Aman", "Rajput", "Software Engineer", "2026-12-31 23:59:59", "CSE"),
(2, "Aradhya", "Sharma", "AI Researcher", "2026-11-30 18:00:00", "CSE AIML"),
(3, "Aanya", "Verma", "Robotics Engineer", "2027-05-15 12:00:00", "MECHANICAL"),
(4, "Diya", "Patel", "Data Scientist", "2026-10-20 09:00:00", "CSE AIDS"),
(5, "Ankush", "Kumar", "Cloud Architect", "2027-01-10 17:30:00", "CSE");

USE college_db;
SELECT * FROM student_info;
SELECT goal, deadline FROM student_info;

DESCRIBE student_info;  # to see the structure of the table

 



