import requests
from bs4 import BeautifulSoup
import re

import json

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

def scrape():
    print('Start scraping')
    # Making a GET request
    url = "https://www.ikhokha.com/shop/card-machines"

    options = Options()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)

    print('Get URL')
    driver.get(url)

    # # Parsing the HTML
    print('Parsing site')
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    driver.quit()

    print('Finding all specifications...')
    items = soup.find_all('div', class_='specifications')
    itemsjson = [];

    try:
        for item in items:
            itemjson = {
                "name": item.div.h3.text, 
                "price": re.sub('[^0-9\.]','',item.div.h4.text),
                "description": item.div.p.text
            }

            itemsjson.append(itemjson)
    except Exception as e:
        print('Can\'t parse items')
        print(str(e))
    finally:
        return itemsjson
