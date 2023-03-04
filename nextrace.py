import requests
from bs4 import BeautifulSoup

URL = 'https://www.formula1.com/en/racing/2023.html'

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    next_race = soup.find('div', {'class': 'f1-page-header--race'}).find('a').text.strip()
    race_time = soup.find('div', {'class': 'f1-race-details__date'}).text.strip()
    location = soup.find('div', {'class': 'f1-race-details__circuit'}).text.strip()
    print(f"The next F1 race is {next_race} at {location} on {race_time}.")
else:
    print(f"Error {response.status_code}: {response.text}")
