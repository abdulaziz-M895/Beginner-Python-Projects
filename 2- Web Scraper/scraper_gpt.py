from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Combine the find_all calls to improve efficiency
books = soup.find_all('article', class_='product_pod')

# Add the data to a data.txt file instead of printing it
file = open('data.txt', 'wt')

for book in books:
    title = book.h3.a['title']
    rating = book.find('p')['class'][1]
    price = book.find('p', {'class': 'price_color'}).text
    
    print(f'Title: {title}', file=file)
    print(f'Rating: {rating.capitalize()} stars', file=file)  # Capitalize the rating for consistency
    print(f'Price: {price}', file=file)
    print('-----------------', file=file)

file.close()