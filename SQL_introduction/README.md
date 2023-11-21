# SQL - Introduction

### SQL SELECT Statement

The 'SELECT' statement is used to select data from a database.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name;
"""
Here, column1, column2, ... are the field names of the table you want to select data from.
The table_name represents the name of the table you want to select data from.

* EXAMPLE:
"""
SELECT CustomerName,City FROM Customers;
"""

* If you want to return all columns, without specifying every column name, you can use the SELECT * syntax.
"""
SELECT * FROM Customers;
"""

### SQL SELECT DISTINCT Statement

The 'SELECT DISTINCT' statement is used to return only distinct (different) values.

* SYNTAX:
"""
SELECT DISTINCT column1, column2, ...
FROM table_name;
"""

* EXAMPLE:
"""
SELECT DISTINCT Country FROM Customers;
"""

### SQL WHERE Clause

The 'WHERE' clause is used to filter records.
It is used to extract only those records that fulfill a specified condition.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name
WHERE condition;
"""

* EXAMPLE:
"""
SELECT * FROM Customers
WHERE Country='Mexico';
"""

Text Fields vs. Numeric Fields
SQL requires single quotes around text values (most database systems will also allow double quotes).
However, numeric fields should not be enclosed in quotes.

* EXAMPLE:
"""
SELECT * FROM Customers
WHERE CustomerID=1;
"""

* The following operators can be used in the WHERE clause.
 =		Equal	
 >		Greater than	
 <		Less than	
 >=		Greater than or equal	
 <=		Less than or equal	
 <>		Not equal. Note: In some versions of SQL this operator may be written as !=	
 BETWEEN	Between a certain range	
 LIKE		Search for a pattern	
 IN		To specify multiple possible values for a column

### SQL ORDER BY Keyword

The 'ORDER BY' keyword is used to sort the result-set in ascending or descending order.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
"""

* EXAMPLE:
"""
SELECT * FROM Products
ORDER BY Price
"""

* DESC
The 'ORDER BY' keyword sorts the records in ascending order by default. To sort the records in descending order, use the 'DESC' keyword.
"""
SELECT * FROM Products
ORDER BY Price DESC;
"""

* Order Alphabetically
For string values the 'ORDER BY' keyword will order alphabetically.
"""
SELECT * FROM Products
ORDER BY ProductName;
"""

* Alphabetically DESC
To sort the table reverse alphabetically, use the 'DESC' keyword:
"""
SELECT * FROM Products
ORDER BY ProductName DESC;
"""

* ORDER BY Several Columns
The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and the "CustomerName" column. This means that it orders by Country, but if some rows have the same Country, it orders them by CustomerName.
"""
SELECT * FROM Customers
ORDER BY Country, CustomerName;
"""

* Using Both ASC and DESC
The following SQL statement selects all customers from the "Customers" table, sorted ascending by the "Country" and descending by the "CustomerName" column:
"""
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
"""

### SQL AND Operator

The 'WHERE' clause can contain one or many 'AND' operators.
The 'AND' operator is used to filter records based on more than one condition, like if you want to return all customers from Spain that starts with the letter 'G'.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
"""

* Example
Select all customers from Spain that starts with the letter 'G':
"""
SELECT * FROM Customers
WHERE Country='Spain' AND CustomerName LIKE 'G%';
"""

* AND vs OR
The 'AND' operator displays a record if all the conditions are TRUE.
The 'OR' operator displays a record if any of the conditions are TRUE.

* All Conditions Must Be True
The following SQL statement selects all fields from Customers where Country is "Germany" AND City is "Berlin" AND PostalCode is higher than 12000:
"""
SELECT * FROM Customers
WHERE Country='Germany'
and City='Berlin'
and PostalCode > 12000;
"""

* Combining AND and OR
You can combine the 'AND' and 'OR' operators.
The following SQL statement selects all customers from Spain that starts with a "G" or an "R".
Make sure you use parenthesis to get the correct result.
"""
SELECT * FROM Customers
WHERE Country='Spain' AND(CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');
"""

Without parenthesis, the select statement will return all customers from Spain that starts with a "G", plus all customers that starts with an "R", regardless of the country value:
"""
SELECT * FROM Customers
WHERE Country = 'Spain' AND CustomerName LIKE 'G%' OR CustomerName LIKE 'R%';
"""

### SQL OR Operator

The 'WHERE' clause can contain one or more 'OR' operators.
The 'OR' operator is used to filter records based on more than one condition, like if you want to return all customers from Germany but also those from Spain.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
"""

* Example
Select all customers from Germany or Spain:
"""
SELECT * FROM Customers
WHERE Country='Germany' OR Country='Spain';
"""

* The examples are are also similar like the " SQL AND Operator ".

### SQL NOT Operator

The 'NOT' operator is used in combination with other operators to give the opposite result, also called the negative result.

* SYNTAX:
"""
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
"""

* Example
Select only the customers that are NOT from Spain:
"""
SELECT * FROM Customers
WHERE NOT Country='Spain';
"""
In the example above, the 'NOT' operator is used in combination with the = operator, but it can be used in combination with other comparison and/or logical operators.

* NOT LIKE
Example
Select customers that does not start with the letter 'A':
"""
SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'A%';
"""

* NOT BETWEEN
Example
Select customers with a customerID not between 10 and 60:
"""
SELECT * FROM Customers
WHERE CustomerID NOT BETWEEN 10 AND 60;
"""

* NOT IN
Example
Select customers that are not from Paris or London:
"""
SELECT * FROM Customers
WHERE City NOT IN('Paris', 'London');
"""

* NOT Greater Than
Example
Select customers with a CustomerId not greater than 50:
"""
SELECT * FROM Customers
WHERE NOT CustomerID > 50;
"""

* NOT Less Than
Example
Select customers with a CustomerID not less than 50:
"""
SELECT * FROM Customers
WHERE NOT CustomerID < 50;
"""

### SQL INSERT INTO Statement

The 'INSERT INTO' statement is used to insert new records in a table.

* INSERT INTO Syntax
It is possible to write the INSERT INTO statement in two ways:
1. Specify both the column names and the values to be inserted:
"""
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
"""
2. If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the INSERT INTO syntax would be as follows:
"""
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
"""

* INSERT INTO Example
The following SQL statement inserts a new record in the "Customers" table:
"""
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
"""

* Insert Data Only in Specified Columns
It is also possible to only insert data in specific columns.
The following SQL statement will insert a new record, but only insert data in the "CustomerName", "City", and "Country" columns (CustomerID will be updated automatically):
"""
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
"""

* Insert Multiple Rows
It is also possible to insert multiple rows in one statement.
To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:
"""
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
"""
Make sure you separate each set of values with a comma ,.

### SQL NULL Values

* What is a NULL Value?
A field with a NULL value is a field with no value.
If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.
Note: A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!

* How to Test for NULL Values?
It is not possible to test for NULL values with comparison operators, such as =, <, or <>.
We will have to use the IS NULL and IS NOT NULL operators instead.

1. IS NULL Syntax
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

2. IS NOT NULL Syntax
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

* The IS NULL Operator
The IS NULL operator is used to test for empty values (NULL values).
The following SQL lists all customers with a NULL value in the "Address" field:
"""
SELECT CustomerName, ContactName, Address
FROM Customers WHERE Address IS NULL;
"""

* The IS NOT NULL Operator
The IS NOT NULL operator is used to test for non-empty values (NOT NULL values).
The following SQL lists all customers with a value in the "Address" field:
"""
SELECT CustomerName, ContactName, Address
FROM Customers WHERE Address IS NOT NULL;
"""

### SQL UPDATE Statement

The 'UPDATE' statement is used to modify the existing records in a table.

* UPDATE Syntax
"""
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
"""
Note: Be careful when updating records in a table! Notice the 'WHERE' clause in the 'UPDATE' statement. The 'WHERE' clause specifies which record(s) that should be updated. If you omit the 'WHERE' clause, all records in the table will be updated!

* UPDATE Table
The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city.
Example:
"""
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
WHERE CustomerID = 1;
"""

* UPDATE Multiple Records
It is the WHERE clause that determines how many records will be updated.
The following SQL statement will update the ContactName to "Juan" for all records where country is "Mexico":
"""
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';
"""

* Update Warning!
Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!
Example:
"""
UPDATE Customers
SET ContactName='Juan';
"""

### SQL DELETE Statement

The 'DELETE' statement is used to delete existing records in a table.

* DELETE Syntax
"""
DELETE FROM table_name WHERE condition;
"""
Note: Be careful when deleting records in a table! Notice the 'WHERE' clause in the 'DELETE' statement. The 'WHERE' clause specifies which record(s) should be deleted. If you omit the 'WHERE' clause, all records in the table will be deleted!

* SQL DELETE Example
The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:
"""
DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
"""

* Delete All Records
1. It is possible to delete all rows in a table without deleting the table. This means that the table structure, attributes, and indexes will be intact:
"""
DELETE FROM table_name;
"""
2. The following SQL statement deletes all rows in the "Customers" table, without deleting the table:
Example:
"""
DELETE FROM Customers;
"""

* Delete a Table
To delete the table completely, use the 'DROP TABLE' statement.
Remove the Customers table:
"""
DROP TABLE Customers;
"""

### SQL TOP, LIMIT, FETCH FIRST or ROWNUM Clause

The SELECT TOP clause is used to specify the number of records to return.
The SELECT TOP clause is useful on large tables with thousands of records. Returning a large number of records can impact performance.

* Example
Select only the first 3 records of the Customers table:
"""
SELECT TOP 3 * FROM Customers;
"""
Note: Not all database systems support the SELECT TOP clause. MySQL supports the LIMIT clause to select a limited number of records, while Oracle uses FETCH FIRST n ROWS ONLY and ROWNUM.

### SQL MIN() and MAX() Functions

The MIN() function returns the smallest value of the selected column.
The MAX() function returns the largest value of the selected column.

* Syntax
"""
SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MAX(column_name)
FROM table_name
WHERE condition;
"""

* MIN Example
Find the lowest price:
"""
SELECT MIN(Price)
FROM Products;
"""

* MAN Example
Find the highest price:
"""
SELECT MAX(Price)
FROM Products;
"""

* Set Column Name (Alias)
When you use MIN() or MAX(), the returned column will be named MIN(field) or MAX(field) by default. To give the column a new name, use the 'AS' keyword:
"""
SELECT MIN(Price) AS SmallestPrice
FROM Products;
"""

### SQL COUNT() Function

The COUNT() function returns the number of rows that matches a specified criterion.

* Syntax
"""
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
"""

* Example
Find the total number of products in the Products table:
"""
SELECT COUNT( * )
FROM Products;
"""

* Add a Where Clause
You can add a WHERE clause to specify conditions.
Find the number of products where Price is higher than 20:
"""
SELECT COUNT(ProdustID)
FROM Products
WHERE Price > 20;
"""

* Specify Column
You can specify a column name instead of the asterix symbol ( * ).
If you specify a column instead of ( * ), NULL values will not be counted.
Find the number of products where the ProductName is not null:
"""
SELECT COUNT(ProductName)
FROM Products;
"""

* Ignore Duplicates
You can ignore duplicates by using the DISTINCT keyword in the COUNT function.
If DISTINCT is specified, rows with the same value for the specified column will be counted as one.
How many different prices are there in the Products table:
"""
SELECT COUNT(DISTINCT Price)
FROM Products
"""

* Use an Alias
Give the counted column a name by using the AS keyword.
Name the column "number of records":
"""
SELECT COUNT( * ) AS [number of records]
FROM Products;
"""

### SQL SUM() Function

The SUM() function returns the total sum of a numeric column.

* Syntax
"""
SELECT SUM(column_name)
FROM table_name
WHERE condition;
"""

* Example
Return the sum of all Quantity fields in the OrderDetails table:
"""
SELECT SUM(Quantity)
FROM OrderDetails;
"""

* Add a Where Clause
You can add a WHERE clause to specify conditions:
"""
SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductID = 11;
"""

* Use an Alias
Give the summarized column a name by using the AS keyword.
Name the column "total":
"""
SELECT SUM(Quantity) AS total
FROM OrderDetails;
"""

* SUM() With an Expression
The parameter inside the SUM() function can also be an expression.
If we assume that each product in the OrderDetails column costs 10 dollars, we can find the total earnings in dollars by multiply each quantity with 10.
Use an expression inside the SUM() parenthesis:
"""
SELECT SUM(Quantity * 10)
FROM OrderDetails;
"""

### SQL AVG() Function

The AVG() function returns the average value of a numeric column.

* Syntax
"""
SELECT AVG(column_name)
FROM table_name
WHERE condition;
"""

* Example
Find the average price of all products:
"""
SELECT AVG(Price)
FROM Products;
"""
Note: NULL values are ignored.

* Add a Where Clause
You can add a WHERE clause to specify conditions.
Return the average price of products in category 1:
"""
SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;
"""

* Use an Alias
Give the AVG column a name by using the AS keyword.
Name the column "average price":
"""
SELECT AVG(Price) AS [average price]
FROM Products;
"""

* Higher Than Average
To list all records with a higher price than average, we can use the AVG() function in a sub query.
Return all products with a higher price than the average price:
"""
SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);
"""

### SQL LIKE Operator
