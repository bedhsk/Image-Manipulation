#Participantes: Brian Bazt, Arge Reyes, Marti Pérez
import tkinter
import cv2
from cv2 import cvtColor
from cv2 import imread, resize
import numpy as np
from tkinter import *
from PIL import ImageTk, Image

def mezcla():
    #1366x768
    imagen_1=cv2.imread('hola.png') 
    imagen_1= cv2.cvtColor(imagen_1, cv2.COLOR_BGR2RGB)

    #1366x768
    imagen_2=cv2.imread('poligon.png')
    imagen_2= cv2.cvtColor(imagen_2, cv2.COLOR_BGR2RGB)
    imagen_2 = cv2.resize(imagen_2,(1366,300))

    parte_image_1= imagen_1[:300]
    mezcla_imagen = cv2.addWeighted(src1=parte_image_1,alpha=0.5,src2=imagen_2,beta=0.5, gamma=0)
    imagen_1[:300]= mezcla_imagen
    
    global img
    im = Image.fromarray(imagen_1)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Aplicar color azul sobre la imagen
def blue():
    copia = np.copy(image)
    
    copia[:,:,0]=0
    copia[:,:,1]=0
    global img
    im = Image.fromarray(copia)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Aplicar color rojo sobre la imagen
def red():
    copia = np.copy(image)
    
    copia[:,:,1]=0
    copia[:,:,2]=0
    global img
    im = Image.fromarray(copia)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Aplicar color verde sobre la imagen
def green():
    copia = np.copy(image)
    
    copia[:,:,0]=0
    copia[:,:,2]=0
    global img
    im = Image.fromarray(copia)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Variables globales para aplicar un rectángulo de color sobre la imagen
D1=0
D2=300
C1 = 0
C2 = 300
# Variables globales para controlar el color del rectángulo
r = g = b = 0

# Aplicar un rectángulo de color sobre la imagen
def importar(x1,x2,y1,y2):
    global D2 
    D2=y2
    global D1 
    D1=y1
    global C1 
    C1=x1
    global C2 
    C2=x2

    f, c, p = image.shape

    capa_color = np.zeros((f, c, p), dtype=np.uint8)
    capa_color[x1:x2, y1:y2] = (r,g,b)

    trans = cv2.add(image, capa_color)
    global img
    im = Image.fromarray(trans)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

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

    return cv2.warpAffine(image, M, (nW, nH), borderMode = cv2.BORDER_CONSTANT, borderValue=(300, 300, 300))

ventana = tkinter.Tk()
ventana.geometry("800x650")
ventana.resizable(False, False)
ventana.config(background= "#6592ba")
pslbl = tkinter.Label(ventana, text ="                                     "  , bg ="#3b6a94") 
pslbl.pack(side= tkinter.RIGHT, fill = tkinter.Y)

# Creación del canvas
my_canvas = tkinter.Canvas(ventana, width=500, height=550, bg="white")
my_canvas.pack(pady=20)

# Añadir una imágen al canvas
image = cv2.imread('src/zero.png') 
image = cvtColor(image, cv2.COLOR_BGR2RGB)

# Convirtiendo la imagen del formato de imutils a tkinter y añadiendola al canvas
im = Image.fromarray(image)
img = ImageTk.PhotoImage(image=im)
my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

angulo = 0
escalado = 0
# variables resize

x_zoom=0
y_zoom=0

y_zoom, x_zoom, _ = image.shape

def zoom():
    global angulo 
    angulo = 0
    global x_zoom, y_zoom
    x_zoom = x_zoom + 30
    y_zoom = y_zoom + 30
    global image
    rezim = cv2.resize(image,(x_zoom,y_zoom), interpolation=cv2.INTER_CUBIC)
    global img
    image= rezim
    im = Image.fromarray(rezim)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

def min():
    global angulo
    angulo = 0
    global x_zoom, y_zoom
    x_zoom = x_zoom - 30
    y_zoom = y_zoom - 30
    global image

    rezim = cv2.resize(image,(x_zoom,y_zoom), interpolation=cv2.INTER_CUBIC)
    global img
    image= rezim
    im = Image.fromarray(rezim)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Botones de rotación
def girar_derecha():
    # Incrementar el ángulo de rotación
    global angulo
    angulo +=10
    global image
    rotated_image = rotate_bound(image, angulo)
    global img
    # Convirtiendo la imagen del formato de imutils a tkinter y añadiendola al canvas
    im = Image.fromarray(rotated_image)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

def girar_izquierda():
    # Incrementar el ángulo de rotación
    global angulo
    angulo -=10
    global image
    rotated_image = rotate_bound(image, angulo)
    global img
    # Convirtiendo la imagen del formato de imutils a tkinter y añadiendola al canvas
    im = Image.fromarray(rotated_image)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

# Botones de movimiento
def arriba():
    x = 0
    y = -10
    my_canvas.move(my_canvas.my_image, x, y)

def abajo():
    x = 0
    y = 10
    my_canvas.move(my_canvas.my_image, x, y)

def derecha():
    x = 10
    y = 0
    my_canvas.move(my_canvas.my_image, x, y)

def izquierda():
    x = -10
    y = 0
    my_canvas.move(my_canvas.my_image, x, y)

#PESTAÑA 
upbtn = tkinter.Button(ventana, text="↑", command=arriba, bg = "#808080")

#FLECHAS
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

B1,B2, _=image.shape
A1 = 0
A2 = 0
def cut_image(x1,y1,x2,y2):
    global B2 
    B2=y2
    global B1 
    B1=y1
    cut = image[x1:y1,x2:y2]
    global img
    im = Image.fromarray(cut)
    img = ImageTk.PhotoImage(image=im)
    my_canvas.my_image = my_canvas.create_image(10, 10, anchor=NW, image=img)

def change_color(rojo,verde,azul):
    global r,g,b
    if(rojo>0):
        r=rojo
        g=0
        b=0
    if(verde>0):
        g=verde
        r=0
        b=0
    if(azul>0):
        b=azul
        g=0
        r=0
    importar(C1,C2,D1,D2)
    

maxbtn = tkinter.Button(ventana, text ="+",command=lambda:cut_image(A1,B1,A2,B2+200), bg = "#808080")
maxbtn.pack()
maxbtn.place (x=750 , y=135 )

minbtn = tkinter.Button(ventana, text= "-", command=lambda:cut_image(A1,B1,A2,B2-200),bg = "#808080")
minbtn.pack()
minbtn.place(x= 770 ,y=135)

allbl = tkinter.Label(ventana, text= "Alto", bg= "#3b6a94" )
allbl.place(x=700 , y=165)

mxbtn = tkinter.Button(ventana, text ="+",command=lambda:cut_image(A1,B1+200,A2,B2), bg = "#808080")
mxbtn.pack()
mxbtn.place (x=750 , y=165 )

mnbtn = tkinter.Button(ventana, text= "-",command=lambda:cut_image(A1,B1-200,A2,B2), bg = "#808080")
mnbtn.pack()
mnbtn.place(x= 770 ,y=165)

#minimizar maximizar 
masbtn = tkinter.Button (ventana, text = "MAXIMIZAR", command = zoom, bg = "#808080")
masbtn.pack()
masbtn.place(x= 700 ,y=195)

menbtn = tkinter.Button(ventana, text = "MINIMIZAR", command = min, bg = "#808080")
menbtn.pack()
menbtn.place(x =700, y=225 )

#IMAGENES
ign1 = tkinter.Button(ventana, text ="Transposición",command= mezcla, bg = "#808080")
ign1.pack()
ign1.place(x= 700, y=600)

#FLECHAS CUADRO
up = tkinter.Button(ventana, text="↑",command=lambda:importar(C1-25,C2-25,D1,D2),  bg = "#808080")
up.pack()
up.place(x= 720, y=400)


down = tkinter.Button(ventana, text="↓",command=lambda:importar(C1+25,C2+25,D1,D2),  bg = "#808080")
down.pack()
down.place(x=720 , y= 425)

left = tkinter.Button(ventana, text="←",command=lambda:importar(C1,C2,D1-25,D2-25), bg = "#808080")
left.pack()
left.place(x= 700, y= 425)

right = tkinter.Button(ventana, text="→",command=lambda:importar(C1,C2,D1+25,D2+25), bg = "#808080")
right.pack()
right.place(x=735, y=425)
#Colores
verde = tkinter.Button(ventana, text ="Verde",command=green, bg = "#808080")
verde.pack()
verde.place(x= 715, y=480)

azul = tkinter.Button(ventana, text ="Azul",command=blue, bg = "#808080")
azul.pack()
azul.place(x=715, y= 520)

rojo = tkinter.Button(ventana, text ="Rojo",command=red, bg = "#808080")
rojo.pack()
rojo.place(x=715, y= 560)

#Colorear
clbl = tkinter.Label(ventana, text = "Colorear", bg= "#3b6a94" )
clbl.place(x=700, y= 255 )

albl = tkinter.Label(ventana, text = "Ancho", bg= "#3b6a94")
albl.place(x= 700, y= 285)

maxtn = tkinter.Button(ventana, text ="+",command=lambda:importar(C1,C2,D1,D2+50), bg = "#808080")
maxtn.pack()
maxtn.place (x=750 , y=285 )

mintn = tkinter.Button(ventana, text= "-",command=lambda:importar(C1,C2,D1,D2-50),bg = "#808080")
mintn.pack()
mintn.place(x= 770 ,y=285)

alll = tkinter.Label(ventana, text= "Alto", bg= "#3b6a94" )
alll.place(x=700 , y=315)

mxtn = tkinter.Button(ventana, text ="+",command=lambda:importar(C1,C2+50,D1,D2), bg = "#808080")
mxtn.pack()
mxtn.place (x=750 , y=315 )

mntn = tkinter.Button(ventana, text= "-",command=lambda:importar(C1,C2-50,D1,D2), bg = "#808080")
mntn.pack()
mntn.place(x= 770 ,y=315)

v = tkinter.Button(ventana, text ="R",command=lambda:change_color(255,0,0), bg = "#808080")
v.pack()
v.place(x= 700, y=360)

a = tkinter.Button(ventana, text ="G",command=lambda:change_color(0,255,0), bg = "#808080")
a.pack()
a.place(x=720, y= 360)

r = tkinter.Button(ventana, text ="B",command=lambda:change_color(0,0,255), bg = "#808080")
r.pack()
r.place(x=740, y= 360)

ventana.mainloop()