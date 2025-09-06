from tkinter import *

screen = Tk()
screen.title("product using widgets")
screen.geometry('400x300')
lbl = Label(text="Hello!", fg= "white", bg="#075F0E" )

num1_label = Label(text="please enter  2 numbers", fg = "white", bg="#075F0E")
num1_entry = Entry()

num2_entry = Entry()

def multiplication():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    product = int(num1) * int(num2)
    global result
    result = f"the product is {product} \n"
    text_box.insert(END, result)
text_box = Text(height=3)

btn = Button(text="get result", command= multiplication, height = 1, bg ="#075F0E", fg = "white"  )
lbl.pack()
num1_label.pack()
btn.pack()
num1_entry.pack()
num2_entry.pack()
text_box.pack()
screen.mainloop()