import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/racing/2023.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
race_title = soup.find('div', {'class': 'event-title f1--xxs'}).text
race_location = soup.find('div', {'class': 'event-place d-block'}).text

print(f'Next race: {race_title} at {race_location}')
