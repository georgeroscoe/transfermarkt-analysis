#!python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

urls = ['https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/saison_id/ges/wettbewerb_id/CL/plus/1/page/1',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/saison_id/ges/wettbewerb_id/CL/plus/1/page/2',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/plus/1?saison_id=ges&wettbewerb_id=GB1',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/1',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/2',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/3',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/4',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/5',
'https://www.transfermarkt.co.uk/cristiano-ronaldo/elfmetertore/spieler/8198/plus/1?saison_id=ges&wettbewerb_id=IT1']

d = []
for page in urls:


#url = "https://www.transfermarkt.co.uk/lionel-messi/elfmetertore/spieler/28003/ajax/yw1/saison_id/ges/wettbewerb_id/ES1/plus/1/page/1"
    res = requests.get(page, headers={'User-Agent': 'Custom5'})
    soup = BeautifulSoup(res.text, "lxml")


    grouped_data = soup.find_all('div', {'class': 'responsive-table'})

    goals_data = grouped_data[0]

    #goals = int(grouped_data.find_all('td', {'class':'zentriert'})[8])
    rows = goals_data.find_all('tr',{'class':['even','odd']})



    for row in rows:
        cells = row.find_all("td", {'class': 'zentriert'})

        a = cells[2].text.strip().encode()
        date = a.decode("utf-8")

        d.append(date)
                #d.append((cells[1].text.strip(),cells[6].text.strip(),times[0].text.strip().strip("'")))

print(d)
print(len(d))

with open('ronaldopens.csv', "w") as f:
     writer = csv.writer(f)
     for val in d:
        writer.writerow([val])
