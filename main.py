from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    # div = soup.find_all('div', {'title': 'buyer-name'})[0]
    span = soup.find('span', class_='item-price')
    for element in span.parents:
      print(element.name)