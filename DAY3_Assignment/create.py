# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter department : ")
email = input("Enter email :")
salary = input("Enter salary : ")
dateofjoining = input("Enter dateofjoining : ")
query = f"insert into employee values('{empid}', '{name}', '{department}', '{email}', '{salary}','{dateofjoining}');"

# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()



