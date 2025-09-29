from tkinter import *

screen = Tk()
screen.geometry("600x600")
screen.title("Password strength checker")
lbl1 = Label(screen, text = "enter your password", fg="black")
passwordentry = Entry(screen)
def password_strength_checker():
    password = passwordentry.get()
    password_length = len(password)
    if password_length <= 5:
        strength = "weak"
        color = "red"
    elif password_length >= 6 and  password_length < 8:
        strength = "medium"
        color = "orange" # yellow not used as it is not visible on white bg
    elif password_length >= 8 and password_length <= 12:
        strength = "strong"
        color = "light green"
    else:
        strength = "very strong"
        color = "dark green"
    strength_lbl = Label(screen, text = f"the strength is {strength}", fg= color)
    strength_lbl.pack()
btn = Button(screen , text="click to check the strength of your password", command=password_strength_checker, fg="black")
lbl1.pack()
passwordentry.pack()
btn.pack()

screen.mainloop()