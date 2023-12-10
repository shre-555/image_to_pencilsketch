import tkinter as tk
from tkinter import *
from tkinter import filedialog #filedialog is submodule containing tkopenfile
from tkinter.filedialog import askopenfile 
from PIL import Image, ImageTk
import customtkinter as ctk
import numpy as np
import cv2
import colour_pencil as cpsk
import random
import pencil_sketch as psk
import Textured_sketch as tsk
import watercolor as wat
import Enhancement as en


root=ctk.CTk()
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root.geometry("1200x800")
root.title("Image to Sketch")
my_font1=('Constantia', 18)


is_enabled=False
image = None
colour_button = None
pencil_button= None
textured_button= None
watercolor_button = None
pick_for_me= None
final_img= None

def upload():
    global panelA, panelB, image, colour_button, pencil_button, watercolor_button, panelC
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png')] 
    path = filedialog.askopenfilename(filetypes=f_types)

    is_enabled = True
    
    image = cv2.imread(path) #reads image from path and converts to an array
    
    image = cv2.resize(image, (500,500))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image1 = Image.fromarray(image)

    image1 = ImageTk.PhotoImage(image1)

    panelA = Label(master=mainbar,image=image1, borderwidth=5, relief="sunken")
    panelA.image = image1
    panelA.grid(row= 3, column=0 , padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Original Image', font=my_font1)
    text.grid(row= 4, column=0, padx=20, pady=20)

    colour_button.configure(state="normal")
    pencil_button.configure(state="normal")
    textured_button.configure(state="normal")
    watercolor_button.configure(state="normal")
    pick_for_me.configure(state="normal")

    return image



def colourpencil():
    global final_img
    cps= cpsk.colour_sketch(image)
    final_img= Image.fromarray(cps)
    final_img1= ImageTk.PhotoImage(final_img)
    panelB = Label(master=mainbar,image=final_img1, borderwidth=5, relief="sunken")
    panelB.image = final_img1
    panelB.grid(row= 3, column=4 , padx=20, pady=20)
    def enhanced():
        global final_img
        final_img = en.colour_enhancement(final_img)
        final_img1 = ImageTk.PhotoImage(final_img)
        panelC = Label(master=mainbar, image=final_img1, borderwidth=5, relief="sunken")
        panelC.image = final_img1
        panelC.grid(row=3, column=4, padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Colour Pencil Sketch', font=my_font1,fg_color="#212121",width=300)
    text.grid(row= 4, column=4 , padx=20, pady=20)
    enhance_button = ctk.CTkButton(mainbar, text='Enhance', command=enhanced)
    enhance_button.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")
    download_button=ctk.CTkButton(mainbar, text='Download', command = downloading)
    download_button.grid(row= 6, column=4 , padx=20, pady=20, sticky="nsew")

def pencil():
    global final_img
    ps= psk.pencil(image)
    final_img= Image.fromarray(ps)
    final_img1= ImageTk.PhotoImage(final_img)
    panelB = Label(master=mainbar,image=final_img1, borderwidth=5, relief="sunken")
    panelB.image = final_img1
    panelB.grid(row= 3, column=4 , padx=20, pady=20)
    def enhanced():
        global final_img
        final_img = en.pencil_enhancement(final_img)
        final_img1 = ImageTk.PhotoImage(final_img)
        panelC = Label(master=mainbar, image=final_img1, borderwidth=5, relief="sunken")
        panelC.image = final_img1
        panelC.grid(row=3, column=4, padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Pencil Sketch', font=my_font1,fg_color="#212121", width=300)
    text.grid(row= 4, column=4 , padx=20, pady=20)
    enhance_button = ctk.CTkButton(mainbar, text='Enhance', command=enhanced)
    enhance_button.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")
    download_button=ctk.CTkButton(mainbar, text='Download', command = downloading)
    download_button.grid(row= 6, column=4 , padx=20, pady=20, sticky="nsew")

def texturedpencil():
    global final_img
    ts=tsk.texturedpencil(image)
    final_img=Image.fromarray(ts)
    final_img1=ImageTk.PhotoImage(final_img)
    panelB = Label(master=mainbar,image=final_img1,borderwidth=5,relief="sunken")
    panelB.image = final_img1
    panelB.grid(row=3,column=4,padx=20,pady=20)
    def enhanced():
        global final_img
        final_img = en.texture_enhancement(final_img)
        final_img1 = ImageTk.PhotoImage(final_img)
        panelC = Label(master=mainbar, image=final_img1, borderwidth=5, relief="sunken")
        panelC.image = final_img1
        panelC.grid(row=3, column=4, padx=20, pady=20)
    text=ctk.CTkLabel(mainbar,text="Textured Sketch",font=my_font1,fg_color="#212121",width=300)
    text.grid(row=4,column=4,padx=20,pady=20)
    enhance_button = ctk.CTkButton(mainbar, text='Enhance', command=enhanced)
    enhance_button.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")
    download_button=ctk.CTkButton(mainbar, text='Download', command = downloading)
    download_button.grid(row= 6, column=4 , padx=20, pady=20, sticky="nsew")

def watercolor():
    global final_img
    wcolor= wat.oil_sketch(image)
    final_img= Image.fromarray(wcolor)
    final_img1= ImageTk.PhotoImage(final_img)
    panelB = Label(master=mainbar,image=final_img1, borderwidth=5, relief="sunken")
    panelB.image = final_img1
    panelB.grid(row= 3, column=4 , padx=20, pady=20)
    def enhanced():
        global final_img
        final_img = en.water_enhancement(final_img)
        final_img1 = ImageTk.PhotoImage(final_img)
        panelC = Label(master=mainbar, image=final_img1, borderwidth=5, relief="sunken")
        panelC.image = final_img1
        panelC.grid(row=3, column=4, padx=20, pady=20)
    text= ctk.CTkLabel(mainbar,text='Watercolor', font=my_font1,fg_color="#212121",width=300)
    text.grid(row= 4, column=4 , padx=20, pady=20)
    enhance_button = ctk.CTkButton(mainbar, text='Enhance', command=enhanced)
    enhance_button.grid(row=5, column=4, padx=20, pady=20, sticky="nsew")
    download_button=ctk.CTkButton(mainbar, text='Download', command = downloading)
    download_button.grid(row= 6, column=4 , padx=20, pady=20, sticky="nsew")

def pick():
    sketch_list=[colourpencil, pencil, texturedpencil, watercolor]
    option= random.choice(sketch_list)
    if option==colourpencil:
        colourpencil()
    elif option==pencil:
        pencil()
    elif option==texturedpencil:
        texturedpencil()
    elif option==watercolor:
        watercolor()

def downloading():
    global final_img
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ('Jpg Files', '*.jpg'),("All files", "*.*")])
    if save_path:
            final_img.save(save_path)
            tk.messagebox.showinfo("Save Complete", f"Image saved successfully at:\n{save_path}")
    

mainbar=ctk.CTkScrollableFrame(master=root, width=700, orientation="horizontal")
l1 = ctk.CTkLabel(mainbar,text='Image to Sketch Converter',width=30,font=('Constantia', 30, 'bold'))  
l1.grid(row=1,column=0,sticky="nsew",padx=10, pady=30)
b1 = ctk.CTkButton(mainbar, text='Upload', width=300,command =upload)
b1.grid(row=2,column=0, pady=5,sticky="n")


sidebar=ctk.CTkFrame(master=root, width=300)

def side():
    global colour_button, pencil_button, textured_button ,watercolor_button, pick_for_me
    sidebar.grid_columnconfigure(0, weight=1)
    leaveline=ctk.CTkLabel(sidebar, text=" ")
    leaveline.grid(row=0,column=0, padx=10, pady=20, sticky="nsew")
    intro=ctk.CTkLabel(sidebar, text="Options", font=('Constantia', 18))
    intro.grid(row=1,column=0, padx=10, pady=5, sticky="nsew")
    pencil_button=ctk.CTkButton(sidebar, text='Pencil Sketch',command = pencil)
    colour_button=ctk.CTkButton(sidebar, text='Colour Pencil Sketch', command = colourpencil)
    textured_button=ctk.CTkButton(sidebar,text='Textured Pencil Sketch',command=texturedpencil)
    watercolor_button=ctk.CTkButton(sidebar,text='Watercolor painting',command=watercolor)
    pick_for_me=ctk.CTkButton(sidebar, text='Pick for me!', command = pick)
    if is_enabled:
        colour_button.configure(state="normal")
        pencil_button.configure(state="normal")
        textured_button.configure(state="normal")
        watercolor_button.configure(state="normal")
        pick_for_me.configure(state="normal")
    else:
        colour_button.configure(state="disabled")
        pencil_button.configure(state="disabled")
        textured_button.configure(state="disabled")
        watercolor_button.configure(state="disabled")
        pick_for_me.configure(state="disabled")

    colour_button.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
    pencil_button.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    textured_button.grid(row=4,column=0, padx=20, pady=20, sticky="nsew")
    watercolor_button.grid(row=5,column=0, padx=20, pady=20, sticky="nsew")
    pick_for_me.grid(row=7, column=0, padx=20, pady=20, sticky="nsew")

side()
sidebar.pack(side=tk.LEFT,fill='both', padx=5, pady=5)


mainbar.pack(side=tk.LEFT,fill='both',expand=True, padx=10,pady=5)

root.mainloop()
