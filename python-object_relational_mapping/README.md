# Python - Object-relational mapping

---

## Connecting to a MySQL Database from a Python Script

To connect to a MySQL database using Python, you can use the `mysql-connector` library. Ensure you have it installed by running:

```bash
pip install mysql-connector-python
```

Next, you can use the following Python code in your script to establish a connection to your MySQL database:

```python
import mysql.connector

# Replace these values with your actual database connection details
db_config = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Connect to the database
conn = mysql.connector.connect(**db_config)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# ... perform database operations ...

# Close the cursor and connection when done
cursor.close()
conn.close()
```

Replace `'your_host'`, `'your_username'`, `'your_password'`, and `'your_database'` with your specific database connection details.

---

## SELECT Rows in a MySQL Table from a Python Script

After connecting to the database, you can execute a SELECT query to retrieve rows from a MySQL table. For example:

```python
# Assuming you have a table named 'example_table'
query = "SELECT * FROM example_table"

# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Process the rows
for row in rows:
    print(row)
```

This code assumes a table named 'example_table'. Adjust the query and table name based on your specific database structure.

---

## INSERT Rows in a MySQL Table from a Python Script

To insert rows into a MySQL table, you can use the following code snippet:

```python
# Assuming you have a table named 'example_table' with columns 'column1' and 'column2'
data = ('value1', 'value2')
query = "INSERT INTO example_table (column1, column2) VALUES (%s, %s)"

# Execute the query
cursor.execute(query, data)

# Commit the changes to the database
conn.commit()
```

Adjust the `data` tuple and query based on your table structure and the values you want to insert.

---

## Object-Relational Mapping (ORM)

Object-Relational Mapping (ORM) is a programming technique that facilitates the interaction between a relational database and an object-oriented programming language. In Python, SQLAlchemy is a popular ORM.

---

## Map a Python Class to a MySQL Table using SQLAlchemy

Using SQLAlchemy, you can map a Python class to a MySQL table. Ensure you have the necessary packages installed:

```bash
pip install mysql-connector-python sqlalchemy
```

Then, create a Python class representing your table and use SQLAlchemy to interact with the database. For example:

```python
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these values with your actual database connection details
db_url = 'mysql+mysqlconnector://your_username:your_password@your_host/your_database'
engine = create_engine(db_url)

Base = declarative_base()

# Define a Python class that represents your table
class ExampleTable(Base):
    __tablename__ = 'example_table'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    column1 = Column(String(50))
    column2 = Column(String(50))

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Use the class to perform database operations
new_row = ExampleTable(column1='value1', column2='value2')
session.add(new_row)
session.commit()

# Query the table
result = session.query(ExampleTable).all()
for row in result:
    print(row.id, row.column1, row.column2)

# Close the session when done
session.close()
```

Replace the placeholders in the `db_url` with your actual database connection details and customize the `ExampleTable` class based on your table structure.

---
