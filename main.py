import requests
from bs4 import BeautifulSoup

URL = '/pokedex/all'
DOMAIN = 'https://pokemondb.net'

def get_content(url):
  response = requests.get(url)
  if response.status_code == 200:
    content = response.text
    return BeautifulSoup(content, 'html.parser')
  else:
    return None

def get_species(url):
  soup = get_content(url)
  pokemon_table = soup.find('table', class_='vitals-table')
  species = pokemon_table.tbody.find_all('tr')[2].td.text
  return species
  

def show_pokemon_data():
  soup = get_content(DOMAIN + URL)
  table = soup.find('table', {'id': 'pokedex'})
    
  for row in table.tbody.find_all('tr', limit=5):
    columns = row.find_all('td', limit=3)
    name = columns[1].a.text
    types = [a.text for a in columns[2].find_all('a')] # List comprehension
    link = DOMAIN + columns[1].a['href']
    species = get_species(link)
    print(name, '-', *types, '-', species)


if __name__ == '__main__':
  show_pokemon_data()