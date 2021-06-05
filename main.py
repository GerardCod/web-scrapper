from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find('div', {'title': 'buyer-info'})
    div['id'] = 'item01'
    div['title'] = 'new-title'

    div.div.string = 'GerardCod'
    print(div.get('titles', 'default'))
    print(div)