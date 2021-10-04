import csv
import sqlite3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver



# URL to the website
URL ='http://www.stackoverflow.com/questions'

# # Getting the html file and parsing with html.parser
html=requests.get(URL)
bs=BeautifulSoup(html.text,'html.parser')

# # Tries to open the file

csv_file=open('stack_overflow.csv','w')
fieldnames=['question','author']
dictwriter=csv.DictWriter(csv_file,fieldnames=fieldnames)

# # Writes the headers
dictwriter.writeheader()


# # Loops through quote in the page

for post in bs.findAll('div', {'class' : 'question-summary'})[:10]:
    question = post.find('a', {'class': 'question-hyperlink'}).text
    author = post.find('div', {'class' : 'user-details'}).text.split('\n')[1]
    date_asked = post.find('span', {'class' : 'relativetime'})['title']
    tags = post.findAll('a', {'class' : 'post-tag flex--item'})
    tag_list = [tag.text for tag in tags]
    dictwriter.writerow({'question':question, 'author': author[1]})

    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    cur.execute('INSERT INTO questions VALUES ("%s","%s","%s","%s")'%(question, author, date_asked, tag_list))
    con.commit()
    con.close()
csv_file.close()


# Selenium version


DRIVER_PATH = '/Users/philchaplin/Documents/documents/py131/selenium_practice/chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)
fieldnames1 = ['question1', 'author1']
driver.get(URL)
csv_file1 = open('selenium_stack_overflow.csv','w')
dictwriter=csv.DictWriter(csv_file1,fieldnames=fieldnames1)

dictwriter.writeheader()

posts =  driver.find_elements_by_class_name('summary')[:10]
for post in posts:
    question1 = post.find_element_by_class_name('question-hyperlink').text
    author1 = post.find_element_by_class_name('user-details').text.split('\n')
    dictwriter.writerow({'question1':question1, 'author1': author1[0]})

csv_file1.close()
driver.close()
