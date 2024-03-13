#Author: Pratham Ramkripal Yadav    
#Assignment: Lab 7
#Class: Advance Data Structures
#Date: 02 October 2023

'''
Description: The Program uses list to implement stack operations and 
queue operations and for graph operations the program makes use of dictionary
'''

#Notes: Difference between stack and queue:
# stack follows LIFO (last element added is first removed)
# queue follows FIFO (first element added is first removed)

#Q1: Implement Stack with functions: .append, .pop. You can use python list, collections.deque, and queue.LifoQueu
import random

#Declaring Stack Class
class stack:
    #Initializing the Stack
    def __init__(self):
        self.x=[]
    
    #defining a function to enter an element to stack
    def append(self):
        self.x.append(random.randint(0,9))
        return
    
    #defining a function to remove an element from the stack (elements are always removed from the end of the stack)
    def pop(self):
        self.x.pop(-1)
        return
    
#Q2: Implement Queue with functions .enqueue and .dequeue. 
#    Enqueue adds element to the back while dequeue removes the first element

#Declaring Queue Class
class queue:
    #defining a function to initialize the queue
    def __init__(self):
        self.x=[]
    
    #defining a function to add new element to queue (elements are always added to the end of the queue)
    def enqueue(self):
        self.x.append(random.randint(0,9))
        return
    
    #defining a function to remove element from the queue (elements are always removed from the start of the queue)
    def dequeue(self):
        self.x.pop(0)
        return

#Q3: Implement Graph with functions add_node, add_edge, and print graph. 
#    Print graph show for each node, every other node that shares an edge

#Defining Graph Class
class Graph:
    #defining a function to initialize a graph 
    def __init__(self):
        self.graph={}
    
    #defining a function to add a new node to the graph
    def add_node(self, node):
        self.graph[node]=[]

    #defining a function to add a new edge to the graph
    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    #defining a function to print a graph
    def print_graph(self):
        print(self.graph)

#---------------Stack Object Creation-------------------#
print("\n------Stack Operations------")
#creating an object for stack class
a=stack()
#printing status of stack after initialization
print("Initialization ")
print(a.x)


print("Push Operation")
#calling the push operation
a.append()
a.append()
#printing the status of stack after push operation
print(a.x)
print("Pop Operation")
#calling the pop operation
a.pop()
#printing the status of stack after pop operation
print(a.x)


#---------------Queue Object Creation-------------------#
print("\n------Queue Operations------")
#creating an object for queue class
b=queue()
print("Initialization ")
#printing the object after initialization
print(b.x)

#calling the enqueue function 
b.enqueue()
b.enqueue()
#printing the queue status after the enqueue operation
print("After Enqueue Operation")
print(b.x)

#calling the dequeue function 
b.dequeue()
#printing the queue status after the dequeue operation
print("After Dequeue Operation")
print(b.x)


#---------------Graph Object Creation-------------------#
print("\n------Graph Operations------")
#creating object for graph class
g=Graph()
#printing the status of graph after initialization
print("After Initializing")
print(g.print_graph())

#calling add_node() function to add new nodes to the graph initialized
g.add_node('A')
g.add_node('B')
g.add_node('C')
#printing the status of the graph after adding new nodes
print("After Adding Nodes")
print(g.print_graph())

#calling add_edge() to add new edges to the graph initialized
g.add_edge('A','B')
g.add_edge('A','C')
#printing the status of the graph after adding new edges
print("After Adding Edges")
print(g.print_graph())


