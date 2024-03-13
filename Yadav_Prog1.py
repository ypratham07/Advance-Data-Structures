#Author: Pratham Ramkripal Yadav
#Date of Creation: 22 August 2023

'''
Description: The program takes the name of the user, once the name is entered the user is gretted with hello user_name message then the user is asked to select the 
system of measurements in which he wants to enter the value of height and weight there are two functions metric_calculation() and imperial_measures() 
which calculate the bmi depending on the measurement type. 
'''
def metric_calculation():
	#Getting weight from user
	print("Please enter your weight in kilograms : ",end=""),
	weight=float(input()) 

	#Getting height from user
	print("Please enter your height in meters : ",end=""),
	height=float(input()) 

	#Applying the formula for BMI and rounding the answer upto two decimal places 
	bmi=round(weight/(height*height),2) 

	return bmi

def imperial_measures():
	#Getting weight from user
	print("Please enter your weight in lbs : ",end=""),
	weight=float(input()) 
	
	#Getting height from user
	print("Please enter your height in inches : ",end=""),
	height=float(input()) 

	#Applying the formula for BMI and rounding the answer upto two decimal places
	bmi=round(weight/(height*height)*703,2)  

	return bmi

#Getting user name
print("Enter Your Name : ",end="") 
user_name=input()	  

#Greeting the user with his name
print("Hello ",user_name) 

#Selecting the System of measurements
#User is asked to select the system of measurements 1 for Metric System and 2 for Imperial Measures System
print("\n Enter 1 for Metric System \n Enter 2 for Imperial Measures System \n Select Your System:",end="")  
calculation_system=int(input())

#declaring the bmi variable
bmi=0

#Depending upon the measurement system selected by the user the functions are called accordingly
if(calculation_system==1): 
	bmi=metric_calculation()
elif(calculation_system==2):
	bmi=imperial_measures()
else:
	print("Select a valid system")

#Displaying the value of BMI to user 
print("Your BMI is ",bmi)



