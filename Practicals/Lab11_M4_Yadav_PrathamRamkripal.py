#Name:       Pratham Ramkripal Yadav  
#Date:       15 November 2023
#Assignment: Lab 11
#Class:      CPS 596

#Importing the necessary library
import tkinter as tk
from tkinter import filedialog

#defining class to define application
class TextFileWriterApp:
    def __init__(self, master):

        #defining the title of file
        self.master = master
        self.master.title("Text File Writer")

        #initializing the file path 
        self.file_path = None

        # Entry box to enter text
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        # Open button that performs the open file operation
        self.open_button = tk.Button(master, text="Open", command=self.open_file)
        self.open_button.pack(pady=5)

        # Write button that performs the write operation 
        self.write_button = tk.Button(master, text="Write", command=self.write_to_file)
        self.write_button.pack(pady=10)

    #defining the function to open the file 
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        #When file path is not none then open the file present at the path
        if file_path:
            self.file_path = file_path
            print(f"File opened: {file_path}")

    #defining the function to perform write operation to the file 
    def write_to_file(self):
        
        #if file path is not present  
        if not self.file_path:
            print("Please open a file first.")
            return

        #getting data from user to write
        text_to_write = self.entry.get()

        #if text is given by the user
        if text_to_write:

            #write text to file
            with open(self.file_path, "a") as file:
                file.write(text_to_write + "\n")
                print(f"Text written to file: {text_to_write}")

#defining the main function
if __name__ == "__main__":
    #creating the window
    root = tk.Tk()
    #calling the class method
    app = TextFileWriterApp(root)

    root.mainloop()
