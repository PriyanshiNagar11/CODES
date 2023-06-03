from tkinter import *

from time import strftime

root = Tk()
root.title("Clock")
root.geometry("400x150+550+300")

def time():
    string= strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root,font=("arial",50,"bold"),background="black", foreground="cyan")
label.pack(anchor='center')
time()


mainloop()