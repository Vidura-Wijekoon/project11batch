'''Automation using Selenium'''

'''Step 1 : Download the Web Drivers'''
#https://www.seleniumhq.org/download/

#installation for firefox
#https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

#installation for chrome
#https://sites.google.com/a/chromium.org/chromedriver/downloads


'''Step 2: Add Selenium library to python'''
# !pip install --upgrade pip
# !pip install selenium



"""
Real website data scrapping for Kerela Results
"""
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

#For Windows System
browser = webdriver.Chrome("D:/Internships/Forsk_batch11_ViduraWijekoon/Codes/chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")


browser.get(url)

sleep(2)

 
#school_code = browser.find_element_by_name("treg") 
school_code = browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input")

#School Code range from 1100 to 5104 
school_code.send_keys("2000")


sleep(2)


#get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result = browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')
get_school_result.click()


sleep(10)
 
html_page = browser.page_source

soup = BS(html_page)

# Now you can add your logic of reading from BeautifulSoup
sleep(10)


sleep(10)

browser.quit()



"""Login into Facebook"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "YOUR EMAILID"
password = "YOUR PASSWORD"
url = "https://www.facebook.com"

#For Windows System
#browser = webdriver.Chrome("c:/chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")
browser.get(url)

element = browser.find_element_by_id("email")
element.send_keys(user_name)
element = browser.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)

sleep(10)

browser.quit()


"""
Real website data scrapping for List of State and Union Territory using Selenium
"""
from selenium import webdriver
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#For Windows System
#browser = webdriver.Chrome("c:/chromedriver.exe")
#browser = webdriver.Firefox(executable_path="D:/geckodriver")

# For Mac System
#browser = webdriver.Chrome(executable_path="/Users/sylvester/chromedriver")
#browser = webdriver.Firefox(executable_path="/Users/sylvester/geckodriver")
browser.get(url)


right_table=browser.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())



import pandas as pd
df = pd.DataFrame()
df["State or UN"]=A
df["Admin Cap"]=B
df["Legis Cap"]=C
df["Judi Cap"]=D
df["Year"]=F

df.to_csv("former.csv")


browser.quit()