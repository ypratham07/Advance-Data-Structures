#Author: Pratham Ramkripal Yadav
#Date of Creation: 13 November 2023

'''
Description: This is a simple program written for game of Rock, Paper and Scissor using the capabilities of Python GUI using tkinter library
The program contains 3 functions to 
1: get_computer_choice to select a random value for computer
2: check_winner to check the winner based on the values selected and defined rules of the game
3: play_game to initiate the game and print the result of the round
'''

#Importing the required modules
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

#defining a function to select a random value from rock, paper and scissor for computer
def get_computer_choice():
    #defining the list of choices
    choices = ['Rock', 'Paper', 'Scissors']

    #selecting a random value from list of availabe choices
    return random.choice(choices)

#defining a function to check the winner of round by comparing the values selected by user and computer
def check_winner(player_choice, computer_choice,user_name):

    #When user and computer select same values, its a tie
    if player_choice == computer_choice:
        return "It's a tie!"

    #When User Selects rock and Computer Selects Scissor then User Wins
    elif (player_choice == 'Rock' and computer_choice == 'Scissors'):
        return user_name + " wins!"
    
    #When User Selects Paper and Computer Selects Rock then User Wins
    elif (player_choice == 'Paper' and computer_choice == 'Rock'):
        return user_name + " wins!"
    
    #When User Selects Scissor and Computer Selects Paper then User Wins
    elif (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return user_name + " wins!"

    #Otherwise Computer Wins 
    else:
        return "Computer wins!"

#defining function to initiate the game 
def play_game(player_choice,user_name):
    #calling get_computer_choice() to get the value for computer
    computer_choice = get_computer_choice()

    #calling the check_winner() function to determine the winner based on the rules defined
    result = check_winner(player_choice, computer_choice,user_name)

    #Printing the result in a MessageBox
    messagebox.showinfo("Result", f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n\n{result}")

#----------------Main Function--------------------------

#Creating a new window
window = tk.Tk()
#Defining the title of window
window.title("Rock, Paper And Scissors Game")


user_name = tk.simpledialog.askstring("User's Name", "Enter Your Name:")

#importing the rock image 
rock_image = tk.PhotoImage(file="image1.gif")  

#importing the paper image 
paper_image = tk.PhotoImage(file="image2.gif")      

#importing the scissor image 
scissors_image = tk.PhotoImage(file="image3.gif")  

#Code to display the rock paper and scissor buttons with the image
rock_button = tk.Button(window, image=rock_image, command=lambda: play_game("Rock",user_name))
paper_button = tk.Button(window, image=paper_image, command=lambda: play_game("Paper",user_name))
scissors_button = tk.Button(window, image=scissors_image, command=lambda: play_game("Scissors",user_name))

# Align buttons to the center horizontally
rock_button.pack(side="left", anchor="center")
paper_button.pack(side="left", anchor="center")
scissors_button.pack(side="left", anchor="center")

# Enter the Tkinter event loop
window.mainloop()


