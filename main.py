from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')

    div = soup.find_all('div', {'title': 'buyer-info'})
    for child in div[0].children:
      print(child)