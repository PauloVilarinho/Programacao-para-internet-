import requests
from bs4 import BeautifulSoup


html_text = requests.get('https://www.spacejam.com/archive/spacejam/movie/cmp/sitemap.html').text
html_content = BeautifulSoup(html_text.lower(), 'lxml').find_all(text=True)

for x in html_content:
    if x != '\n':
        print(x)
