import json
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import Alien_classes
from random import randint

root = tk.Tk()
#initiation of the classes
alien_builder = Alien_classes.Alien_builder()
director = Alien_classes.Director(alien_builder)
# filedialog 
def load_json():
    filename = askopenfilename(filetypes=[("json file","*.json")] )
    if filename:
        f = open(filename)
        data_dict = json.load(f)
        director.data = data_dict
#alien name generator
def random_shuffle():
    '''Function to get alien name, it generates a random number to address the name list
    args: None
    '''
    first_len = len(director.data['first_name'])
    second_len = len(director.data['second_name'])
    third_len = len(director.data['third_name'])

    first_name = director.data['first_name'][randint(0,first_len-1)]
    second_name = director.data['second_name'][randint(0,second_len-1)]
    third_name = director.data["third_name"][randint(0,third_len-1)]

    alien = director.build_alien(first_name,second_name,third_name)
    alien_name= f'Your alien name is: {alien.first_name} {alien.second_name} {alien.third_name}'

    text_box = tk.Text(root, height=1,width=50,pady=5)
    text_box.insert(1.0, alien_name)
    text_box.grid(column=1,row=2)






# Image
logo = Image.open("./pictures/Alien.png")
logo = logo.resize((100,100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row = 0)


canvas = tk.Canvas(root, width=600, height=480)
canvas.grid(columnspan=3,rowspan=4)

instruction = tk.Label(root, text="Press the button to get a cool alien name!", font="Raleway")
instruction.grid(columnspan=3,column=0,row=1)
#button to open input json
browse_string = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_string, command=lambda:load_json())
browse_string.set("Open input file")
browse_button.grid(column=0, row=3)

#button to make alien name
shuffle_string = tk.StringVar()
shuffle_button = tk.Button(root, textvariable=shuffle_string, command=lambda:random_shuffle())
shuffle_string.set("Get alien name!")
shuffle_button.grid(column=2, row=3)

root.mainloop()

