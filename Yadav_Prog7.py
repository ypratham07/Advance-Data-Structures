#Author: Pratham Ramkripal Yadav
#Creation Date: 12 December 2023

import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

'''
Description: 
The following program tries to extract the names of all the books that are listed on the Web Page of the below URL

'''

# URL to scrape 
url = "https://www.flipkart.com/search?q=python%20books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# Make HTTP request and parse HTML content 
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Function to clean text  
def clean_text(text):
    return re.sub(r'\W+', '', text)

# Lists to store book info
titles = []
prices = [] 
ratings = []

# Find all books on page
for div in soup.findAll('div', attrs={'class':'_1AtVbE col-12-12'}):
    
    # Extract Title
    title = div.find('div', attrs={'class':'_4rR01T'}) 
    if title:
        titles.append(title.text)
    else:
        titles.append('NA')
        
    # Extract Price 
    price = div.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    if price: 
        price = clean_text(price.text)
        prices.append(int(price[1:]))
    else:
        prices.append(0)
    
    # Extract Rating
    rating = div.find('div', attrs={'class':'_3LWZlK'})  
    if rating:
        ratings.append(float(rating.text)) 
    else:
        ratings.append(0)
        
# Print book with highest price        
highest_price = max(prices)  
print("Book with the Highest Price is:", titles[prices.index(highest_price)])

# Print book with highest rating
highest_rating = max(ratings)
print("Book with Highest Rating is:", titles[ratings.index(highest_rating)])

# Print book with lowest price
lowest_price = min(prices)
print("Book with Lowest Price is:", titles[prices.index(lowest_price)])   

# Print book with lowest rating
lowest_rating = min(ratings)
print("Book with lowest Rating is:", titles[ratings.index(lowest_rating)])

# Scatter plot
plt.scatter(prices, ratings)
plt.xlabel('Price')
plt.ylabel('Rating')
plt.title('Rating vs Price') 
plt.show()