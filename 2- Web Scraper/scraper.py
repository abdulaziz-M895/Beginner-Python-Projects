from bs4 import BeautifulSoup;
import requests;

url = 'https://books.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h3')

ratings = soup.find_all('p',{'class': 'star-rating'})

titlesList = []
for title in titles:
  titlesList.append(title.a['title'])

ratingsList = []
for rating in ratings:
  ratingsList.append(rating['class'][1])

# Add the data to a data.txt file instead of printing it
file = open('data.txt', 'wt')

for i in range(len(titlesList)):
  print(f'Title: {titlesList[i]}', file=file)
  print(f'Rating: {ratingsList[i]} stars', file=file)
  print('-----------------', file=file)

file.close()