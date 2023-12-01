import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import customtkinter as ctk
import numpy as np
import cv2
import colour_pencil as cpsk

root=ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root.geometry("800x800")
root.title("Image to Sketch")
my_font1=('Constantia', 18)
is_enabled=False
image = None
colour_button = None

def upload():
    global panelA, panelB, image
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    path = filedialog.askopenfilename(filetypes=f_types)

    is_enabled = True
    
    image = cv2.imread(path) 
    image = cv2.resize(image, (500,500))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image)

    image1 = ImageTk.PhotoImage(image1)

    panelA = Label(master=mainbar,image=image1, borderwidth=5, relief="sunken")
    panelA.image = image1
    panelA.grid(row= 3, column=2 , padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Original Image', font=my_font1)
    text.grid(row= 4, column=2, padx=20, pady=20)

    colour_button.configure(state="normal")

    return image



def colourpencil():
    if image is None:
        print("Upload an image")
        return
    cps= cpsk.colour_sketch(image)
    pencil= Image.fromarray(cps)
    pencil= ImageTk.PhotoImage(pencil)
    panelB = Label(master=mainbar,image=pencil, borderwidth=5, relief="sunken")
    panelB.image = pencil
    panelB.grid(row= 3, column=4 , padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Colour Pencil Sketch', font=my_font1,fg_color="#262626")
    text.grid(row= 4, column=4 , padx=20, pady=20)



mainbar=ctk.CTkScrollableFrame(master=root, width=700, orientation="horizontal")
l1 = ctk.CTkLabel(mainbar,text='Upload Files & display',width=30,font=my_font1)  
l1.grid(row=1,column=0,sticky="nsew",padx=10, pady=5)
#icon = PhotoImage(file=r"C:\Users\ROSHNI\OneDrive\Pictures\upload_icon.png")
b1 = ctk.CTkButton(mainbar, text='Upload', width=50,command =upload)
b1.grid(row=2,column=0,sticky="nsew",padx=10, pady=5)


sidebar=ctk.CTkFrame(master=root, width=100)

def side():
    global colour_button
    sidebar.grid_columnconfigure(0, weight=1)
    intro=ctk.CTkLabel(sidebar, text="Image to Sketch", font=('Constantia', 18, 'bold'))
    intro.grid(row=0,column=0, padx=10, pady=5, sticky="nsew")
    #pencil_button=ctk.CTkButton(sidebar, text='Pencil Sketch',command = pencil)
    #pencil_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    colour_button=ctk.CTkButton(sidebar, text='Colour Pencil Sketch', command = colourpencil)
    print(is_enabled)
    if is_enabled:
        colour_button.configure(state="normal")
    else:
        colour_button.configure(state="disabled")
    colour_button.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

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
