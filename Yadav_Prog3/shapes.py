#defining function to calculate circumference of circle 
def circumfernce_circle(radius):
    #retuning the circumference of circle 
    return 2*(3.142)*radius

#defining function to calculate area of circle 
def area_circle(radius):
    #retuning the area of circle 
    return (3.142)*radius*radius

#defining function to calculate circumference of rectangle 
def circumference_rectangle(length,breadth):
    #caluclating the circumference of rectangle 
    circumference= 2*(length + breadth)
    #returning the circumference of rectangle
    return circumference

#defining function to calculate are of rectangle 
def area_rectangle(length,breadth):
    #calculating the area of rectangle 
    area=length*breadth
    #returning the area of rectangle 
    return area

#defining function to calculate circumference of square 
def circumference_square(side):
    #caluclating the circumference of square 
    circumference = side*4
    #returning the circumference of square
    return circumference

#defining function to calculate area of square 
def area_square(side):
    #caluclating the area of square
    area= side**2
    #returning the area of square
    return area
