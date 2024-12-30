from bs4 import BeautifulSoup as bs
from urllib import request
import re
import pandas as pd

print("Fetching Data of Different Airports...")

# Adding top 100 airports in the world
page = request.urlopen("https://gettocenter.com/airports/top-100-airports-in-world")
soup = bs(page, features="html.parser")

column_names = ['city','airport','code','country']
df = pd.DataFrame(columns=column_names)

tr = soup.body.find_all('tr')

for r in tr:
    d = r.find_all('td')
    if len(d) < 5:  # Agar ustunlar yetarli bo'lmasa, keyingi satrga o'tadi
        continue
    # d = r.find_all('td')
    airport = d[1].text.strip()
    code = d[2].text.strip().upper()
    city = d[3].text.strip()
    country = d[4].text.strip()
    
    row = {
        'city': city,
        'airport': airport,
        'code': code,
        'country': country
    }
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)



# Adding top 30 airports in india
page = request.urlopen("https://www.worlddata.info/asia/india/airports.php")
soup = bs(page, features="html.parser")

tr = soup.body.find_all('table')[0].find_all('tr')

for r in tr[1:]:
    d = r.find_all('td')
    airport = d[1].text.strip()
    code = d[0].text.strip().upper()
    city = d[2].text.strip()
    country = 'India'
    
    row = {
        'city': city,
        'airport': airport,
        'code': code,
        'country': country
    }
    if len(df[df['code'] == code]):
        continue
    else:
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)


print("airports.csv faylidagi malumotlar bazaga yuklandi")
df.to_csv("airports.csv", index=False)

print("Bajarildi")
