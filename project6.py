import mysql.connector
import requests
from bs4 import BeautifulSoup
import csv
from sklearn import tree

def create_database ():
    cnx = mysql.connector.connect (host="localhost", user="root", password="")
    cursor = cnx.cursor ()
    cursor.execute ("CREATE DATABASE test")
    cursor.execute ("CREATE TABLE cars ( name VARCHAR (100), year INT, km INT, price INT)")
    cnx.close ()

def read_page (page):
    if (page == 1):
        res = requests.get ("https://mashinbank.com/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%AE%D9%88%D8%AF%D8%B1%D9%88")
    else:
        res = requests.get ("https://mashinbank.com/%D8%AE%D8%B1%DB%8C%D8%AF-%D8%AE%D9%88%D8%AF%D8%B1%D9%88?page=" + str (page))

    soup = BeautifulSoup (res.text, "html.parser")

    cars = soup.find_all ("a", attrs={"class": "cars-item-card"})

    items = []

    for i in range (len (cars)):
        name = cars[i].find ("div", attrs={"class": "cars-title"}).text

        year = cars[i].find ("div", attrs={"class": "cars-year"}).text
        year = year.split ()
        year = year[0]
        year = int (year)

        km = cars[i].find ("span", attrs={"style": "font-size:1.2em;"}).text
        km = km.replace (",", "")

        price = cars[i].find ("div", attrs={"class": "cars-price"}).text
        price = price.split ()
        price = price[0]
        price = price.replace (",", "")

        if (year >= 2000):
            continue
        if (km == "حواله"):
            continue
        elif (km == "صفر"):
            km = 0
    
        km = int (km)

        if (price == "توافقی"):
            continue
        
        price = int (price)

        items.append ([name, year, km, price])

        return items

page = 1
items = []

while (len (items) < 30):
    items = items + read_page (page)
    page = page + 1

cnx = mysql.connector.connect (host="localhost", user="root", password="", database="test")

cursor = cnx.cursor ()

for i in range (len (items)):
    name = "\"" + items[i][0] + "\""
    year = "\"" + str (items[i][1]) + "\""
    km = "\"" + str (items[i][2]) + "\""
    price = "\"" + str (items[i][3]) + "\""

    cursor.execute ("INSERT INTO cars VALUES (" + name + "," + year + "," + km + "," + price ")")
    cursor.commit ()

cnx.close ()

x = []
y = []

for i in range (len (items)):
    x.append ([items[i][1], items[i][2]])
    y.append (items[i][3])

clf = tree.DecisionTreeClassifier ()
clf = clf.fit (x, y)