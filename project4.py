import requests
from bs4 import BeautifulSoup

res = requests.get ("https://divar.ir/s/tehran")

soup = BeautifulSoup (res.text, "html.parser")

items = soup.find_all ("div", attrs={"class": "kt-post-card__body"})


for i in range (len (items)):
    if (items[i].find ("div", attrs={"class": "kt-post-card__description"}) != None):
        if (items[i].find ("div", attrs={"class": "kt-post-card__description"}).text == "توافقی"):
            print (items[i].find ("h2", attrs={"class": "kt-post-card__title"}).text)

