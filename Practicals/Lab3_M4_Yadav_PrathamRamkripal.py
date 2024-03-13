#Author : Pratham Ramkripal Yadav
#Creation Date: 06 September 2023

'''
Question 1: create a function that takes in a string and uses a for loop to reverse it
The for loop should use a list as a placeholder to store characters from the string as it accesses the string from right to left.
A list can be converted using ''.join(list)

Description : Program converts the string into list of individual characters and 
then passes the list to reverse_list function where the list is appended into 
a new list named reversed_list in reversed manner and returns the new reversed list by joining it to the main function
'''

#defining the reversed_list function
def reverse_list(list1):
    #creating a variable to raverse the original list 
    index=len(list1)-1
    
    #declaring a new list to store the reversed list 
    reversed_list=[]

    #running the for loop to reverse the list 
    for i in range(index,-1,-1):
        reversed_list.append(list1[i])

    #returning the joined list to the main function
    return ''.join(reversed_list)


a=list('PRATHAM')
print(reverse_list(a))


#Author : Pratham Ramkripal Yadav
#Creation Date: 06 September 2023

'''
Question 2: Merge two lists, sorted
Create a function that takes in two lists of letters and iterates through each, appending each letter letter to an empty list in a way that the final list is sorted.


Description: The program merges two list into one and uses the bubble sort logic to sort the merged list
and printing the sorted list
'''

#defining a function to sort the list
def sorted_list(c):
    #writing a logic for bubble sort to sort the list in ascending 
    for i in range(0,len(c)):
        for j in range(i+1,len(c)):
            #writing the logic to swap the characters in ascending order
            if(c[i]>c[j]):
                temp=c[i]
                c[i]=c[j]
                c[j]=temp
    #returning the sorted list
    return c

#Declaring the two lists to sort
a=['P','R','A','T','H','A','M']
b=['Y','A','D','A','V']

#merging the two list into one
c=a+b

#calling the sorted_list funtion and printing the sorted list
print(sorted_list(c))
