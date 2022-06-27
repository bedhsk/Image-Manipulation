import cv2
import tkinter
import numpy as np
from tkinter import *
from cv2 import cvtColor
from PIL import ImageTk, Image
from main import escala, cut_image

def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)

    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH), borderMode = cv2.BORDER_CONSTANT, borderValue=(101, 146, 186))

ventana = tkinter.Tk()
ventana.geometry("800x650")
ventana.resizable(False, False)
ventana.config(background= "#6592ba")

# Creación del canvas
my_canvas = tkinter.Canvas(ventana, width=500, height=550, bg="white")
my_canvas.pack(pady=20)

# Añadir una imágen al canvas
image = cv2.imread('src/zero.png')
image = cvtColor(image, cv2.COLOR_BGR2RGB)

# Convirtiendo la imagen del formato de imutils a tkinter y añadiendola al canvas
im = Image.fromarray(image)
img = ImageTk.PhotoImage(image=im)
my_image = my_canvas.create_image(100, 125, anchor=NW, image=img)

# Botones de movimiento
def arriba():
    x = 0
    y = -10
    my_canvas.move(my_image, x, y)

def abajo():
    x = 0
    y = 10
    my_canvas.move(my_image, x, y)

def derecha():
    x = 10
    y = 0
    my_canvas.move(my_image, x, y)

def izquierda():
    x = -10
    y = 0
    my_canvas.move(my_image, x, y)

# Botones de rotación
def girar_derecha():
    rotatedImg = rotate_bound(image, 40)
    global img
    im = Image.fromarray(rotatedImg)
    img = ImageTk.PhotoImage(image=im)
    my_image = my_canvas.create_image(100, 125, image=img)
    my_canvas.ref

def girar_izquierda():
    rotatedImg = rotate_bound(image, -10)
    global img
    im = Image.fromarray(rotatedImg)
    img = ImageTk.PhotoImage(image=im)
    my_image = my_canvas.create_image(100, 125, image=img)


upbtn = tkinter.Button(ventana, text="↑", command=arriba, bg = "#808080")
upbtn.pack()
upbtn.place(x= 20, y=600)


downbtn = tkinter.Button(ventana, text="↓", command=abajo, bg = "#808080")
downbtn.pack()
downbtn.place(x=20 , y= 625)

leftbtn = tkinter.Button(ventana, text="←", command=izquierda, bg = "#808080")
leftbtn.pack()
leftbtn.place(x= 0, y= 625)

rightbtn = tkinter.Button(ventana, text="→", command=derecha, bg = "#808080")
rightbtn.pack()
rightbtn.place(x=35, y=625)

#Edicion de imagen
editorlbl = tkinter.Label(ventana, text = "Editor de imagen", bg = "#3b6a94")
editorlbl.place(x=700, y=0)

#ROTACION BOTONES Y LBL'S
rtlbl =tkinter.Label(ventana, text = "Rotación", bg= "#3b6a94")
rtlbl.place(x=700, y= 35)

rdbtn = tkinter.Button(ventana, text="⟳", command=girar_derecha, bg = "#808080")
rdbtn.pack()
rdbtn.place(x= 765 , y= 70 )

ribtn = tkinter.Button(ventana, text="⟲", command=girar_izquierda, bg = "#808080")
ribtn.pack()
ribtn.place(x= 730, y=70 )

#Cortar

ctlbl = tkinter.Label(ventana, text = "Cortar", bg= "#3b6a94" )
ctlbl.place(x=700, y= 105 )

anlbl = tkinter.Label(ventana, text = "Ancho", bg= "#3b6a94")
anlbl.place(x= 700, y= 135)

maxbtn = tkinter.Button(ventana, text ="+", bg = "#808080")
maxbtn.pack()
maxbtn.place (x=750 , y=135 )

minbtn = tkinter.Button(ventana, text= "-", command=lambda: cut_image(100,200,300,400),bg = "#808080")
minbtn.pack()
minbtn.place(x= 770 ,y=135)

allbl = tkinter.Label(ventana, text= "Alto", bg= "#3b6a94" )
allbl.place(x=700 , y=165)

mxbtn = tkinter.Button(ventana, text ="+", bg = "#808080")
mxbtn.pack()
mxbtn.place (x=750 , y=165 )

mnbtn = tkinter.Button(ventana, text= "-", bg = "#808080")
mnbtn.pack()
mnbtn.place(x= 770 ,y=165)

masbtn = tkinter.Button (ventana, text = "MAXIMIZAR", bg = "#808080")
masbtn.pack()
masbtn.place(x= 700 ,y=195)

menbtn = tkinter.Button(ventana, text = "MINIMIZAR", bg = "#808080")
menbtn.pack()
menbtn.place(x =700, y=225 )

#IMAGENES

ign1 = tkinter.Button(ventana, text ="Imagen 1",command=lambda: escala(600,500), bg = "#808080")
ign1.pack()
ign1.place(x= 600, y=620)

ign2 = tkinter.Button(ventana, text ="Imagen 2", bg = "#808080")
ign2.pack()
ign2.place(x=700, y= 620)



ventana.mainloop()