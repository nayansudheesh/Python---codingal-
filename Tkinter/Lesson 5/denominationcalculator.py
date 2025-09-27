from tkinter import *

screen = Tk()
screen.title("main window")
screen.geometry("400x400")

def topscreen():
    top = Toplevel()
    top.geometry("200x200")
    top.title("this is top window")
    l2 = Label(top, text="this is a top window")
    l2.pack()
     
    top.mainloop()
l1 = Label(screen,text="this is root window")
btn = Button(screen, text="click to see top window", command=topscreen)

l1.pack()
btn.pack()

screen.mainloop()