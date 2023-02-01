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

# Create function to calculate the number of pages:
def quantity_pages():
    start_page = 1
    current_page = start_page
    while True:
        url_current_page = url + str(current_page)
        soup = getparse(url_current_page)
        if istherenextpage(soup):
            current_page += 1
        else:
            break
    last_page = current_page
    return last_page

number_pages = quantity_pages()

info_units = {'name': [], 'address': [], 'phone': []}

def istherephone(complete_address):
    return (len(complete_address) == 2)


#Get information for each page:
for page_index in range(1, number_pages):
    current_page = f'https://www.totvs.com/unidade/page/{page_index}'
    soup = getparse(current_page)
    units = soup.find_all('a', class_=re.compile('card card-simple'))

    #Get informataion for each unit:
    for unit in units:
        name = unit.find('h3', class_=re.compile('h4 text-dark font-weight-bolder mb-1')).get_text().strip()
        complete_address = unit.find_all('p', class_=re.compile('mb-0'))
        address = complete_address.text

