from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.geometry('500x500')

def msg():
    messagebox.showwarning("Alert","Stop! virus has been found")

btn = Button(screen, text="click to scan for virus", command=msg)
btn.place(x=40, y =80)

screen.mainloop()