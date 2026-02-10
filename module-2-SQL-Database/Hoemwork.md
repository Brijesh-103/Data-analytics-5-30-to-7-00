# Student Database

## Question 1: create a database named "school".

```sql
CREATE DATABASE school;
```
## Question 2: create a table named "students" with the following columns: id (primary key), name, age, grade, and country_id (foreign key referencing the country table).

```sql
CREATE TABLE students (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      age INT,
      grade VARCHAR(10),
      country_id INT,
      FOREIGN KEY (country_id) REFERENCES country(id)
);
```

## Question 3: insert at least 5 records into the students table.

```sql
INSERT INTO students (name, age, grade, country_id) VALUES
('Brijesh', 20, 'A', 1),
('Raj', 22, 'B', 2),
('Divyang', 19, 'A', 3),
('Krish', 21, 'C', 1),
('Het', 23, 'B', 2);
```

## Question 4:  create a table named "country" with the following columns: country_id (primary key) and country_name.

```sql
CREATE TABLE country (
      id INT AUTO_INCREMENT PRIMARY KEY,
      country_name VARCHAR(100)
);
```

## Question 5: insert at least 5 records into the country table.

```sql
INSERT INTO country (country_name) VALUES
('India'),
('USA'),
('UK'),
('Australia'),
('Canada');
```

## Question 6: write a query to select all students along with their country names.

```sql
SELECT s.name, s.age, s.grade, c.country_name
FROM students s
JOIN country c ON s.country_id = c.id;
```

## Question 7: write a query to find the average age of students in each grade.

```sql
SELECT grade, AVG(age) AS average_age
FROM students
GROUP BY grade;
```

## Question 8: write a query to find the total number of students in each country.

```sql
SELECT c.country_name, COUNT(s.id) AS total_students
FROM country c
LEFT JOIN students s ON c.id = s.country_id
GROUP BY c.country_name;
```

## Question 9: write a query to find the student with the highest grade.

```sql
SELECT name, grade FROM students
WHERE grade = (SELECT MAX(grade) FROM students);
```

## Question 10: write a query to update the grade of a student with a specific id.

```sql
UPDATE students
SET grade = 'A+'
WHERE id = 3;
```

## Question 11: write a query to delete a student with a specific id.

```sql
DELETE FROM students
WHERE id = 5;
```
&nbsp;
---

---
&nbsp;
# Add to cart database

## Question 1: create a database named "ecommerce"
```sql
CREATE DATABASE ecommerce;
```

## Question 2: create a table named "products" with the following columns: product_id (primary key), product_name, price, and stock.

```sql
CREATE TABLE products (
      product_id INT AUTO_INCREMENT PRIMARY KEY,
      product_name VARCHAR(100),
      price DECIMAL(10, 2),
      stock INT
);
```


## Question 3: insert at least 5 records into the products table.
```sql
INSERT INTO products (product_name, price, stock) VALUES
('Laptop', 999.99, 10),
('Smartphone', 499.99, 20),
('Headphones', 199.99, 15),
('Smartwatch', 299.99, 5),
('Tablet', 399.99, 8);
```

## Question 4: create a table named "customers" with the following columns: customer_id (primary key), customer_name, email, and country_id (foreign key referencing the country table).
```sql
CREATE TABLE customers (
      customer_id INT AUTO_INCREMENT PRIMARY KEY,
      customer_name VARCHAR(100),
      email VARCHAR(255),
      country_id INT,
      FOREIGN KEY (country_id) REFERENCES country(id)
);
```

## Question 5: insert at least 3 records into the customers table.
```sql
INSERT INTO customers (customer_name, email, country_id) VALUES
('Alice', 'alice@example.com', 1),
('Bob', 'bob@example.com', 2),
('Charlie', 'charlie@example.com', 3);
```

## Question 6: create a table named "orders" with the following columns: order_id (primary key), customer_id (foreign key referencing the customers table), product_id (foreign key referencing the products table), quantity, and order_date.
```sql
CREATE TABLE orders (
      order_id INT AUTO_INCREMENT PRIMARY KEY,
      customer_id INT,
      product_id INT,
      quantity INT,
      order_date DATETIME,
      FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
      FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## Question 7: insert at least 5 records into the orders table.
```sql
INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, '2024-01-01 10:00:00'),
(2, 2, 2, '2024-01-02 11:00:00'),
(3, 3, 1, '2024-01-03 12:00:00'),
(1, 4, 1, '2024-01-04 13:00:00'),
(2, 5, 1, '2024-01-05 14:00:00');
```

## Question 8: write a query to select all orders along with customer names and product names.
```sql
SELECT o.order_id, c.customer_name, p.product_name, o.quantity, o.order_date
FROM orders o JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
```

## Question 9: write a query to find the total revenue generated from all orders.
```sql
SELECT SUM(p.price * o.quantity) AS total_revenue
FROM orders o JOIN products p ON o.product_id = p.product_id;
```

## Question 10: write a query to find the most popular product based on the quantity ordered.
```sql
SELECT p.product_name, SUM(o.quantity) AS total_quantity
FROM orders o JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 1;
```

## Question 11: write a query to update the stock of a product after an order is placed.
```sql
UPDATE products p JOIN orders o ON p.product_id = o.product_id
SET p.stock = p.stock - o.quantity
WHERE o.order_id = 1;
```

## Question 12: write a query to delete an order with a specific order_id.
```sql
DELETE FROM orders
WHERE order_id = 5;
```

