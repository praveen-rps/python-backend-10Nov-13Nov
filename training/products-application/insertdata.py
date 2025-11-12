
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
query = "insert into books(bookid,name,author) values(?,?,?)"
data = ("1001","Java", "Kumar")

cursor.execute(query,data)

conn.commit()


# 5. Process the result 



# 6. close the connection to database
print("Record inserted successfully...!")
conn.close()