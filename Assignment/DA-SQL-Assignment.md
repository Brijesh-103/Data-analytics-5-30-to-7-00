# SQL Assignment

## For this assignment, you will finish building the contact management database for MarketCo

### Question 1) Statement to create the Contact table
```sql
CREATE TABLE Contact (
    ContactID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyID INT NOT NULL,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    IsMain BOOLEAN,
    Email VARCHAR(45),
    Phone VARCHAR(12),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);
```

Output:

| ContactID | CompanyID | FirstName | LastName | Street | City | State | Zip | IsMain | Email | Phone |
|-----------|-----------|-----------|----------|--------|------|-------|-----|--------|--------|-------|


### Question 2) Statement to create the Employee table
```sql
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyID INT NOT NULL,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    Email VARCHAR(45),
    Phone VARCHAR(12),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);
```
Output:
| EmployeeID | CompanyID | FirstName | LastName | Street | City | State | Zip | Email | Phone |
|------------|-----------|-----------|----------|--------|------|-------|-----|--------|-------|


### Question Statement to create the ContactEmployee table
HINT: Use DATE as the datatype for ContactDate. It allows you to store the
date in this format: YYYY-MM-DD (i.e., ‘2014-03-12’ for March 12, 2014).

```sql
CREATE TABLE ContactEmployee (
    ContactID INT NOT NULL,
    EmployeeID INT NOT NULL,
    ContactDate DATE,
    PRIMARY KEY (ContactID, EmployeeID),
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
```
Output:
| ContactID | EmployeeID | ContactDate |
|-----------|------------|-------------|

### Question 4) In the Employee table, the statement that changes Lesley Bland’s phone number to 215-555-8800

```sql
UPDATE Employee
SET Phone = '215-555-8800'
WHERE FirstName = 'Lesley' AND LastName = 'Bland';
```
Output:
| EmployeeID | CompanyID | FirstName | LastName | Street | City | State | Zip | Email | Phone |
|------------|-----------|-----------|----------|--------|------|-------|-----|--------|-------|
