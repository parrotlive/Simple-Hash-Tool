import os
from turtle import back
os.makedirs('logs', exist_ok=True)
import hashcalc
import tkinter

def runprogram(mode):
    window.destroy()
    mode()

window = tkinter.Tk()
window.title("Hash Calculator")
selecttext = tkinter.Label(window, text="Select Operation:")
selecttext.pack()
hashcalcop = tkinter.Button(window, text="Run Hash Calculator", command=lambda: runprogram(hashcalc.hashcalc))
hashcalcop.pack()
tkinter.mainloop()
