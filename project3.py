import mysql.connector
import re

cnx = mysql.connector.connect (host="localhost", user="root", password="root", database="test")

cursor = cnx.cursor ()

email_input = str (input ("Enter email: "))

email_format = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
while (not re.fullmatch (email_format, email_input)):
    print ("Invalid email address try again")
    print ("Email format: expression@string.string")
    email_input = str (input ("Enter email: "))

password_input = str (input ("Enter password: "))

email_input = "\"" + email_input + "\""
password_input = "\"" + password_input + "\""

cursor.execute ("INSERT INTO email VALUES (" + email_input + "," + password_input + ")")
cnx.commit ()

cnx.close ()