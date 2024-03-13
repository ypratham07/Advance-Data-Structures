#Author: Pratham Ramkripal Yadav    
#Assignment: Lab 12
#Class: Advance Data Structures
#Date: 20 November 2023

#Importing the necessary libraries
import tkinter as tk
from PIL import Image, ImageTk 
import os 

#Creating a list of images to be displayed
images=["1.jpeg","2.jpeg","3.jpeg","4.jpeg","5.jpeg"]

#creating a global variable to keep track of current_image_index
current_image_index = 0 

def next_window():
    def load_image(image_file):
        #opening the image
        image=Image.open(image_file)
        
        #getting the width and height of original image
        width,height=image.size
        
        #resizing the image according to canvas
        ratio = min(300/width, 200/height)
        image = image.resize((int(width*ratio), int(height*ratio)))
        photo = ImageTk.PhotoImage(image)

        #returning the reference to image object
        return photo

    def update_image():
        # use the global variable
        global current_image_index
        
        # load the image from the image list
        photo = load_image(images[current_image_index])
        
        # delete the previous image from the canvas
        canvas.delete("all")
       
        # create a new image on the canvas
        canvas.create_image(150, 100, image=photo)
        
        # keep a reference to the photo object
        canvas.image = photo        
        
    
    image_window=tk.Toplevel(my_window)

    image_window.title("Image Window")

    canvas = tk.Canvas(image_window, width=300, height=200)
    canvas.create_text(150, 100, text="Welcome To Image Window")
    canvas.pack()

    #creating next button to view next image
    next_button=tk.Button(image_window,text="Next Image", command= lambda : next_image() )
    next_button.pack()
    
    #creating previous button to view previous image
    previous_button=tk.Button(image_window,text="Previous Image", command=lambda : previous_image() )
    previous_button.pack()
    
    #creating done buttonto return to initial window
    done_button=tk.Button(image_window, text= "Done", command= lambda : done() )
    done_button.pack()

    #calling the update_image() function to display the first image
    update_image()    
   
    # define a function to display the next image
    def next_image():
        # use the global variable
        global current_image_index 
        # increment the current index by one
        
        current_image_index = (current_image_index + 1) % len(images)
        
        # update the canvas with the next image
        update_image()

    # define a function to display the previous image
    def previous_image():
        global current_image_index # use the global variable
        
        # decrement the current index by one
        current_image_index = (current_image_index - 1) % len(images)
        
        # update the canvas with the previous image
        update_image()

    # define a function to close the new window and return to the main window
    def done():
        # destroy the new window
        image_window.destroy()

#creating initial Krame
my_window= tk.Tk()

#creating canvas for the first i.e. initial frame
canvas = tk.Canvas(my_window, width=300, height=200)
canvas.create_text(150, 100, text="Welcome")
canvas.pack()

#Creating next button
button = tk.Button(my_window, text="Next", command=next_window)
button.pack()   


my_window.mainloop()
