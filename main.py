from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.new_tag('div', id='title', title='data')
    a = soup.new_tag('a', href='www.codigofacilito.com')
    a.string = 'Link a la plataforma'
    div.append('\n')
    div.append(a)
    div.append('\n')
    # soup.body.append(div)
    soup.body.insert(1, div)
    print(soup.prettify())