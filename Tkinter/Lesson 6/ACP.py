from tkinter import *
import random 

screen = Tk()

screen.geometry("800x800")
screen.title("rock paper scissors application")

lbl1 = Label(screen, text="Welcome to this rock paper scissors application, you will play against a computer ", fg="black")
lbl2 = Label(screen, text="enter your choice (rock paper or scissor) below" , fg="black")
choice_entry = Entry()
lbl1.pack()
lbl2.pack()
choice_entry.pack()
def computer_play():
    top = Toplevel()
    player_choice = choice_entry.get()
    choices = ["rock" , "paper" , "scissor"]
    computer_choice = random.choice(choices)
    if player_choice.lower() == computer_choice:
       lbl3 = Label(top , text=f"you and the computer have both played the same , ({player_choice}) , so it is a draw")
       lbl3.pack()
    elif player_choice.lower() == "rock" and computer_choice == "paper":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {computer_choice} beats {player_choice} so you lose")
       lbl3.pack()
    elif player_choice.lower() == "paper" and computer_choice == "rock":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {computer_choice} beats {player_choice} so you win")
       lbl3.pack()
    elif player_choice.lower() == "scissor" and computer_choice == "paper":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {player_choice} beats {computer_choice} so you win")
       lbl3.pack()
    elif player_choice.lower() == "paper" and computer_choice == "scissor":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {computer_choice} beats {player_choice} so you lose")
       lbl3.pack()
    elif player_choice.lower() == "rock" and computer_choice == "scissor":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {player_choice} beats {computer_choice} so you win")
       lbl3.pack()
    elif player_choice.lower() == "scissor" and computer_choice == "rock":
       lbl3 = Label(top , text=f"you have played {player_choice} , the computer has played {computer_choice} , {computer_choice} beats {player_choice} so you lose")
       lbl3.pack()
    else:
       lbl3 = Label(top , text= "invalid input")
btn1 = Button(screen , text="click me", command=computer_play)
btn1.pack()
screen.mainloop()