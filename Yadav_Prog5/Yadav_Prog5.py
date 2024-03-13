#Author: Pratham Ramkripal Yadav
#Creation Date: 25 October 2023
#Assignment: 05
'''
Description: The following program makes 3 class to store different parameters of book, 
other 2 classes Young() and Adult() are inherited from parent book class.
The program contains 4 functions to add a book , delete a book based on author , 
read a book from a particular author and view details of book. 

'''
#Importing necessary libraries
import os

#Declaring Book class 
class Book:
    def __init__(self,title,author,publication_date,price,readers_category):
        #assigning values from the parameters passed
        self.title=title
        self.author=author
        self.publication_date=publication_date
        self.price=price
        self.readers_category=readers_category

#Declaring Young class inherited from Book Class  
class Young(Book):
        def __init__(self,title,author,publication_date,price):
            super().__init__(title,author,publication_date,price,"Young")

#Declaring Adult class inherited from Book Class  
class Adult(Book):
        def __init__(self,title,author,publication_date,price):
            super().__init__(title,author,publication_date,price,"Adult")

#defining a menu class to print the menu
def menu():
    print("1 : Add a book")
    print("2 : Delete a book")
    print("3 : View a book")
    print("4 : View the book file")
    print("5 : Exit")

#defining add_book() function to add the book
def add_book():
    
    #getting title from user 
    title=input("Enter Title of Book: ")
    #getting author from user
    author=input("Enter Author of Book: ")
    #getting publication_date from user
    publication_date=input("Enter Publication Date: ")
    #getting price from user
    price=input("Enter Price of Book: ")
    #getting readers_category from user
    readers_category=input("Enter Readers Category: ")

    #creating object based on readers_category 
    if(readers_category=="Young"):
        new_book=Young(title,author,publication_date,price)
    elif(readers_category=="Adult"):
        new_book=Adult(title,author,publication_date,price)
    
    #opening BookShop.txt file in append mode
    f = open("BookShop.txt", "a")
    #writing new line to the file
    f.write(new_book.title +","+ new_book.author +","+ new_book.publication_date +","+ new_book.price +","+ new_book.readers_category)
    #closing the BookShop.txt file
    f.close()

    #printing the success message 
    print("Book Sucessfully Added To Inventory!")

#defining delete_book() function to delete the book 
def delete_book(author):
    #opening BookShop.txt file in read + write mode
    f1=open("BookShop.txt","r+")
    #opening temp.txt file in write
    f2=open("temp.txt","w")

    #iterating through each line
    for i in f1.readlines():
        #if author is not in the iterated line
        if(author not in i):
            #write the line to new file
            f2.write(i)
    
    #close the BookShop.txt file
    f1.close()
    #close the temp.txt file
    f2.close()

    #delete the BookShop.txt file
    os.remove("BookShop.txt")

    #rename the temp.txt file to BookShop.txt
    os.rename("temp.txt","BookShop.txt")

#defining read_book() to print details of the book 
def read_book(author):
    #opening BookShop.txt file in read mode
    f=open("BookShop.txt","r")
    
    #iterating through each line in file
    for i in f.readlines():
        #if name of author matches book author
        if(author in i):
            #split each line between comma
            words=i.split(',')
            #printing book name
            print("Book Name: ",words[0])
            #printing book author
            print("Author: ",words[1])
            #printing published date
            print("Publised Date: ",words[2])
            #printing book price
            print("Price: ",words[3])
            #printing readers category
            print("Readers Category: ",words[4])
    
    #close the BookShop.txt file
    f.close()

#defining view_book() function to print details of al the books
def view_book():
    #opening BookShop.txt file in read mode
    f=open("BookShop.txt","r")

    #iterating through each line in file
    for i in f.readlines():
        #spliting each line on comma
        words=i.split(',')
        #printing book name
        print("Book Name: ",words[0])
        #printing author name
        print("Author: ",words[1])
        #printing published date
        print("Publised Date: ",words[2])
        #printing price
        print("Price: ",words[3])
        #printing readers category
        print("Readers Category: ",words[4])
    
    #close the BookShop.txt file
    f.close()  

#getting the name of the user
name=input("Enter Your Name: ")
#greeting the user
print("Hello", name,"!")
#informing the user that this program facilitates reading from and writing to the bookstores inventory file
print("This program facilitates reading from and writing to the bookstores inventory file.")

#start of while loop
while (True):
    #calling the menu function 
    menu()
    
    #getting user choice 
    choice=int(input("Enter Your Choice: "))  
    
    #when user enters 1 
    if(choice==1):
        #calling add_book() function
        add_book()
    
    #when user enters 2
    elif(choice==2):
        #getting the author name from user
        author=input("Enter Name of Author: ")
        #calling delete_book() function
        delete_book(author)
    
    #when user enters 3
    elif(choice==3):
        #getting the author name from user
        author=input("Enter Name of Author: ")
        #calling read_book() function to print the details of book by author
        read_book(author)

    #when user enters 4
    elif(choice==4):
        #calling view_book() function to print the details of all book 
        view_book()

    #when user enters 5
    elif(choice==5):
        #exiting the loop if user enters 5
        break
    
    #when user enters any other value
    else:
        #print Invalid Option Selected if user selects any other value
        print("Invalid Option Selected")
        #continue with the next iteration
        continue

