import json
import tkinter as tk
import Alien_classes


root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=680)
canvas.grid(columnspan=3)

instruction = tk.Label(root, text="Press the button to get a cool alien name!", font="Raleway")
instruction.grid(columnspan=3,column=0,row=0)



root.mainloop()

