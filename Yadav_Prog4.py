#Author: Pratham Ramkripal Yadav
#Creation Date: 09 October 2023

'''
Description: The program is written to provide a functionality to user to practice mathematical operations such as addition, subtraction,
multiplication and division along with this the program also provides a functionality to the user to print its report so that 
the user can view his performance. The program makes use of 2D Matrix to store the results of different operations. 
The Program also uses random module to generate two random number for asking question for different operations. 
The program rewards users by selecting a word from the list of positive reinforcers randomly. 
It also motivates the user if the answer is incorrect for the first time by selecting a word from the list of supportive_reinforcers.
The program is written in such a way that the user is provided with a second chance to answer correctly for same question if the 
first attempt is incorrect if the user fails to answer the question incorrectly for the second time then the attempt is counted as 
incorrect attempt.
'''

#Importing the necessary library
import random

#Defining the menu function
def menu():
    #displaying the menu 
    print("Select Operation to Practice")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Present Report")
    print("6: Exit")

#defining the addition function
def addition(num1,num2):
    #declaring a list of positive reinforcers and supportive reinforcers to be displayed in event of correct and incorrect result respectively
    positive_reinforcers=[' Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct']
    supportive_reinforcers=['Try Again', 'OOPS', 'Not Quite', 'Look at it Again', 'Sorry']
    
    #calculating the correct answer
    correct_answer=num1+num2

    #print statement to display the question
    print(num1," + ",num2," = ",end='')
    #taking the answer from the user
    user_answer=int(input())

    #when answer enterd by user matches the correct answer 
    if(correct_answer==user_answer):
        #print one word randomly from the list of positive reinforcers
        print(random.choice(positive_reinforcers))

        #return 1 to main function indicating that the user entered right answer
        return 1
    
    #when the answer entered by the user does not match the correct answer
    elif(correct_answer!=user_answer):
        #print one word from the list of supportive reinforcers 
        print(random.choice(supportive_reinforcers))
        
        #Giving one more chance to user and asking to enter the answer once again
        user_answer=int(input("Try One More Time : "))

        #if the answer entered by the user matches the correct answer in second attempt
        if(correct_answer==user_answer):
            #print one word randomly from the list of positive reinforcers
            print(random.choice(positive_reinforcers))

            #return 1 to main function indicating that the user entered right answer
            return 1
        
        #return 0 to main function indicating that the user entered wrong answer
        return 0
    
#defining the subtraction function
def subtraction(num1,num2):
    #declaring a list of positive reinforcers and supportive reinforcers to be displayed in event of correct and incorrect result respectively
    positive_reinforcers=[' Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct']
    supportive_reinforcers=['Try Again', 'OOPS', 'Not Quite', 'Look at it Again', 'Sorry']
    
    #calculating the correct answer
    correct_answer=num1-num2

    #print statement to display the question
    print(num1," - ",num2," = ",end='')
    #taking the answer from the user
    user_answer=int(input())

    #when answer enterd by user matches the correct answer 
    if(correct_answer==user_answer):
        #print one word from the list of supportive reinforcers 
        print(random.choice(positive_reinforcers))
        
        #return 1 to main function indicating that the user entered right answer
        return 1
    
    #when the answer entered by the user does not match the correct answer
    elif(correct_answer!=user_answer):
        #print one word from the list of supportive reinforcers 
        print(random.choice(supportive_reinforcers))
        
        #Giving one more chance to user and asking to enter the answer once again
        user_answer=int(input("Try One More Time : "))
        
        #if the answer entered by the user matches the correct answer in second attempt
        if(correct_answer==user_answer):
            #print one word randomly from the list of positive reinforcers
            print(random.choice(positive_reinforcers))

            #return 1 to main function indicating that the user entered right answer
            return 1
        
        #return 0 to main function indicating that the user entered wrong answer
        return 0

#defining the multiplication function
def multiplication(num1,num2):
    #declaring a list of positive reinforcers and supportive reinforcers to be displayed in event of correct and incorrect result respectively
    positive_reinforcers=[' Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct']
    supportive_reinforcers=['Try Again', 'OOPS', 'Not Quite', 'Look at it Again', 'Sorry']
    
    #calculating the correct answer
    correct_answer=num1*num2

    #print statement to display the question
    print(num1," * ",num2," = ",end='')

    #taking the answer from the user
    user_answer=int(input())

    #when answer enterd by user matches the correct answer
    if(correct_answer==user_answer):
        #print one word randomly from the list of positive reinforcers
        print(random.choice(positive_reinforcers))
        #return 1 to main function indicating that the user entered right answer
        return 1
    
    #when the answer entered by the user does not match the correct answer
    elif(correct_answer!=user_answer):
        #print one word from the list of supportive reinforcers
        print(random.choice(supportive_reinforcers))
        
        #Giving one more chance to user and asking to enter the answer once again
        user_answer=int(input("Try One More Time : "))

        #if the answer entered by the user matches the correct answer in second attempt
        if(correct_answer==user_answer):
            #print one word randomly from the list of positive reinforcers
            print(random.choice(positive_reinforcers))

            #return 1 to main function indicating that the user entered right answer
            return 1
        
        #return 0 to main function indicating that the user entered wrong answer
        return 0
    
#defining a division function
def division(num1,num2):
    #declaring a list of positive reinforcers and supportive reinforcers to be displayed in event of correct and incorrect result respectively
    positive_reinforcers=[' Excellent', 'Very Good', 'Well Done', 'Awesome', 'Good Job', 'Correct']
    supportive_reinforcers=['Try Again', 'OOPS', 'Not Quite', 'Look at it Again', 'Sorry']
    
    #calculating the correct answer
    correct_answer=round((num1/num2),2)

    #print statement to display the question
    print(num1," / ",num2," = ",end='')
    #taking the answer from the user
    user_answer=float(input())

    #when answer enterd by user matches the correct answer
    if(correct_answer==user_answer):
        #print one word randomly from the list of positive reinforcers
        print(random.choice(positive_reinforcers))
        #return 1 to main function indicating that the user entered right answer
        return 1
    
    #when the answer entered by the user does not match the correct answer
    elif(correct_answer!=user_answer):
        #print one word from the list of supportive reinforcers
        print(random.choice(supportive_reinforcers))
        
        #Giving one more chance to user and asking to enter the answer once again
        user_answer=int(input("Try One More Time : "))

        #if the answer entered by the user matches the correct answer in second attempt
        if(correct_answer==user_answer):
            #print one word randomly from the list of positive reinforcers
            print(random.choice(positive_reinforcers))
            #return 1 to main function indicating that the user entered right answer
            return 1
        
        #return 0 to main function indicating that the user entered wrong answer
        return 0

#defining a function to generate a random number of either single, double or triple digits to be used later for operations
def generate_random_number(digit_length):
    #When user has selected single digit length
    if(digit_length==1):
        #generate and return a random number between 0 to 9  
        return random.randint(0,9)
    
    #When user has selected double digit length
    elif(digit_length==2):
        #generate and return a random number between 10 to 99 
        return random.randint(10,99)
    
    #When user has selected triple digit length
    elif(digit_length==3):
        #generate and return a random number between 100 to 999
        return random.randint(100,999)

#defining present_report() function to print report
def present_report(matrix):
    
    #Indicating the start of report
    print("\n--------Start Of Report--------\n")

    #for every operation performed print the name of operation performed, number of attempts, number of correct answers and number of incorrect answers
    for i in range(len(matrix[0])):
        print("Name Of Operation : ",matrix[0][i])
        print("Number Of Attempts : ",matrix[1][i])
        print("Correct Answers : ",matrix[2][i])
        print("Incorrect Answers : ",matrix[3][i],"\n\n")
    
    #Indicating the end of report
    print("\n--------End Of Report--------\n")
    
    #return 1 to indicate that the present_report() function was called
    return 1

#-------------Start of main Function----------------
#getting the name of user
name=input("Enter Name: ")

#greeting the user with Hello message
print("Hello", name )
#creating a flag variable to keep track if the present_report() function was called or not
print_report_flag=0
#creating a 2d matrix to store name of operations,number of attemtps,correct answers and incorrect answers
matrix=[[],[],[],[]]

#creating a list to store the number of correct and incorrect answers
attempt_track=[]

#start of while loop
while(True):
    
    #print the menu by calling the menu function
    menu()

    #getting input from the user for which math operation the person wants to practice
    operation_choice=int(input("Enter Your Choice: "))

    #When user inputs 1 then addition function is called
    if(operation_choice ==1):
        #clearing the attempt_track list to store the results of addition operation attempts
        attempt_track.clear()

        #asking the user to select if he wants to practice operation on single, double or triple digits
        print("Select Digit Length \n 1 : Single Digit Operation \n 2 : Double Digit Operation \n 3 : Triple Digit Operation")
        #getting the users choice for digit_length i.e., single, double or triple digits
        digit_length=int(input("Enter Your Choice: "))

        #getting input for the number of times user wants to practice this operation and storing it in attempts variable
        attempts=int(input("Enter Number of times you want to practice : "))

        #running the for loop for the number of attempts       
        for i in range(attempts):
            #generate num1,num2 by calling generate_random_number()
            num1=generate_random_number(digit_length)
            num2=generate_random_number(digit_length)

            #calling the addition() function and storing the result
            attempt_track.append(addition(num1,num2))

        #updating the matrix to store the results of the addition operation
        matrix[0].append("Addition")
        matrix[1].append(attempts)
        matrix[2].append(sum(attempt_track))
        matrix[3].append(len(attempt_track)-sum(attempt_track))

    #When user inputs 2 then subtraction function is called
    elif(operation_choice==2):
        #clearing the attempt_track list to store the results of subtraction operation attempts 
        attempt_track.clear()

        #asking the user to select if he wants to practice operation on single, double or triple digits
        print("Select Digit Length \n 1 : Single Digit Operation \n 2 : Double Digit Operation \n 3 : Triple Digit Operation")
        #getting the users choice for digit_length i.e., single, double or triple digits
        digit_length=int(input("Enter Your Choice: "))
        #getting input for the number of times user wants to practice this operation and storing it in attempts variable
        attempts=int(input("Enter Number of times you want to practice : "))

        #running the for loop for the number of attempts       
        for i in range(attempts):
            #generate num1,num2 by calling generate_random_number()
            num1=generate_random_number(digit_length)
            num2=generate_random_number(digit_length)

            #calling the subtraction() function and storing the result
            attempt_track.append(subtraction(num1,num2))
        
        #updating the matrix to store the results of the subtraction operation
        matrix[0].append("Subtraction")
        matrix[1].append(attempts)
        matrix[2].append(sum(attempt_track))
        matrix[3].append(len(attempt_track)-sum(attempt_track))

    #When user inputs 3 then multiplication function is called
    elif(operation_choice==3): 
        #clearing the attempt_track list to store the results of multiplication operation attempts
        attempt_track.clear()

        #asking the user to select if he wants to practice operation on single, double or triple digits
        print("Select Digit Length \n 1 : Single Digit Operation \n 2 : Double Digit Operation \n 3 : Triple Digit Operation")
        #getting the users choice for digit_length i.e., single, double or triple digits
        digit_length=int(input("Enter Your Choice: "))

        #getting input for the number of times user wants to practice this operation and storing it in attempts variable
        attempts=int(input("Enter Number of times you want to practice : "))

        #running the for loop for the number of attempts       
        for i in range(attempts):
            #generate num1,num2 by calling generate_random_number()
            num1=generate_random_number(digit_length)
            num2=generate_random_number(digit_length)

            #calling the multiplication() function and storing the result
            attempt_track.append(multiplication(num1,num2))

        #updating the matrix to store the results of the multiplication operation
        matrix[0].append("Multiplication")
        matrix[1].append(attempts)
        matrix[2].append(sum(attempt_track))
        matrix[3].append(len(attempt_track)-sum(attempt_track))

    #When user inputs 4 then division function is called    
    elif(operation_choice==4): 
        #clearing the attempt_track list to store the results of division operation attempts
        attempt_track.clear()

        #asking the user to select if he wants to practice operation on single, double or triple digits
        print("Select Digit Length \n 1 : Single Digit Operation \n 2 : Double Digit Operation \n 3 : Triple Digit Operation")
        #getting the users choice for digit_length i.e., single, double or triple digits
        digit_length=int(input("Enter Your Choice: "))

        #getting input for the number of times user wants to practice this operation and storing it in attempts variable
        attempts=int(input("Enter Number of times you want to practice : "))

        #running the for loop for the number of attempts     
        for i in range(attempts):
            #generate num1,num2 by calling generate_random_number()
            num1=generate_random_number(digit_length)
            num2=generate_random_number(digit_length)

            #calling the division() function and storing the result
            attempt_track.append(division(num1,num2))
        
        #updating the matrix to store the results of the division operation
        matrix[0].append("Division")
        matrix[1].append(attempts)
        matrix[2].append(sum(attempt_track))
        matrix[3].append(len(attempt_track)-sum(attempt_track))

    #When user inputs 5 then present_report() function is called     
    elif(operation_choice==5):
        #Calling present_report() and updating the print_report_flag to indicate that the report was printed
        print_report_flag=present_report(matrix)

    #When user inputs 6 then exit the program
    elif(operation_choice==6):
        #if report is not yet printed
        if(print_report_flag==0):
            # inform the user that the results will be lost and confirm if user still wishes to exit
            print("No Report was generated , No records will be maintained once you exit the program \n Do you still wish to Exit? \n 1 : Yes \t 2 : No")
            #getting an input from the user for exit confirmation
            final_choice=int(input())

            #if the user sitll wishes to exit 
            if(final_choice==1):
                #print thank you and exit the program 
                print("Thank you")
                break
            #if the user does not wish to exit 
            else:
                #continue with next iteration
                continue
        
        #when the report is already printed 
        else:
            #printing thank you
            print("Thank you")
    
            #exiting the program
            break
