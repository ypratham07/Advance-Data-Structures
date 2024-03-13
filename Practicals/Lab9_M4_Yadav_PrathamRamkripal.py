# Name: Pratham Ramkripal Yadav 
# Date: 01 November 2023
# Class: CPS 501
# Assignment: Lab 9

#importing regular expression module
import re
#imporint wrap function from functools module
from functools import wraps
#importing time module
import time

# Today we will be working on decorators, regular expressions. 
# For each I will provide you an example on how each works and what I am looking for.
# Decorators allow you to pass a function through a wrapper that can access 
# the functions arguments and run code as well as the function passed into it
# example:
    
#defining a decorator 
def example_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #using time function to get the system time
        start=time.time()
        #printing the start time
        print("Start: ",start)
        #calling the main function
        func(*args, **kwargs)
        #storing the end time into end variable
        end=time.time()
        #printing the end time
        print("Finish: ",end)
        #printing the time taken by the function to execute
        print("Time Taken:",end-start)

    return wrapper
            
#Attaching a decorator with function       
@example_decorator
def printHelloWorld(number):
    for i in range(number):
        print("Hello World")

#calling printHelloWorld function    
printHelloWorld(2)

# Q1: Write a decorator that measures and prints the time taken by a function to execute.
# and then define another function, decorate it with the decorator and run it.
# Don't forget to use @wraps(func) as in the example above

# A regular expression is a sequence of characters that defines a search pattern
# https://docs.python.org/3/library/re.html
# For the next two questions, the link above contains all information to answer them correctly.

# Regular expression example:
    
# text = "apple;banana,orange:grape"
# pattern = r'[;,:]'
# result = re.split(pattern, text)
# print(result)

# # vs. :
    
# text = "apple;banana,orange:grape"
# pattern = r'[;,]'
# result = re.split(pattern, text)
# print(result) 

# Q2: define the pattern to search the string for the word python
#defining the string
text = "Python is fun, isn't Python?"

#defining the pattern to find the word Python in the string
pattern = r'\bPython\b'

#iterating through the string
for match in re.finditer(pattern, text):
    start, end = match.span()
    print(f"Found '{pattern}' at index: {start}-{end}")
# Found 'Python' at index: 0-6
# Found 'Python' at index: 21-27

# Q3: Return list of all words in the sentence, no punctuation

#defining the string
text = "Hello, world! How is your day?"

#defining the pattern to find each word without punctiuation
pattern = r'\b\w+\b'

#using the findall function to locate the pattern in the string passed to it
tokens = re.findall(pattern, text)

#Printing the tokens
print(tokens)

# Output: ['Hello', 'world', 'How', 'is', 'your', 'day']








