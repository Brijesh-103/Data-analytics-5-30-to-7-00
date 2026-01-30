# What is SQL?
SQL stands for Structured Query Language. It is used to communicate with a database. 

## What is a Database?
A database is a structured collection of data that is stored and accessed electronically. It allows users to store, retrieve, and manage data efficiently.


**List of some Database provider  names:**
1. MySQL
2. PostgreSQL
3. SQLite
4. Microsoft SQL Server
5. Oracle Database
6. MongoDB
7. MariaDB
8. IBM Db2
9. Amazon Aurora
10. Google Cloud Spanner



## What is a Table?
A table is a collection of related data held in a structured format within a database. It consists of rows and columns.

**Users Table:**
| id | name    | email        | password | age | salary |
|----|---------|--------------|----------|-----|--------|
| 1  | Brijesh | brijesh@gmail.com | 20023  | 23  | 23000  |


## What are Columns and Rows in Tables?

**Columns:** 
Columns are the vertical entities in a table that contain all information associated with a specific field.

**Users Table Columns:**

| id | name    | email        | password | age | salary |
|----|---------|--------------|----------|-----|--------|



**Rows:**
Rows are the horizontal entities in a table that contain data for a specific record.

**Users Table:**
| id | name     | email              | password | age | salary |
|----|----------|--------------------|----------|-----|--------|
| 1  | Brijesh  | brijesh@gmail.com  | 20023    | 23  | 23000  |
| 2  | Aman     | aman@gmail.com     | a123456  | 28  | 55000  |
| 3  | Priya    | priya@gmail.com    | p123456  | 31  | 72000  |
| 4  | Rohit    | rohit@gmail.com    | r123456  | 26  | 48000  |
| 5  | Neha     | neha@gmail.com     | n123456  | 29  | 61000  |
| 6  | Sumit    | sumit@gmail.com    | s123456  | 35  | 88000  |
| 7  | Kavita   | kavita@gmail.com   | k123456  | 32  | 75000  |
| 8  | Arjun    | arjun@gmail.com    | ar123456 | 27  | 52000  |
| 9  | Pooja    | pooja@gmail.com    | po123456 | 30  | 68000  |
| 10 | Rahul    | rahul@gmail.com    | ra123456 | 36  | 92000  |

## Types of Commands in SQL
There are five types of SQL commands:
1. DDL (Data Definition Language)
2. DML (Data Manipulation Language)
3. DCL (Data Control Language)
4. TCL (Transaction Control Language)
5. DQL (Data Query Language)

### 1. DDL
DDL stands for Data Definition Language. It is used to define and manage database structures such as databases, tables, indexes, and constraints.


**Commands or Queries in DDL:**
- CREATE
- ALTER
- DROP
- TRUNCATE
- RENAME


### How to Create a Database

**Syntax:**
```sql
CREATE DATABASE database_name;
```

**Examples:**
```sql
CREATE DATABASE  Student_DB;

```

### How to Create a Table

**Chart of Table Creation:**
| Column Name | Data Type    | Size | Description                        |
|-------------|--------------|------|------------------------------------|
| id          | INT          |      | Integer type, used for IDs |
| name        | VARCHAR      | 100  | Variable character string for names |
| email       | VARCHAR      | 255  | Variable character string for email addresses |
| password    | VARCHAR      | 255  | Variable character string for passwords |
| age         | INT          |      | Integer type for age values |
| salary      | DECIMAL      | 10,2 | Decimal type for precise salary amounts |
| department  | VARCHAR      | 100  | Variable character string for department |
| country     | VARCHAR      | 100  | Variable character string for country |
| created_at  | DATETIME     |      | Date and time of record creation |
| is_active   | BOOLEAN      |      | Boolean type for active status |
| phone       | BIGINT       |      | Large integer for phone numbers |
| address     | TEXT         |      | Text type for longer address strings |


**Syntax of Create Table:**
```sql
CREATE TABLE table_name (
    column_name datatype(size) AUTO_INCREMENT PRIMARY KEY,
    ...
    column_name datatype(size)
);
```

**Examples:**
```sql
CREATE TABLE Student_DB (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      email VARCHAR(255),
      password VARCHAR(255),
      age INT,
      salary DECIMAL(10,2),
      department VARCHAR(100),
      country VARCHAR(100),
      created_at DATETIME,
      is_active BOOLEAN,
      phone BIGINT,
      address TEXT
);
```

## ALTER

ALTER is used to add, modify, update, or delete columns.

### Add New Column
```sql
ALTER TABLE Student_DB ADD state VARCHAR(255);
```

### Add New Column After Particular Column
```sql
ALTER TABLE Student_DB ADD photo BLOB AFTER age;
```

### Update Any Column Name
```sql
ALTER TABLE Student_DB CHANGE photo upload_image BLOB;
```

### Delete Any Column Name
```sql
ALTER TABLE Student_DB DROP age;
```

## CHANGE

Change the column name using ALTER.
```sql
ALTER TABLE Student_DB CHANGE photo upload_image BLOB;
```

## ADD

Add a new column name using ALTER.
```sql
ALTER TABLE Student_DB ADD state VARCHAR(255);
```

## DROP

DROP is used to delete database and table structures.

### How to Delete Database
```sql
DROP DATABASE Student_DB;
```
**After DROP, we can never rollback any data.**

### How to Delete Table
```sql
DROP TABLE Student_DB;
```
**After DROP, we can never rollback any data in the table.**

## TRUNCATE

TRUNCATE is used to empty or remove all data at once.
```sql
TRUNCATE TABLE Student_DB;
```
**After TRUNCATE, we can never rollback data.**

# RENAME

RENAME changes the table name.

```sql
RENAME TABLE Student_DB TO flip_Student_DB;
```