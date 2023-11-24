import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import customtkinter as ctk

root=ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root.geometry("800x800")
root.title("Image to Sketch")
my_font1=('Constantia', 18, 'bold')


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename) # read the image file
    img=img.resize((100,100)) # new width & height
    img=ImageTk.PhotoImage(img) #to convert to format tkinter can use
    e1 =tk.Label(mainbar)
    e1.grid(row=3,column=2)
    e1.image = img # keep a reference! by attaching it to a widget attribute
    e1['image']=img # Show Image


sidebar=ctk.CTkFrame(master=root, width=100, fg_color='gray')
sidebar.pack(side=tk.LEFT,fill='both',expand=True)
mainbar=ctk.CTkFrame(master=root, width=500, fg_color='black')
mainbar.pack(side=tk.LEFT,fill='both',expand=True)

#mainbar.grid_rowconfigure(1, weight=1)
#mainbar.grid_columnconfigure(1, weight=1)
l1 = ctk.CTkLabel(mainbar,text='Upload Files & display',width=30,font=my_font1)  
l1.grid(row=1,column=2,columnspan=4,sticky="nsew",padx=10, pady=5)
b1 = ctk.CTkButton(mainbar, text='Upload Files', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4,sticky="nsew",padx=10, pady=5)


root.mainloop()
