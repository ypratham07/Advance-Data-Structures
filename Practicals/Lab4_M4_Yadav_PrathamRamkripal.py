#Author : Pratham Ramkripal Yadav
#Creation Date: 13 September 2023
'''
Question 1: Given a string s, find the length of the longest substring without repeating characters.
'''
'''
Description : The program starts with two pointers left and right left is set to index 0 and right is left+1 
and the program iterates throught each element of the string until it finds an another element which it has 
already traversed or it reaches the end of string lengths of all such string is strored in a list and 
maximum of all theses stored lengths is printed
'''

#defining substring_length() function
def substring_length(a,l):    
    r=l+1        #initializing right pointer 
    list1=[a[l]] #list1 stores the number of characters that we have passed througth in past

    #run the loop until you come across another character that we have already came across or we come to end of the string
    while(a[r] not in list1 and r<len(a)):
        #push the new character to list1 
        list1.append(a[r])
        #increment the right pointer
        r=r+1       

    return len(list1)

#initializing variable a that stores a string
a="abcabcbb"
#created a list l to store the length of substrings
l=[]    

for i in range(len(a)-1):
    
    #calling the Substring_length() function to calculate the length of substring starting with i
    l.append(substring_length(a,i))    

#printing the maximum of length of substrings
print("Length Of Longest Substring =",max(l))


#Author : Pratham Ramkripal Yadav
#Creation Date: 13 September 2023
'''
Question 2: Given a list of numbers, find the number that repeats the most.
'''
'''
Description: The program uses a dictionary to keep track of number of unique elements in the list and traverses through the given list of numbers 
the program then calculates the maximum of all the values and prints the keys corresponding to the maximum value
'''
#initializing a list of numbers
a=[1,2,3,1,2,1,1,1]
#defining a dictionary
c={}

#runing a for loop to traverse through every element of the list and increment the value of corresponding key in the dictionary  
for i in a:
    #if the key is not present dictionary keys, then the key is initialized with value 0 
    if(i not in c.keys()):
        c[i]=0
    #increment the value of key in dictionary 
    c[i]=c[i]+1

#iterating through each element of dictionary     
for key,value in c.items():
    #if the variable value matches the maximum from values in dictionary printing the corresponding key
    if(max(c.values())==value):
        print("Most Repeating Number =",key)
