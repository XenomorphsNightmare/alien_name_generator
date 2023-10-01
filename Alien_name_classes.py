import json
from PIL import Image, ImageTk
import tkinter as tk
import Alien_classes

def load_json(filename):
    f = open(filename)
    data_dict = json.load()


root = tk.Tk()
# Image
logo = Image.open("./pictures/Alien.png")
logo = logo.resize((100,100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row = 0)


canvas = tk.Canvas(root, width=800, height=680)
canvas.grid(columnspan=3)

instruction = tk.Label(root, text="Press the button to get a cool alien name!", font="Raleway")
instruction.grid(columnspan=3,column=0,row=1)

button_string = tk.StringVar()
browse_button = tk.Button(root, textvariable=button_string,)
button_string.set("Open input file")
root.mainloop()

