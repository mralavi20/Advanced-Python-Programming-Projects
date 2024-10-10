import mysql.connector

cnx = mysql.connector.connect (user = 'root', password = '', host = 'localhost', database = 'test')

cursor = cnx.cursor ()

query = 'SELECT * FROM people;'
cursor.execute (query)

persons = []

for (name, weight, height) in cursor:
    p = [name, weight, height]
    persons.append (p)

cnx.close ()

for i in range (len (persons)):
    for j in range (i, len (persons)):
        if (persons[i][2] < persons[j][2]):
            persons[i],persons[j] = persons[j],persons[i]
        elif (persons[i][2] == persons[j][2] and persons[i][1] > persons[i][1]):
            persons[i],persons[j] = persons[j],persons[i]

for i in range (len (persons)):
    print (persons[i][0], persons[i][2], persons[i][1])