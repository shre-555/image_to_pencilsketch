import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import customtkinter as ctk
import numpy as np
import artistic as art
import cv2

root=ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root.geometry("800x800")
root.title("Image to Sketch")
my_font1=('Constantia', 18)


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename) # read the image file
    img=img.resize((100,100)) # new width & height
    img1=ImageTk.PhotoImage(img) #to convert to format tkinter can use
    e1 =tk.Label(mainbar)
    e1.grid(row=3,column=2)
    e1.image = img1 # keep a reference! by attaching it to a widget attribute
    e1['image']=img1 # Show Image

#org_img= cv2.imdecode(np.fromstring(filename.read(), np.uint8), 1)

'''
def pencil1():
    global org_img
    res=art.sketch(org_img)
    res_img=Image.fromarray(org_img)
    res_img=ImageTk.PhotoImage(res_img)
    e2 =tk.Label(mainbar)
    e2.grid(row=3,column=3)
    e2.image = res_img # keep a reference! by attaching it to a widget attribute
    e2['image']=res_img # Show Image
'''

sidebar=ctk.CTkFrame(master=root, width=100)

def side():
    sidebar.grid_columnconfigure(0, weight=1)
    intro=ctk.CTkLabel(sidebar, text="Image to Sketch", font=('Constantia', 18, 'bold'))
    intro.grid(row=0,column=0, padx=10, pady=5, sticky="nsew")
    pencil_button=ctk.CTkButton(sidebar, text='Pencil Sketch',command = lambda:pencil1())
    pencil_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

side()
sidebar.pack(side=tk.LEFT,fill='both',expand=True, padx=5, pady=5)
mainbar=ctk.CTkScrollableFrame(master=root, width=700, orientation="horizontal")
mainbar.pack(side=tk.LEFT,fill='both',expand=True, padx=10,pady=5)


l1 = ctk.CTkLabel(mainbar,text='Upload Files & display',width=30,font=my_font1)  
l1.grid(row=1,column=2,columnspan=4,sticky="nsew",padx=10, pady=5)
#icon = PhotoImage(file=r"C:\Users\ROSHNI\OneDrive\Pictures\upload_icon.png")
b1 = ctk.CTkButton(mainbar, text='Upload Files', width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4,sticky="nsew",padx=10, pady=5)


root.mainloop()
