from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    """ Primera forma de búsqueda por clases 
    for element in soup.find_all(attrs={'class':'item-price'}):
      print(element.text) 
    """

    for element in soup.find_all(class_='item-price'):
      print(element.text)