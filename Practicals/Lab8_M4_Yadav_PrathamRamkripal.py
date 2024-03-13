#Author: Pratham Ramkripal Yadav    
#Assignment: Lab 8
#Class: Advance Data Structures
#Date: 25 October 2023

'''
Description: The Program uses OOPS fundamentals to store different parameters of books like name of title, 
number of pages, name of author and price of book along with discount. 
It also contains store class which stores all the books along with the store name
'''

#Declaring a Book Class
class Book:
    def __init__(self, title, pages, author, price):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price

    #defining setDiscount() function to set discount value for book
    def setDiscount(self, amount):
        self.discount = amount

    #defining getPrice() function to return price of book
    def getPrice(self):
        return self.price

# Q3: create class function - getPriceAfterDiscount(self): which returns the price after discount
    #defining getPriceAfterDiscount() function to return the price of book after discount
    def getPriceAfterDiscount(self):
        self.DiscountedPrice=round(self.price-self.discount,2)
        return self.DiscountedPrice

# Q4: Create another class store, with attributes books, storeName, where books is a list.
#defining Store Class
class Store:
    #defining init() funtion of store class to assign values to variables
    def __init__(self,books,store):
        self.books=books
        self.store=store 

# Q1: create 3 books with title, pages, author, and price
book1=Book('To Kill a MockingBird',528,'Harper Lee',16.90)
book2=Book('Jane Eyre',680,'Charlotte Bronte',20.02)
book3=Book('Atomic Habits',320,'James Clear',13.79)

# Q2: print the price of all three books
print("Price of",book1.title,"is",book1.getPrice(),"USD")
print("Price of",book2.title,"is",book2.getPrice(),"USD")
print("Price of",book3.title,"is",book3.getPrice(),"USD","\n",)


# Q4: set discounts for the 3 books, print the the price before and after
#setting discount values of different books
book1.setDiscount(1.99)
book2.setDiscount(2.99)
book3.setDiscount(3.99)

#printing values of books before and after discount
print("Book Name : ",book1.title,"\n","Price Before Discount : ",book1.price,"USD","\n","Price After Dicount : ",book1.getPriceAfterDiscount(),"USD","\n")
print("Book Name : ",book2.title,"\n","Price Before Discount : ",book2.price,"USD","\n","Price After Dicount : ",book2.getPriceAfterDiscount(),"USD","\n")
print("Book Name :",book3.title,"\n","Price Before Discount : ",book3.price,"USD","\n","Price After Dicount : ",book3.getPriceAfterDiscount(),"USD","\n")


# Q5: Create instance of store, append all books to store.books and then print all the prices of the stores books.

#Creating an instance of store class
store1=Store([book1,book2,book3],"Charles Book Store")

#printing all th prices of stores books
for i in store1.books:
    print("Book Name: ",i.title,"\n","Price: ",i.price,"\n")
