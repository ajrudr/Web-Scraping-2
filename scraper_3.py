import enum
from re import L
from attr import attrs
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import pandas as pd
import requests
import csv

START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Edge('')
browser.get(START_URL)

time.sleep(10)
planets_data=[]
headers=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date','planet_type','planet_radius','orbital_radius',
'orbital_period','eccentricity']

def scrape():
    for i in range(1,5):
        while True :
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,'html.parser')

    for ul_tag in soup.find_all('ul',attrs={'class','exoplanet'}):
        li_tags=ul_tag.find_all('li')
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append('')

scrape()

new_planets_data=[]

def scrape_more_data(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,'html.parser')
        temp_list=[]
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

for index,data in enumerate(planets_data):
    scrape_more_data(data[5])
    print(f'scraping@hyperlink{index+1} is completed')
print(new_planets_data[0:10])

final_planet_data=[]

for index,data in enumerate(planets_data):
    new_planets_data_element=new_planets_data[index]
    new_planets_data_element=[elem.replace('\n','')for elem in new_planets_data_element]
    new_planets_data_element=new_planets_data_element[:7]
    final_planet_data.append[data+new_planets_data_element]

with open ('final.csv','w') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_planet_data)