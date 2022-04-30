from selenium import webdriver
import time 
import csv
from bs4 import BeautifulSoup

START_URL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=webdriver.Chrome('https://chromedriver.chromium.org/downloads')
browser.get(START_URL)

time.sleep(10)
def scrape():
    headers=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']
    planet_data=[]
    for i in range(0,428):
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
            planet_data.append(temp_list)
        browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div').click()

    with open('scraper_2.csv','w') as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()