from tkinter import *
from tkinter import ttk
import random
import time

symbols = ["7","🍒","🍊","🍉","🍇"]

scoreDict = {("7","7","7"):1000,
    ("🍒","🍒","🍒"):750,
    ("🍊","🍊","🍊"):500,
    ("🍉","🍉","🍉"):250,
    ("🍇","🍇","🍇"):100}

class slot:
    def __init__(self,starting_balance):
        self.balance = starting_balance
        self.cooldown = False

    def Spin(self):
        if not self.cooldown:
            self.cooldown = True
            spinButton.config(state="disabled")
            self.balance = self.balance - 50
            result = []
            for _ in range(3):
                result.append(random.choice(symbols))
            output1.config(text=result[0])
            output2.config(text=result[1])
            output3.config(text=result[2])
            result = tuple(result)
            if result in scoreDict:
                self.balance += scoreDict[result]
            score.config(text=f"Balance: {slot.balance}")
            time.sleep(0.1)
            spinButton.config(state="normal")
            self.cooldown = False

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

spinButton = ttk.Button(frm, text="SPIN",command=slot.Spin)
spinButton.grid(column=1, row=2)

root.mainloop()