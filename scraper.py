from bs4 import BeautifulSoup
import requests
import csv


# URL to the website
url='http://www.stackoverflow.com/questions'

# Getting the html file and parsing with html.parser
html=requests.get(url)
bs=BeautifulSoup(html.text,'html.parser')

# Tries to open the file 

csv_file=open('stack_overflow.csv','w')
fieldnames=['question','author']
dictwriter=csv.DictWriter(csv_file,fieldnames=fieldnames)

# Writes the headers
dictwriter.writeheader()


# Loops through quote in the page

for post in bs.findAll('div', {'class' : 'question-summary'})[:10]:
    question = post.find('a', {'class': 'question-hyperlink'}).text
    author = post.find('div', {'class' : 'user-details'}).text.split('\n')
    dictwriter.writerow({'question':question, 'author': author[1]})


csv_file.close()