import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Samiul13",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql_command = """
                  INSERT INTO Student(Roll, First_name, Last_name)
                  VALUES(13, "Samiul", "Hasan");
                """

mycursor.execute(sql_command)
mydb.commit()