import requests

import bs4

res = requests.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi')

soup = bs4.BeautifulSoup(res.text,'lxml')

soup

soup.select('.toclevel-1')

soup.select('.toclevel-1')[0]

for item in soup.select('.toclevel-1'):
    print(item.text)
############################################
NOW TRY FOR IMAGE
############################################
img_res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

img_sup= bs4.BeautifulSoup(img_res.text,'lxml')

img_sup

img_sup.select('.thumbimage')

img_sup.select('.thumbimage')[0]

computer=img_sup.select('.thumbimage')[0]

computer

computer['src']

<img
     src = "//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg">
