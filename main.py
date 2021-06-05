import requests
import re

if __name__ == '__main__':
  with open('econpy.html', 'r') as file:
    content = file.read()
    regex = '<div title="buyer-name">(.+?)</div>'
    for title in re.findall(regex, content):
      print(title)