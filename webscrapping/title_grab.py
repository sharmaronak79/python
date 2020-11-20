import requests

result = requests.get("https://en.wikipedia.org/wiki/Mahatma_Gandhi")

type(result)

result.text

import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")

soup

soup.select('title')

soup.select('title')[0]

soup.select('title')[0].getText()

site_paragraphs = soup.select('head')



site_paragraphs[0]

site_paragraphs[0].getText()

