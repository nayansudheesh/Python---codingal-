# 1 inch = 2.54 cm
from tkinter import *
from tkinter import messagebox

screen = Tk()

screen.title("ACP, lesson 3")
screen.geometry("500x500")

lbl = Label(text="app to convert inches to cm", fg="white", bg="black")
inch_entry = Entry()
def conversion():
    global inch
    inch = int(inch_entry.get())
    global cm
    cm = int(inch) * 2.54
    global result
    result = Label(text=f"{inch} inches are {cm} centimeters`s")
    result.pack()

btn = Button(master=screen, text="Click me to convert", fg="white", bg="black", command=conversion)

lbl.pack()
inch_entry.pack()
btn.pack()

screen.mainloop()