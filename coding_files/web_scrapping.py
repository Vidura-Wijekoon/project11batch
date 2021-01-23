# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:45:02 2021

@author: user pc vidura97
"""


import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
    
 

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.etsy.com/listing/514988912/beach-tote-bags-for-women-canvas-print?ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=&ref=sr_gallery-1-45')
cust_name = []
review_list = []
rating = []

df = pd.DataFrame()

df['Customer Name']=cust_name


df['Reviews']=review_list

df['Rating']=rating

sleep(5)
html = driver.page_source
soup = BeautifulSoup(html,'lxml')


while(True):
    try:
        
        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')
        for i in range(4):
            try: 
                df['Customer Name'] =cust_name.append(soup.find_all('a',class_="wt-text-link wt-mr-xs-1")[i].getText().strip())
                
                df['Reviews'] = review_list.append(soup.find_all('p',class_="wt-text-truncate--multi-line wt-break-word")[i].getText().strip())
                
                df['Rating'] = rating.append(driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/span/input[1]').getText().strip())
                
            except:
                pass
        next_button = driver.find_element_by_xpath('//*[@id="reviews"]/div[2]/nav/ul/li[position() = last()]/a')
        next_button.click()
        sleep(5)
        
        
    except Exception as e:
        print('finish : ', e)
        break



df.to_csv(r'E:/reviews.csv',index=True)


import sqlite3 as sql

conn = sql.connect('etsy.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM statetable")

for record in cursor:
    print (record)


