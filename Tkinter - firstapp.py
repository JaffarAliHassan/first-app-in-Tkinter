from tkinter import *
import time

root = Tk()
root.geometry('300x200')
root.title("Tkinter - firstapp")

title = Label(root, text="Time", bg="#111", fg="#eee", width=40, font=(20))
title.pack()

def TimeNow():
    time1 = time.strftime("%r")
    timelb.config(text=time1)

timelb = Label(root, text="", font=(60), fg="#9E0000")
timelb.pack(pady=10)

btn = Button(root, text="Time Now", bg="#00FFB3", fg="#000", font=(15), width=25, border=0, command=TimeNow)
btn.pack(pady=40)

mainloop()