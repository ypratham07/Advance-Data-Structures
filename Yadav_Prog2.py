#Author: Pratham Ramkripal Yadav
#Creation Date: 04 September 2023
'''
Description: 
Step 1: The Program asks user their name and then greets them user with hello
Step 2: The Program asks user to choose the math operation to practice where 1 is for Addition 2 is for Subtraction and 3 is to Exit the program
Step 3: If user enters 1, addition function is called the program generates 2 random number and asks user addition of two number if the user enter correct value then program prints well done else program prints sorry and shows correct answer
Step 4: If user enters 2, subtraction function is called the program generates 2 random number and asks user subtraction of two number if the user enter correct value then program prints well done else program prints sorry and shows correct answer
Step 5: If the user enters 3 as choice then the program prints thankyou and breaks the loop and comes out of while loop
'''

#Importing the necessary library
import random

#Defining the menu function
def menu():
    #displaying the menu 
    print("Select Operation to Practice")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Exit")

#Defining the addition function
def addition():

    #generating two random numbers num1 and num2 between range 0 to 100
    num1=random.randint(0,100)
    num2=random.randint(0,100)

    #calculating the correct answer
    correct_ans=num1+num2

    #asking user to enter the answer
    print("Enter Sum of ",num1,"+",num2," : " ,end="")

    #getting the answer from user
    user_ans=int(input())

    #if the answer calculated by system matches the answer calculated by user the print well done
    if(correct_ans==user_ans):
        print("Well done")
        print("Press enter key to continue")

        #waiting for the user to press enter key (if the user presses enter then the length of char will be 0 that condition is checked in below if statement)
        if(len(input())==0):
            return
        
    #if the answer calculated by system does not match with the answer calculated by user the print sorry ans show the correct answer
    else:
        print("Sorry the correct answer is",correct_ans)
        print("Press enter key to continue")

        #waiting for the user to press enter key (if the user presses enter then the length of char will be 0 that condition is checked in below if statement)    
        if(len(input())==0):
            return

#Defining the subtraction function
def subtraction():

    #generating two random numbers num1 and num2 between range 0 to 100
    num1=random.randint(0,100)
    num2=random.randint(0,100)

    #if num1 is greater than num2 then swap to make sure that the result is always positive
    if(num1<num2):
        num1,num2=num2,num1

    #calculating the correct answer
    correct_ans=num1-num2

    #asking user to enter the answer
    print("Enter Subtraction of ",num1,"-",num2," : " ,end="")
    
    #getting the answer from user
    user_ans=int(input())

    #if the answer calculated by system matches the answer calculated by user the print well done
    if(correct_ans==user_ans):
        print("Well done")
        print("Press enter key to continue")

        #waiting for the user to press enter key (if the user presses enter then the length of char will be 0 that condition is checked in below if statement)
        if(len(input())==0):
            return
        
    #if the answer calculated by system does not match with the answer calculated by user the print sorry ans show the correct answer
    else:
        print("Sorry the correct answer is",correct_ans)
        print("Press enter key to continue")

        #waiting for the user to press enter key (if the user presses enter then the length of char will be 0 that condition is checked in below if statement)
        if(len(input())==0):
            return
                    

#Start of main Function

#getting the name of user
name=input("Enter Name: ")

#greeting the user with Hello message
print("Hello", name )

#start of while loop
while(True):
    #print the menu by calling the menu function
    menu()

    #getting input from the user for which math operation the person wants to practice
    operation_choice=int(input("Enter Your Choice: "))

    #if user inputs 1 then addition function is called
    if(operation_choice ==1):
        #calling the addition function
        addition()
    elif(operation_choice==2): 
        #calling the subtraction function
        subtraction()
    elif(operation_choice==3):
        #printing thank you
        print("Thank you")
    
        #exiting the program
        break