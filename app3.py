from tkinter import *
from tkinter import messagebox
from random import randint


# Screen
root = Tk()
root.geometry("500x300")
root.title("Number Guessing Game")
root.configure(bg="ivory")


# Generate Number Function
def GenerateNumberFunc():
    global Number
    # Generate number
    Number = randint(1, 10)

    # MessageBox to show that a number was generated
    messagebox.showinfo("A number was generated!", "Please Guess the Number")


# Guess Number Function
def GuessNumberFunc():
    global Number
    # Get Value from Answer Entry Box
    UserResponse = AnswerEntry.get()

    # Convert Value from Answer Entry Box to a Number
    UserResponse = int(UserResponse)

    # Check if User Response was higher, lower, or equal to the correct number
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Please Guess Lower", fg='Red')
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Please Guess Higher", fg='Red')
    else:
        ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")


# Title
Title = Label(root, text="Number Guessing Game", font=("Arial",30))
Title.pack()


# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=40)
MainFrame.configure(bg="ivory")


# Guess the Number Label
GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 10:", font=("Arial",20))
GuessNumLabel.pack()


# Answer Entry
AnswerEntry = Entry(MainFrame, font=("Arial",16))
AnswerEntry.pack(pady=10)


# Generate Number Button
GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=16, font=("Arial",16), bg='orange', fg='Dodgerblue', command=GenerateNumberFunc)
GenerateNumberBtn.pack()


# Guess Button
GuessBtn = Button(MainFrame, text="Guess", width=16, font=("Arial",16), bg='orange', fg='#15e650', command=GuessNumberFunc)
GuessBtn.pack(pady=5)


# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()


# Mainloop
root.mainloop()