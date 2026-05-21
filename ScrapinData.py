import requests
from bs4 import BeautifulSoup
import csv



page = requests.get("https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003105020-S")

def main(page):

    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    data = []
    
    section = soup.find_all('div', {'class' : 'angebotskontakt-bewerbungsdetails-wrapper'})

    def get_firma_infos(section):

        firma_name = section.find_all('div', {'class' : 'angebotskontakt'}).text.strip() 

        print(firma_name)

    print(section)       

main(page)