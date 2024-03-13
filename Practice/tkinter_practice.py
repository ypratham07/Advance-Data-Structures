import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry("600x400")

def GenderSelect():
    GenderSelected.set(1)


GenderSelected=IntVar()
MaleGender=IntVar()
FemaleGender=IntVar()

Checkbutton(window,text="Male",variable=MaleGender,command=lambda: GenderSelect()).pack()
Checkbutton(window,text="Female",variable=FemaleGender,command=lambda: GenderSelect()).pack()
window.wait_variable(GenderSelected)
print("MaleGender: ",MaleGender.get(),"\n","FemaleGender: ",FemaleGender.get())

window.mainloop()
