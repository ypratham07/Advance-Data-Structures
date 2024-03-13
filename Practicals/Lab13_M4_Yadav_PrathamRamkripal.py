#Name:       Pratham Ramkripal Yadav  
#Date:       29 November 2023
#Assignment: Lab 13
#Class:      CPS 596
'''
Description : The following program fetches the data from website and prints all the 
links, paragraphs and headings with help of python libraries like resuests and beautifulsoup
'''

#importing libraries
import requests
from bs4 import BeautifulSoup

#getting the url in variabe
url="https://realpython.github.io/fake-jobs/"
#sending the get request and storing the response in response variable
response=requests.get(url)

#paring the reponse through beautiful soup
soup = BeautifulSoup(response.content,'html.parser')


#using findall() function to get all the paragraphs from response
paragraphs=soup.find_all('p')

#printing the paragraphs
print("\nParagraphs\n")
for i in paragraphs:
    print(i.text)


#using findall() function to get all the links from response
links=soup.find_all('a',href=True)

#printing the links
print("\nLink\n")
for i in links:
    print (i['href'])
    

#using findall() function to get all the headings from response
headings=soup.find_all(['h1','h2','h3','h4','h5','h6'])

#printing the headings
print("\nHeading\n")
for i in headings:
    print(i.text.strip())
