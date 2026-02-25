# Assignment 

## Question 1: Statement to create the Contact table
```sql
CREATE TABLE Contact (
    ContactID INT PRIMARY KEY auto_increment,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    IsMain BOOLEAN,
    Email VARCHAR(45),
    Phone VARCHAR(12),
    CompanyID INT REFERENCES Company(CompanyID),
);
```

## Question 2: Statement to create the Employee table
```sql
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY auto_increment,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Salary DECIMAL(10, 2),
    HireDate DATE,
    JobTitle VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
);
```

## Question 3:  Statement to create the ContactEmployee table
```sql
CREATE TABLE ContactEmployee (
    ContactEmployeeID INT PRIMARY KEY auto_increment,
    ContactID INT REFERENCES Contact(ContactID),
    EmployeeID INT REFERENCES Employee(EmployeeID),
    ContactDate DATE,
    Description VARCHAR(100)
);
```
---
---
```sql
CREATE TABLE Company (
    CompanyID INT PRIMARY KEY auto_increment,
    CompanyName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    Phone VARCHAR(12)
);
```


---