import requests
import mysql.connector
from bs4 import BeautifulSoup

brand = str (input ("Enter Brand: "))
model = str (input ("Enter Model or all: "))

if (model == "all"):
    site_address = "https://www.truecar.com/used-cars-for-sale/listings/" + brand + "/location-java-va/"
else:
    site_address = "https://www.truecar.com/used-cars-for-sale/listings/" + brand + "/" + model + "/location-java-va/"

res = requests.get (site_address)

soup = BeautifulSoup (res.text, "html.parser")

cars = soup.find_all ("div", attrs={"class": "card-content"})

cnx = mysql.connector.connect (host="localhost", user="root", password="", database="test")

cursor = cnx.cursor ()

if (len (cars) < 20):
    size = len (cars)
else:
    size = 20

for i in range (size):
    price = cars[i].find ("div", attrs={"class": "heading-3"}).text
    a = (cars[i].find ("div", attrs={"data-test": "vehicleMileage"}).text).split ()
    mileage = a[0]
    price = "\"" + price + "\""
    mileage = "\"" + mileage + "\""

    cursor.execute ("INSERT INTO cars VALUES (" + price + "," + mileage + ")")
    cursor.commit ()

cnx.close ()