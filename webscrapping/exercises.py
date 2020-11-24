# TASK /: IMPORT ANY LIBRARIES YOU THINK YOU WILL NEED TO SCRAP A WEBSITE

import requests
import bs4

# TASK : USE REQUESTS LIBRARY AND BEAUTIFULSOUP TO CONNECT TO http://quotes.toscrape.com/ AND GET THE HTML TEXT FROM THE HOMEPAGE

res = requests.get('http://quotes.toscrape.com')    



soup=bs4.BeautifulSoup(res.text,'lxml')

soup

soup.select('.author')

authors=set()

for name in soup.select('.author'):
    authors.add(name.text)

authors

# TASK TO CREATEA LIST OF ALL QUOTES ON THE FIRST PAGE

soup.select('.text')

quotes=[]

for quote in soup.select('.text'):
    quotes.append(quote.text)

quotes

# TASK : INSPECT THE SITE AND USE BEAUTIFUL SOUP TO EXTRACT THE TOP TEN TAGS FROM THE REQUESTS TEXT SHOWN ON THE TOP RIGHT FROM 
# THE HOME PAGE (E.G LOVE, INSPIRATIONL, LIFE ETC) 


soup.select('.tag-item')

for item in soup.select('.tag-item'):
    print(item.text)

# TASK : NOTICE HW THERE IS MORE THAN ONE PAGE , AND SUBSEQUENT PAGES LOOK LIKE THIS 

url='http://quotes.toscrape.com/page/{}/'

authors=set()


for page_number in range(1,10):
    page_url=url.format(page_number)
    result = requests.get(page_url)
    
    soup_page=bs4.BeautifulSoup(result.text,'lxml')
    
    for name in soup_page.select('.author'):
        authors.add(name.text)

authors



# TASK : IF YOU DO NOT KNOW THE LAST NUMBER OF PAGE THEN WHAT WE CAN DO
authors_name=set()
for page_number in range(1,20):
    page_url=url.format(page_number)
    result = requests.get(page_url)
    
    soup_page=bs4.BeautifulSoup(result.text,'lxml')
    
    if not "No quotes found!" in result.text:
        for name in soup_page.select('.author'):
            authors_name.add(name.text)
    else:
        break
        
    
    


authors_name







"No quotes found!" in result.text



page_still_valid = True
authors_name=set()
page=1

while page_still_valid:
    page_url = url.format(page_number)
