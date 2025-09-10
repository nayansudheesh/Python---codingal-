from tkinter import *

screen = Tk()

screen.title("event handler")
screen.geometry('400x400')

def handle_keypress():
    """ print the character associated to the key pressed"""
    print(Event.char)

screen.bind("<Key>", handle_keypress)

def handle_click():
    print("\n the button was clicked!")
btn = Button(text="click me", fg="white", bg="black")
btn.pack()

btn.bind("<Button-1>", handle_click)

screen.mainloop()
