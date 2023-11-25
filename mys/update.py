import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Samiul13",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_command = """
                 UPDATE Student
                 SET First_name = "Someone"
                 WHERE Roll = 13
            """
mycursor.execute(sql_command)
mydb.commit()