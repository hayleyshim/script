import requests
from bs4 import BeautifulSoup

re = requests.get('http://naver.com')

link = re.find('link')

soup = BeautifulSoup(re.text, 'html.parser')
soup.txt

link = soup.find('link')
link

link = soup.find_all('link')

para = soup.find_all('p')

para



