# Author: Pratham Ramkripal Yadav
# Assignment: Lab 6
# Date: 27 September 2023
# Class: Advance Data Structures
'''
Description: The following Python Script contains multiple functions to work with matrix , stacks and list
'''


import random
    
#Q1: Define a matrix of size m and n using lists inside of list and initialize it
#    with random numbers. m = rows, n = columns
def create_matrix(m,n):
    a=[]
    for i in range(m):
        a.append([])
        for j in range(n):
            a[i].append(random.randint(0, 9))	
    return a

#Q2: Sets - given a list of items see if there are any duplicates. Only use lists and comparisons.
#    Return a bool
def is_a_set(list1):
    #creating a new list to store the traversed items
    comparision_list=[]

    #traversing each element in the list
    for i in list1:
        #if current element is already traversed 
        if(i in comparision_list):
            #return 0 indicating that the given list is not a set
            return 0
        #if current element is not already traversed 
        else:
            #push the current element to the list of traversed elements
            comparision_list.append(i)
    #return 1 indicating that the given list is a set
    return 1

#Q3: Return a list of n random numbers
def return_list(n):
    #declaring a new list
    a=[]
    #starting a for loop to insert n elements in list a
    for i in range(n):
        a.append(random.randint(0, 9))
    #return the list of n randomly generated numbers
    return a

#Q4 Traverse the list one by one and find the minimum number
def return_minimum(list1):
    #initialing a new vairable minimum with first element of list
    minimum=list1[0]

    #traversing each element in list 
    for i in list1:
        #if current element is less than minimum 
        if(minimum>i):
            #set minimum value as current value
            minimum=i
    #return the value stored in minimum variable
    return minimum

#Q4: Design a stack that supports push, pop. Then intialize it and fill it with 10 random numbers.
#    Then delete the last three elements and print the stack
#    This means creating a class with the methods: push, pop

#creating a new class named stack
class stack:
    #initialing a stack 
    def __init__(self):
        self.stack = []

    #declaring a new function to perform push operation in stack
    def push(self):
        #pushing a new item towards the end of stack 
        self.stack.append(random.randint(0, 9))
        return self.stack
    
    #declaring a new function to perform pop operation in stack
    def pop(self):
        #storing the last element of stack
        b = self.stack[-1]
        #ower writing the stack from first element to second last element
        self.stack = self.stack[0:-1]
        #returning the poped element
        return b

#calling the create_matrix() function
matrix=create_matrix(3,3)
#printing the randomly generated matrix
print("Generated Random Matrix")
for i in matrix:
    for j in i:
        print(j,end="\t")
    print("\n")

#calling the return_list() function
list_a=return_list(3)
#printing the newly generated random list
print("Generated Random List : ",list_a)

#calling the return_minimum() function and printing the minimum value
print("Minimum Value: ",return_minimum([5,4,3,2,1]))

#initialing a list
list1=[1,2,2,3]
#calling is_a_set() function with list1 as parameter passed in the function
is_set=is_a_set(list1)

#if is_a_set() returns 1 then it is a set
if(is_set==1):
    print(list1," is a set")

#if is_a_set() returns 0 then it is not a set
elif(is_set==0):
    print(list1," is not a set")

#creating an instance of a class stack as stack1
stack1=stack() 
#calling push() for stack1 
stack1.push()
#printing the stack after push operation
print("Stack After Push Operation :",stack1.stack)

#calling pop() for stack1 
stack1.pop()
#printing the stack after pop operation
print("Stack After Pop Operation :",stack1.stack)