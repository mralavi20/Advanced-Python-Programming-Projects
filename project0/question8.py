import datetime

year,month,day = str (input ()).split ("/")
year = int (year)
month = int (month)
day = int (day)

if (year <= 0 or month <= 0 or month > 12 or day <= 0 or day > 31):
    print ("WRONG")
else:
    today = datetime.datetime.now ()
    days1 = today.year * 365 + today.month * 30 + today.day
    days2 = year * 365 + month * 30 + day
    age_day = days1 - days2
    age = int (age_day / 365)
    print (age)
