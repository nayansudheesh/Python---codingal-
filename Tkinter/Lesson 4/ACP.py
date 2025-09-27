from tkinter import *

screen = Tk()
screen.title("intrest calculator")
screen.geometry("800x800")

principal_lbl = Label(text="enter your principal")

principal_entry = Entry()
rate_lbl = Label(text="enter your rate of intrest")
rate_entry = Entry()
time_lbl = Label(text="enter your the time you will pay intrest over")
time_entry = Entry()

def simple_intrest():
    rate = rate_entry.get()
    time = time_entry.get()
    principal = principal_entry.get()
    simple_intrest = (principal*rate*time)/100
    global intrest_lbl
    intrest_lbl = Label(text=f"simple intrest is {simple_intrest}")

def compound_intrest():
    