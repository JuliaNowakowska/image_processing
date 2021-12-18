#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import Label,Tk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import math
import matplotlib.pyplot as plt
import numpy as np

root = Tk()

################# WCZYTYWANIE OBRAZKA #######################    
path= askopenfilename(filetypes=[("Image File",'*.jpg'), ("PNG files", "*.png")])
im = Image.open(path)
tkimage = ImageTk.PhotoImage(im)
myvar=Label(root,image = tkimage)
myvar.image = tkimage
myvar.pack()

img1 = Image.open(path)
############################################################    
    
    
    

################# FUNKCJE PRZEKSZTAŁCAJĄCE ###################

####### LOGARYTM ########
    
def logarytm():
    obraz_poprawiony = logPoprawienie(img1)
    obraz_poprawiony.save("obraz_poprawiony_log.jpg")
    
    
def logPoprawienie(img):
    #getting the shape of an image
    height, width = img.size
    
    #scaling constant
    c = 255/math.log(float(255), 10)

    #Loop through all the pixels
    for w in range(0, width):
        for h in range(0, height):
            colors = list(img.getpixel((h,w)))
            
            #changing each pixel by logarithm function
            red = round(c * math.log(float(1 + colors[0]), 10))
            green = round(c * math.log(float(1 + colors[1]), 10))
            blue = round(c * math.log(float(1 + colors[2]), 10))

            img.putpixel((h,w), (red, green, blue))
    
    #returning changed image
    return img  

################################# 


####### POTĘGA ########

def potega():
    gamma = float(e1.get())
    obraz_poprawiony = potegaPoprawienie(img1, gamma)
    obraz_poprawiony.save("obraz_poprawiony_pot.jpg")

    
def potegaPoprawienie(img, gamma):
    #getting the shape of an image
    height, width = img.size
    
    #Loop through all the pixels
    for w in range(0, width):
        for h in range(0, height):
            
            #get RGB values of the pixel
            colors = list(img.getpixel((h,w)))
            
            #changing each pixel by power-law function
            red = round(255*math.pow((colors[0]/255),gamma))
            green = round(255*math.pow((colors[1]/255),gamma))
            blue = round(255*math.pow((colors[2]/255),gamma))

            #saving new intensity values in the pixel
            img.putpixel((h,w), (red, green, blue))
    
    #returning image
    return img

################################# 

def liniowe():
    x1 = float(e2.get())
    y1 = float(e3.get())
    x2 = float(e4.get())
    y2 = float(e5.get())
    obraz_poprawiony_liniowe = przedzialami_liniowymi(img1, x1, y1, x2, y2)
    obraz_poprawiony_liniowe.save("obraz_poprawiony_lin.jpg")

    
def przedzialami_liniowymi(img, x1, y1, x2, y2):
    #getting the shape of an image
    height, width = img.size
    
    #Loop through all the pixels
    for w in range(0, width):
        for h in range(0, height):
            
            #get RGB values of the pixel
            colors = list(img.getpixel((h,w)))
            
            #generating R value
            if (0 <= colors[0] and colors[0] <= x1):
                colors[0] = (y1 / x1)*colors[0]
            elif (x1 < colors[0] and colors[0] <= x2):
                colors[0] = ((y2 - y1)/(x2 - x1)) * (colors[0] - x1) + y1
            else:
                colors[0] = ((255 - y2)/(255 - x2)) * (colors[0] - x2) + y2

            #generating G value    
            if (0 <= colors[1] and colors[1] <= x1):
                colors[1] = (y1 / x1)*colors[1]
            elif (x1 < colors[1] and colors[1] <= x2):
                colors[1] = ((y2 - y1)/(x2 - x1)) * (colors[1] - x1) + y1
            else:
                colors[1] = ((255 - y2)/(255 - x2)) * (colors[1] - x2) + y2  
            
            #generating B value    
            if (0 <= colors[2] and colors[2] <= x1):
                colors[2] = (y1 / x1)*colors[2]
            elif (x1 < colors[2] and colors[2] <= x2):
                colors[2] = ((y2 - y1)/(x2 - x1)) * (colors[2] - x1) + y1
            else:
                colors[2] = ((255 - y2)/(255 - x2)) * (colors[2] - x2) + y2
            
            #saving to a tuple and puting into pixel
            new_tuple = (int(colors[0]), int(colors[1]), int(colors[2]))
            img.putpixel((h,w), new_tuple)
    
    return img
    
    




    
################ WYBÓR PRZEKSZTAŁCENIA #####################    
master = tk.Tk()
master.title("Poprawa obrazu według równania")

tk.Label(master,
         text="Wybierz przekształcenie:").grid(row=0)


#### LOGARYTMICZNE ####
tk.Label(master,
         text="Przekształcenie logarytmiczne").grid(row=1, column = 0)
tk.Button(master,
          text='Wygeneruj', command=logarytm).grid(row=1,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)
#######################


#### POTĘGOWE ####
tk.Label(master,
         text="Przekształcenie potęgowe, podaj wykładnik: ").grid(row=2, column = 0)
e1 = tk.Entry(master)
e1.grid(row=2, column=1)              
tk.Button(master,
          text='Wygeneruj', command=potega).grid(row=2, column=3, sticky=tk.W,pady=4)
##################              


#### PRZEDZIALAMI LIN. ####
tk.Label(master,
         text="Przekształcenie przedziałami liniowymi, podaj współrzędne: ").grid(row=3, column = 0)

tk.Label(master,
         text="x1: ").grid(row=4, column = 0)
tk.Label(master,
         text="y1: ").grid(row=4, column = 2)
tk.Label(master,
         text="x2: ").grid(row=5, column = 0)
tk.Label(master,
         text="y2: ").grid(row=5, column = 2)


e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)


e2.grid(row=4, column=1)
e3.grid(row=4, column=3)
e4.grid(row=5, column=1)
e5.grid(row=5, column=3)

tk.Button(master,
          text='Wygeneruj', command=liniowe).grid(row=6,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)



############################################################



root.mainloop()

