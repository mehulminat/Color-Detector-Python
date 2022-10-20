from tkinter import *
from tkinter import filedialog
import time
import cv2
import os
import sys

import tkinter as Tk
pathhhhhh=os.path.dirname(__file__)+"\\main.py"
def orangeopen():
    cmm="python "+pathhhhhh+" "+"10 150 10 20 255 255"   # adhaa commm
    os.system(cmm)
def greenopen():
    cmm="python "+pathhhhhh+" "+'40 150 0 140 255 255'   # adhaa commm
    os.system(cmm)
def redopen():
    cmm="python "+pathhhhhh+" "+'160 109 20 179 255 255'   # adhaa commm
    os.system(cmm)
def blueopen():
    cmm="python "+pathhhhhh+" "+'40 150 0 140 255 255'   # adhaa commm
    os.system(cmm)

    
root = Tk.Tk()
root.wm_geometry("350x160")
root.wm_title(" 20DCS049 | Python Mini Project")
frame1 = Tk.Frame(root, width=400, height=350)
frame1.pack()
orange = Tk.Button(master=frame1, text='orange', width=10, command=orangeopen)
orange.pack(side=Tk.LEFT, padx=2, pady=2)
blue = Tk.Button(master=frame1, text='blue', width=10, command=blueopen)
blue.pack(side=Tk.LEFT, padx=2, pady=10)
green = Tk.Button(master=frame1, text='green', width=10, command=greenopen)
green.pack(side=Tk.LEFT, padx=2, pady=20)
red = Tk.Button(master=frame1, text='red', width=10, command=redopen)
red.pack(side=Tk.LEFT, padx=2, pady=30)
# livelabel = Tk.Label(master=frame1, text='Press q to capture the video snap', width=100)
# livelabel.place(relx = 0.5,
                #    rely = 0.5,
                #    anchor = 'center')
# livelabel.pack(side=Tk.BOTTOM, padx=2, pady=15)
Label(root, text='Press esc to exit video window', bg="white", fg="black").place(x=20,y=80)
Tk.mainloop()