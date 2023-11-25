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

##filename=0
##
##def upload_file():
##    global filename
##    f_types = [('Jpg Files', '*.jpg'),
##    ('PNG Files','*.png')]   # type of files to select 
##    filename = tk.filedialog.askopenfilename(filetypes=f_types)
##    img=Image.open(filename) # read the image file
##    img=img.resize((100,100)) # new width & height
##    img1=ImageTk.PhotoImage(img) #to convert to format tkinter can use
##    e1 =tk.Label(mainbar)
##    e1.grid(row=3,column=2)
##    e1.image = img1 # keep a reference! by attaching it to a widget attribute
##    e1['image']=img1 # Show Image

def upload():
    global panelA, panelB, image
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    path = filedialog.askopenfilename(filetypes=f_types)
    image = cv2.imread(path) 
    image = cv2.resize(image, (500,500))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image)

    image1 = ImageTk.PhotoImage(image1)

    panelA = Label(master=mainbar,image=image1, borderwidth=5, relief="sunken")
    panelA.image = image1
    panelA.grid(row= 3, column=2 , padx=20, pady=20)
    
    return image

def pencil():
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img)
    img_smoothing = cv2.GaussianBlur(img_invert, (25, 25),sigmaX=0, sigmaY=0)
    
    pencilimg = cv2.divide(img, 255 - img_smoothing, scale=255)
    pencilimg1= Image.fromarray(pencilimg)
    
    pencilimg1= ImageTk.PhotoImage(pencilimg1)
    
    panelB = Label(master=mainbar,image=pencilimg1, borderwidth=5, relief="sunken")
    panelB.image = pencilimg1
    panelB.grid(row= 3, column=4 , rowspan= 13,columnspan= 3, padx=20, pady=20)


mainbar=ctk.CTkScrollableFrame(master=root, width=700, orientation="horizontal")
l1 = ctk.CTkLabel(mainbar,text='Upload Files & display',width=30,font=my_font1)  
l1.grid(row=1,column=2,columnspan=4,sticky="nsew",padx=10, pady=5)
#icon = PhotoImage(file=r"C:\Users\ROSHNI\OneDrive\Pictures\upload_icon.png")
b1 = ctk.CTkButton(mainbar, text='Upload', width=20,command =upload)
b1.grid(row=2,column=1,columnspan=4,sticky="nsew",padx=10, pady=5)


sidebar=ctk.CTkFrame(master=root, width=100)

def side():
    sidebar.grid_columnconfigure(0, weight=1)
    intro=ctk.CTkLabel(sidebar, text="Image to Sketch", font=('Constantia', 18, 'bold'))
    intro.grid(row=0,column=0, padx=10, pady=5, sticky="nsew")
    pencil_button=ctk.CTkButton(sidebar, text='Pencil Sketch',command = pencil)
    pencil_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

side()
sidebar.pack(side=tk.LEFT,fill='both',expand=True, padx=5, pady=5)

'''org_img= cv2.imdecode(np.fromstring(filename.read(), np.uint8), 1)

def pencil1():
    global org_img
    res=art.sketch(org_img)
    res_img=Image.fromarray(org_img)
    res_img=ImageTk.PhotoImage(res_img)
    e2 =tk.Label(mainbar)
    e2.grid(row=3,column=3)
    e2.image = res_img # keep a reference! by attaching it to a widget attribute
    e2['image']=res_img # Show Image'''

mainbar.pack(side=tk.LEFT,fill='both',expand=True, padx=10,pady=5)

root.mainloop()
