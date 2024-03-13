#Author: Pratham Ramkripal Yadav
#Creation Date: 26 September 2023
'''
Description: The program imports module named shapes which is a user defined module which contains six
different functions each for calculating circumference and area of circle, rectangle and square
depending upon the input from the user the user is asked to prompt the dimentions of the geometric shape and 
the circumference and area of geometric shape is displayed 
'''

#importing user defined custom module 
import shapes as s

#defining function to display menu
def menu():
    print("1 : Circle")
    print("2 : Rectangle")
    print("3 : Square")
    print("4 : Exit")

#main funtion

#start of while loop
while True:
    #calling the menu function to display menu
    menu()
    #getting the users choice 
    choice= int(input("Select Shape : "))

    #if user selects 1 then get circle parameters
    if(choice==1):
        #getting radius from user
        radius=int(input("Enter Radius : "))
        #callng the circumfernce_circle() function from user defined shapes module to calculate circumference of circle and printing the returned value
        print("Circle Circumference : ",s.circumfernce_circle(radius))
        #callng the area_circle() function from user defined shapes module to calculate area of circle and printing the returned value
        print("Circle Area : ", s.area_circle(radius))
    
    #if user selects 2 then get rectangle parameters
    elif(choice==2):
        #getting length from user
        length=int(input("Enter Length of Rectangle : "))
        #getting breadth from user
        breadth=int(input("Enter Breadth of Rectangle : "))
        #callng the circumference_rectangle() function from user defined shapes module to calculate circumference of rectangle and printing the returned value
        print("Rectangle Circumference : " , s.circumference_rectangle(length,breadth))
        #callng the area_rectangle() function from user defined shapes module to calculate area of rectangle and printing the returned value
        print("Rectangle Area : ", s.area_rectangle(length,breadth))
    
    #if user selects 3 then get square parameters
    elif(choice==3):
        #getting side dimentions of square from user
        side=int(input("Enter Side of Square : "))
        #callng the circumference_square() function from user defined shapes module to calculate circumference of square and printing the returned value
        print("Square Circumference : ",s.circumference_square(side))
        #callng the circumference_square() function from user defined shapes module to calculate area of square and printing the returned value
        print("Square Area : ",s.area_square(side))

    #if user selects 4 then exit the while loop and end the program
    elif(choice==4):
        break

# end of main function