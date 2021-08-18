from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
driver = webdriver.Chrome('/Users/dayong/project/crawingpy/chromedriver')

html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

# 화면 이동
driver.get(url)
titles = []

driver.implicitly_wait(3)
resultfind = bsObject.find_all('a')


for link in resultfind:
    result = link.get('title')

    if result != None:
        titles.append(result)


print(titles)
