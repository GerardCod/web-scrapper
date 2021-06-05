from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    # div = soup.find_all('div', {'title': 'buyer-name'})[0]
    div = soup.find('div', string='Carson Busses')
    """ 
    print(div.next_sibling) # Salto de línea
    print(div.next_sibling.next_sibling) # span
    print(div.next_sibling.next_sibling.next_sibling) # Salto de línea
    print(div.previous_sibling) # Salto de línea 
    """

    for element in div.next_siblings:
      print(element)

    for element in div.previous_siblings:
      print(element)