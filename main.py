from bs4 import BeautifulSoup

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.head)
    print(type(soup.head))