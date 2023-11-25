import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Samiul13",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_commad= """
                CREATE TABLE Student(
                Roll INT,
                First_name VARCHAR(20),
                Last_name VARCHAR(20)
                )
            """

mycursor.execute(sql_commad)