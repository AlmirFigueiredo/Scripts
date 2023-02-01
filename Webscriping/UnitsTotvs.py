import requests
import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Declare User-Agent to avoid problems with permissions:
headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                         "Safari/537.36"}
# Declare url address:
url = 'https://www.totvs.com/unidade/page/'

# Create html Session:
session = HTMLSession()

#Create Function to get parsing:
def getparse(url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# Create Function to know if there is next page:
def istherenextpage(soup):
    page = soup.find('ul', {'class': 'pagination justify-content-center'})
    if page.find('li', {'class': 'page-item next'}):
        return True
    else:
        return False
        

