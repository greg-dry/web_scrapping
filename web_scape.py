import requests
import bs4
import lxml

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

soup = bs4.BeautifulSoup(r.text, 'lxml')

toc = soup.select('.toctext')

for t in toc:
    print(t.getText())








