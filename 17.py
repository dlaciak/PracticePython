import requests
from bs4 import BeautifulSoup


odpowiedz = requests.get("https://www.nytimes.com/")
odpowiedzHTML = odpowiedz.text


soup = BeautifulSoup(odpowiedzHTML, 'html.parser')
#title = soup.find('span', 'articletitle').string




