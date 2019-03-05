import requests

from bs4 import BeautifulSoup

data = requests.get('https://www.auftrag.at/Search.aspx?searchfilter=software&nutscode=AT')

soup = BeautifulSoup(data.text, 'html.parser')

print(data.text)