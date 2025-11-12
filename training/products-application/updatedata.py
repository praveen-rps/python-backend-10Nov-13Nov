
# 1. import the required lib or modules
import sqlite3
#import mysql-connector


# 2. Establish the connection
conn = sqlite3.connect("products.db")
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
query = "update product set name = ? where pid = ?"
data = ("HP Mouse",3)


cursor.execute(query,data)

print("Updated sucessfully..!")
# 6. close the connection to database
conn.commit()
conn.close()