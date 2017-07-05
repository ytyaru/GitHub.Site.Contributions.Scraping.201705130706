#!python3
# encoding: utf-8
# http://qiita.com/jnchito/items/8f44a3c52d4669fefa93

import requests
from bs4 import BeautifulSoup

username = 'ytyaru'
url = 'https://github.com/{username}'.format(username=username)
file_name = '{username}_contributions'.format(username=username)

r = requests.get(url)
r.raise_for_status()
html_str = r.text
with open('{file_name}.html'.format(file_name=file_name), 'w') as f:
    f.write(html_str)

soup = BeautifulSoup(html_str, 'html.parser') # html.parser, lxml
contributes = soup.find("svg", attrs={"class": "js-calendar-graph-svg"})
print(contributes)
with open('{file_name}.svg'.format(file_name=file_name), 'w') as f:
    f.write(str(contributes))

csv_str = ''
for rect in contributes.find_all('rect'):
    date = rect.get('data-date')
    count = rect.get('data-count')
    csv_str += "{date},{count}".format(date=date, count=count) + '\n'
print(csv_str)
with open('{file_name}.csv'.format(file_name=file_name), 'w') as f:
    f.write(csv_str)

