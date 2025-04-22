import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

root = tk.Tk()
root.title('Passgen')

texts = tk.StringVar()
textb = tk.StringVar()
textn = tk.StringVar()
textspe = tk.StringVar()
message2 = tk.Label(root, text = "" ,font=("Helvetica", 15))

window_width = 300
window_height = 300

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#set minimum position
root.minsize(300,300)

#widgets
title = tk.Label(root, text = "Passgen",font=("Helvetica", 20))
title.pack()

title = tk.Label(root, text = "Number of small letters",font=("Helvetica", 10))
title.pack()
textboxs = ttk.Entry(root, textvariable=texts)
textboxs.pack()

title = tk.Label(root, text = "Number of big letters",font=("Helvetica", 10))
title.pack()
textboxb = ttk.Entry(root, textvariable=textb)
textboxb.pack()

title = tk.Label(root, text = "Number of numbers",font=("Helvetica", 10))
title.pack()
textboxn = ttk.Entry(root, textvariable=textn)
textboxn.pack()

title = tk.Label(root, text = "Number of special characters",font=("Helvetica", 10))
title.pack()
textboxspe = ttk.Entry(root, textvariable=textspe)
textboxspe.pack()

# exit button
exit_button = ttk.Button(
    root,
    text='Create password',
    command= lambda:one()
)
exit_button.pack()
def one():
    password = []
    if(textboxs.get()!=""):
        smallLettersNum = int(textboxs.get())
    else:
        smallLettersNum = 0
    smallLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while(smallLettersNum>0):
        password.append(smallLetters[random.randint(0,25)])
        smallLettersNum-=1;
        
    if(textboxb.get()!=""):
        bigLettersNum = int(textboxb.get())
    else:
        bigLettersNum = 0
    bigLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while(bigLettersNum>0):
        password.append(bigLetters[random.randint(0,25)])
        bigLettersNum-=1;

    if(textboxn.get()!=""):
        numbersNum = int(textboxn.get())
    else:
        numbersNum = 0
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while(numbersNum>0):
        password.append(numbers[random.randint(0,8)])
        numbersNum-=1;

    if(textboxspe.get()!=""):
        speNum = int(textboxspe.get())
    else:
        speNum = 0
    special = ['!','#','$','%','&','(',')','*','+','-','.']
    while(speNum>0):
        password.append(special[random.randint(0,10)])
        speNum-=1;

    random.shuffle(password)
    message2.pack_forget()
    message2.config(text = password)
    message2.pack()
    
root.mainloop()
