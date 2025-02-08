from bs4 import BeautifulSoup as bs
import requests

InCountry_cur = input("input the in country currency in BLOCK letters:")
OutCountry_cur = input("input the out country currency in BLOCK letters:")
def get_currency(InCountry_cur, OutCountry_cur):
    url = f'https://www.x-rates.com/calculator/?from={InCountry_cur}&to={OutCountry_cur}&amount=1'
    # print(url)
    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    rate = soup.find('span', class_="ccOutputRslt").get_text()
    # Trim for only float value and removing strings
    rate = float(rate[:-7])
    return rate
print(get_currency(InCountry_cur, OutCountry_cur))