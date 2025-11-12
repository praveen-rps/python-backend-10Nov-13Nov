
# 1. import the required lib or modules
import sqlite3
#import mysql-connector


# 2. Establish the connection
conn = sqlite3.connect("books.db")
"""
conn = mysql.connector.connect(
username=root,
password=root,
port=3306,
host=loclahost,
database=products
)
"""
# 3. Create a cursor object 
cursor = conn.cursor()

# 4. Write the query and execute  it
query = "select * from books"


cursor.execute(query)
rows = cursor.fetchall()


if rows is None:
    print("No records found")


# 5. Process the result 

for row in rows:
    print(row[0], " " ,row[1], " " ,row[2])


# 6. close the connection to database

conn.close()