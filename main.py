from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find('div', {'title': 'buyer-info'})
    # div.contents = []
    div.div.string = ''
    span = div.span.extract()
    print(div)
    print(span)