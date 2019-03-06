import requests

from bs4 import BeautifulSoup

keywords = ["KI", "AI", "Big Data", "Data", "data", "big data", "Analytics", "analytics", "digitalisierung", "ML",
            "Machine Learning"]

headers = ""

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"

data = requests.get('https://www.auftrag.at//tenders.aspx')

soup = BeautifulSoup(data.text, 'html.parser')

jobs = soup.find_all('div', {'class': 'main-cont'})

print(jobs.text)


"""
For links use 

links = []

for link in jobs.find_all('a'):
    links.append(link.get('href'))

"""


