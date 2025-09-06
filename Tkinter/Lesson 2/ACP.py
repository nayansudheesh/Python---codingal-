#ACP , "Age Calculator App"
from tkinter import *
from datetime import *

window = Tk()

window.title("age calculator app")
window.geometry("400x400")
GREY = "#3A3A3A"

birthyear_lbl = Label(master=window, text="enter your birthyear", fg="white", bg="#000000")
birthyear_entry = Entry()

birthmonth_lbl = Label(master=window, text="enter your birthmonth", fg="white", bg="#000000")
birthmonth_entry = Entry()

birthday_lbl = Label(master=window, text="enter your birthday", fg="white", bg="#000000")
birthday_entry = Entry()

def age_calculator():
    birthyear = int(birthyear_entry.get())
    birthmonth =int(birthmonth_entry.get())
    birthday = int(birthday_entry.get())
    today = datetime.today()
    month = today.month
    year = today.year
    age_years = year - birthyear
    age_months = month - birthmonth
    age_days = today.day - birthday
    if age_days < 0:
        age_days = age_days * -1
    global age
    age = f" {age_years} years, {age_months} months, {age_days} days"
    result_lbl = Label(master=window, text=f"the result is{age}", fg="white", bg="#000000")
    result_lbl.pack()
btn = Button(master=window, text="click to get result", command=age_calculator, fg="white", bg="black")

birthyear_lbl.pack()
birthyear_entry.pack()
birthmonth_lbl.pack()
birthmonth_entry.pack()
birthday_lbl.pack()
birthday_entry.pack()
btn.pack()

window.mainloop()

    