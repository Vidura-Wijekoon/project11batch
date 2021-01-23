
import requests
from bs4 import BeautifulSoup

sl = "https://en.wikipedia.org/wiki/Districts_of_Sri_Lanka"

source = requests.get(sl).text

soup = BeautifulSoup(source, "lxml")

reviews = soup.find('table', class_ = 'wikitable')



A = []
B = []
C = []
D = []
E = []
F = []


for row in reviews.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
import pandas as pd

df = pd.DataFrame()

df['State or UT'] =  A
df['Admin Cap'] =  B
df['Legis Cap'] =  C
df['Judi Cap'] =  D
df['Year'] =  E
df['Formar Cap'] =  F


df.to_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/states1.csv', index = False)



import sqlite3 as sql
import pandas as pd

#open the connection
conn = sql.connect('states.db')

df.to_sql('statetable', conn)


#load the database table back to dataframe
conn = sql.connect('states.db')
new_df = pd.read_sql('SELECT * FROM statetable',conn)


pd.read_sql('SELECT * FROM statetable WHERE District  ==Vavuniya',conn)

pd.read_sql('SELECT * FROM statetable WHERE Province == Eastern',conn)


conn.execute('SELECT * FROM statetable').fetchall()


conn.execute('SELECT * FROM statetable').fetchone()



#one more way

conn = sql.connect('states.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM statetable")

for record in cursor:
    print (record)






