# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:38:17 2018

@author: hp-pc
"""

import tkinter as tk
from time import sleep

# The truncation will make the progressbar more accurate
# Note however that no progressbar is perfect
from math import trunc

# You will need the ttk module for this
from tkinter import ttk

# Just to demonstrate
fileList = range(10)

# How much to increase by with each iteration
# This formula is in proportion to the length of the progressbar
step = trunc(100/len(fileList))

def MAIN():
    """Put your loop in here"""
    for fileName in fileList:
        # The sleeping represents a time consuming process
        # such as reading a file.
        sleep(1)

        # Just to demonstrate
        print(fileName)

        # Update the progressbar
        progress.step(step)
        progress.update()

    root.destroy()

root = tk.Tk()

progress = ttk.Progressbar(root, length=100)
progress.pack()

# Launch the loop once the window is loaded
progress.after(1, MAIN)

root.mainloop()
