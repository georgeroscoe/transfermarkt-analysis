#!python3
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://www.transfermarkt.co.uk/cristiano-ronaldo/leistungsdatendetails/spieler/8198/plus/1?saison=&verein=&liga=&wettbewerb=PO1"
res = requests.get(url, headers={'User-Agent': 'Custom5'})
soup = BeautifulSoup(res.text, "lxml")

grouped_data = soup.find_all('div', {'class': 'responsive-table'})
goals_data = grouped_data[1]
rows = goals_data.find_all('tr')

d = []

for row in rows:
    cells = row.find_all("td", {'class': 'zentriert'})
    times = row.find_all("td", {'class': 'rechts'})

    if len(cells) == 14:

        a = cells[1].text.strip().encode()
        date = a.decode("utf-8")
        b = cells[6].text.strip().encode()
        goals = b.decode("utf-8")
        c =  times[0].text.strip().strip("'").encode()
        minutes = c.decode("utf-8")

        if goals == '':
            goals = '0'
        d.append((date,goals,minutes))
    else:
        continue

with open('ronaldonos.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['date','goals','minutes'])
    for row in d:
        csv_out.writerow(row)
