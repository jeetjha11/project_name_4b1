import mysql.connector

class ConnectToDb:

     def create_connection(self):
         connection = mysql.connector.connect(
             user="root",
             password="root",
             host="localhost",
             database="user_data12"
         )
         if connection.is_connected():
             cursor=connection.cursor()
             print("Connected")
             return cursor
         else:
             print("Something Wrong")