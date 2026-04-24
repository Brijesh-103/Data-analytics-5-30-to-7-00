# SQL Assignment

## Question 8) What is the significance of “%” and “_” operators in the LIKE statement?
The "%" and "_" operators are used in the LIKE statement in SQL to perform pattern matching in string comparisons.
- The "%" operator is a wildcard that matches zero or more characters. For example, if you want to find all records where a column starts with "A", 
you can use the query: `SELECT * FROM table_name WHERE column_name LIKE 'A%';`. This will return all records where the column value starts with "A" followed by any number of characters.
- The "_" operator is a wildcard that matches exactly one character. For example, if you want to find all records where a column has "A" as the second character, 
you can use the query: `SELECT * FROM table_name WHERE column_name LIKE '_A%';`. This will return all records where the second character is "A" and there can be any number of characters before and after it.




9) Explain normalization in the context of databases.
10) What does a join in MySQL mean?
11) 19.What do you understand about DDL, DCL, and DML in MySQL?
12) What is the role of the MySQL JOIN clause in a query, and what are some
common types of joins?
