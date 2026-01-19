from tkinter import *
from tkinter import ttk
import random
import time

symbols = ["7","🍒","🍊","🍉","🍇"]

scoreDict = {("7","7","7"):10,
    ("🍒","🍒","🍒"):5,
    ("🍊","🍊","🍊"):4,
    ("🍉","🍉","🍉"):3,
    ("🍇","🍇","🍇"):2}

class slot:
    def __init__(self,starting_balance ,bet = 10):
        self.balance = starting_balance
        self.cooldown = False
        self.bet = bet

    def spin(self):
        if not self.cooldown and self.balance>=self.bet:
            self.cooldown = True
            spinButton.config(state="disabled")
            self.balance -= self.bet
            result = []
            for _ in range(3):
                result.append(random.choice(symbols))
            self.animation()
            output1.config(text=result[0])
            output2.config(text=result[1])
            output3.config(text=result[2]) 
            result = tuple(result)
            if result in scoreDict:
                self.balance += scoreDict[result]*self.bet
            score.config(text=f"Balance: {slot.balance}")
            time.sleep(0.1)
            spinButton.config(state="normal")
            self.cooldown = False
    def animation(self,i=0):
        if i < 4:
            output1.config(text=random.choice(symbols))
            output2.config(text=random.choice(symbols))
            output3.config(text=random.choice(symbols))
            root.after(100, self.animation, i + 1)
    def increase_bet(self):
        if self.bet < 100:
            self.bet += 10
            bet.config(text=f"Bet:{self.bet}")

    def decrease_bet(self):
        if self.bet > 10:
            self.bet -= 10
            bet.config(text=f"Bet:{self.bet}")

slot = slot(1000)
root = Tk()

root.title("Slot Machine")
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid()

score = ttk.Label(frm,text= f"Balance: {slot.balance}",font=("Arial", 30, "bold"),width=15, anchor='center')
score.grid(column=1, row=0)


output1 = ttk.Label(frm,text= "7",font=("Arial", 30, "bold"), width=3, anchor='center')
output1.grid(column=0, row=1)

output2 = ttk.Label(frm, text="7",font=("Arial", 30, "bold"), width=3, anchor='center')
output2.grid(column=1, row=1)

output3 = ttk.Label(frm, text="7",font=("Arial", 30, "bold"), width=3, anchor='center')
output3.grid(column=2, row=1)

bet = ttk.Label(frm, text=f"Bet:{slot.bet}",font=("Arial", 30, "bold"), width=7, anchor='center')
bet.grid(column=1, row=3)

spinButton = ttk.Button(frm, text="SPIN",command=slot.spin)
spinButton.grid(column=1, row=2)

raiseBetButton = ttk.Button(frm, text="Raise Bet",command=slot.increase_bet)
raiseBetButton.grid(column=2, row=3)

lowerBetButton = ttk.Button(frm, text="Lower Bet",command=slot.decrease_bet)
lowerBetButton.grid(column=0, row=3)


root.mainloop()