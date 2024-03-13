#Author: Pratham Yadav
#Creation Date: 30 August 2023

'''
#Question: define a function 'area_of_circle' that takes in one argument 'radius'. 
radius should be automatically assigned 0 if not passed to the function. 
The function checks to see if radius is < or = to 0. If yes, return 0.
Else, return the area of a circle (pi*r**2)
'''

#defining a function area_of_circle() to calculate area of circle 
def area_of_circle(radius=0):
    
    #defining the pi value
    pi=3.14   

    #Putting condition if radius is less than or equals to 0 then return 0 else return pi*radius**2
    if(radius<=0):
        return 0
    else:
        return pi*(radius**2)


        
#Calling area_of_circle with radius=10
print("Area of Circle:", area_of_circle(10))

#Calling area_of_circle without passing any radius
print("Area of Circle:", area_of_circle())



#Author: Pratham Yadav
#Creation Date: 30 August 2023

'''
#Question: define a function 'calculate_sum_forloop' that takes in the argument 'numbers' (a list) 
and uses a for loop to return the sum of the list of numbers.
'''

#Defining a function calculate_sum_forloop() to calculate sum of elements present in list
def calculate_sum_forloop(numbers):
    #initializing the value of sum to 0
    sum=0

    #starting the for loop to add all the elements of list
    for i in range(0, len(numbers),1):
        sum=sum+numbers[i]

    #returning the sum
    return sum


#printing the sum of the list
print("Sum of List=",calculate_sum_forloop([1,2,3,4,5]))
    





#Author: Pratham Yadav
#Creation Date: 30 August 2023

'''
#Question: define a function 'calculate_sum_whileloop' that takes in the argument 'numbers' (a list) 
and uses a while loop to return the sum of the list of numbers.
'numbers' should be defined as numbers = [1,2,3,4,5]
'''

#defining a function calculate_sum_whileloop() to calculate sum of elements present in list
def calculate_sum_whileloop(numbers):
    #initializing the sum variable to 0
    sum=0
    #initializing the i variable to 0 which will be used as index variable
    i=0

    #starting the while loop from i=0 till the length of the list i.e the last element of the list
    while(i<len(numbers)):
        #adding the elements and storing the sum in sum variable
        sum=sum+numbers[i]
        #incrementing the value of i to i+1 i.e. the next index
        i=i+1

    #returning the sum
    return sum

#printing the sum of elements present in the list 
print("Sum of List=", calculate_sum_whileloop([1,2,3,4,5]))