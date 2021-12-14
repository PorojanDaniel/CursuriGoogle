from tkinter import *
from tkinter.ttk import *

from time import *

window = Tk()
window.title("clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(window, font=("ds-digital", 80), background = 'black', foreground='#eee')
label.pack(anchor='center')

time()
mainloop()