import requests
from bs4 import BeautifulSoup

url = 'http://patmerschool.com/' 

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
print(soup.find_all('p'))