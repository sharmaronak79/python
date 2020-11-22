import requests
import bs4

'http://books.toscrape.com/catalogue/page-2.html'

'http://books.toscrape.com/catalogue/page-3.html'

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

base_url.format('20')

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml')

len(soup.select('.product_pod'))

soup.select('.product_pod')

products = soup.select('.product_pod')

example = products[0]

example

example.select('.star-rating.Two')  #'.xyz is a class and space is removed by . '

example.select('.star-rating.Three')  # star-rating.three is present so it will show detail

example.select('a')

example.select('a')[1]

type(example.select('a')[1])   # this is bs4 element , so, we can use as dictionary

example.select('a')[1]['title']

# we can check if something is 2 star using (string call in or example.select(rating))
# example.select('a')[1]['title'] to grab the book title

two_star_title = []

for n in range(1,51):
    
    scrup_url = base_url.format(n)
    res = requests.get(scrup_url)
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')
    
    for book in books:
        
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)

two_star_title



