# Урок от 06.07.2021
# API - application programming interface
# use requests and beautifulsoup4

import requests
from bs4 import BeautifulSoup

doc = requests.get("https://google.com/search?q=рыбки")
soup = BeautifulSoup(doc.text)
for i in soup.find_all("a"):
    print(i.attrs["href"])
    print(i)
