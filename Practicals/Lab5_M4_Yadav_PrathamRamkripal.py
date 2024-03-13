# Author: Pratham Ramkripal Yadav   
# Assignment: 5
# Date: 20 September 2023
# Class: 

import random
import math

#Question 1: create a list of random numbers between 0 and 10 of length n, use random.random()
def create_random_list(n):
    #declaring a list l
    l = []
    #running a for loop upto n iterations 
    for i in range(n):
        #generating a random number 
        l.append(round(random.random()*10))
    #returning the final list
    return l

#Question 2: take a list l and iterate through it. Return a list where every corresponding number of l is the floor of it
def iterate_floor(l):
    #declaring a new list l1 to store the floor values
    l1=[]
    #iterating throught each value in the list l and storing the floored value into list l1
    for i in l:
        l1.append(math.floor(i))
    #returning list l1
    return l1

#Question 3: create a dictionary using two lists: authors and books.
def create_dictionary(authors,books):
    #declaring the dictionary
    dictionary = {}
    #finding the length of dictionary
    length=len(authors)

    #running a for loop for length of authors list to add all the key value pairs to dictionary
    for i in range(length):
        dictionary[authors[i]]=books[i]
    
    #returning the dictionary
    return dictionary

#Question 4: search the dictionary using a string, return index
def find_index(book, dictionary):
    #iterating through the dictionary 
    for i in dictionary:
        #if the value for the key matches the value that user is searching for return the key
        if(dictionary[i]==book):
            return i



#initializing the list and dictionaries to be used in function call
authors = ['stephen hawking', 'daniel kahneman', 'donald knuth', 'andrew tanenbaum']
books = ['a brief history in time', 'thinking, fast and slow', 'the art of computer programming', 'computer networks']
book = 'the art of computer programming'
dictionary={'stephen hawking': 'a brief history in time', 'daniel kahneman': 'thinking, fast and slow', 'donald knuth': 'the art of computer programming', 'andrew tanenbaum': 'computer networks'}

#call each function and print output

#calling create_random_list function 
print(create_random_list(4))

#calling iterate_floor function
print(iterate_floor([2.4,8.9]))

#calling create_dictionary function
print(create_dictionary(authors,books))

#calling find_index function
print(find_index(book,dictionary))

