
import os
import pathlib
import requests
import json

from pprint import pprint

from bs4 import BeautifulSoup
from selenium import webdriver

from urllib.parse import urljoin



def get_response(url):  
    response = requests.get(url)
    response.raise_for_status()
    return response


url1 = "https://xn--80aesfpebagmfblc0a.xn--p1ai/information/"

link = urljoin("https://xn--80aesfpebagmfblc0a.xn--p1ai/information/",
"/covid_data.json?do=region_stats")
                         
                         
def parse_page(response):
    soup = BeautifulSoup(response.text,
                         "html.parser")
    
    tags = soup.select_one('.d-map__indicator d-map__indicator_hospitalized')
    tags2 = tags
    #"#app  article  section:nth-child(2)  div.cv-section__content").find(
    #'cv-spread-overview')
    
    # section div.cv-spread-overview__table  div  table")
    #soup.find(id='app').find(class_="cv-content").find_all(
    #class_= 'cv-section')[1].find(class_ = 'cv-spread-overview')
    
    #app > article > section:nth-child(2) > div > div > section > div.cv-spread-overview__table > div > table
    
    #region-data-url="/covid_data.json?do=region_stats"
    return tags
    
    ##[x.get['data-url'] for x in soup.find_all ('tr')]
   
    #> article > section:nth-child(2) > div > div > section > div.cv-spread-overview__table')
#app > article > section:nth-child(2) > div > div > section > div.cv-spread-overview__table > div > table > tbody > tr:nth-child(7)

if __name__ == "__main__":

    link = "https://xn--80aesfpebagmfblc0a.xn--p1ai/information/"
    ops = webdriver.ChromeOptions()
    ops.add_argument('headless')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    #os.environ["webdriver.chrome.driver"] = driver
    driver.get(link)
    page_link=driver.page_source
    soup = BeautifulSoup(page_link,
                         features="html.parser")
    tags = soup.select_one('.d-map__list')
    col_healed = tags.select('td')
    
    print(col_healed)


