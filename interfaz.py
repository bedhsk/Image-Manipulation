import tkinter

from main import escala, cut_image

ventana = tkinter.Tk()
ventana.geometry("800x650")
ventana.resizable(False, False)
ventana.config(background= "#6592ba")

#PESTAÑA 

pslbl = tkinter.Label(ventana, text ="                                     "  , bg ="#3b6a94") 
pslbl.pack(side= tkinter.RIGHT, fill = tkinter.Y)


#fLECHAS

upbtn = tkinter.Button(ventana, text="↑", bg = "#808080")
upbtn.pack()
upbtn.place(x= 20, y=600)


downbtn = tkinter.Button(ventana, text="↓", bg = "#808080")
downbtn.pack()
downbtn.place(x=20 , y= 625)

leftbtn = tkinter.Button(ventana, text="←", bg = "#808080")
leftbtn.pack()
leftbtn.place(x= 0, y= 625)

rightbtn = tkinter.Button(ventana, text="→", bg = "#808080")
rightbtn.pack()
rightbtn.place(x=35, y=625)

#Edicion de imagen


editorlbl = tkinter.Label(ventana, text = "Editor de imagen", bg = "#3b6a94")
editorlbl.place(x=700, y=0)

#ROTACION BOTONES Y LBL'S

rtlbl =tkinter.Label(ventana, text = "Rotación", bg= "#3b6a94")
rtlbl.place(x=700, y= 35)

rdbtn = tkinter.Button(ventana, text="⟳", bg = "#808080")
rdbtn.pack()
rdbtn.place(x= 765 , y= 70 )

ribtn = tkinter.Button(ventana, text="⟲", bg = "#808080")
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

#minimizar maximizar 

masbtn = tkinter.Button (ventana, text = "MAXIMIZAR", bg = "#808080")
masbtn.pack()
masbtn.place(x= 700 ,y=195)

menbtn = tkinter.Button(ventana, text = "MINIMIZAR", bg = "#808080")
menbtn.pack()
menbtn.place(x =700, y=225 )

#IMAGENES

ign1 = tkinter.Button(ventana, text ="Imagen 1",command=lambda: escala(600,500), bg = "#808080")
ign1.pack()
ign1.place(x= 715, y=580)

ign2 = tkinter.Button(ventana, text ="Imagen 2", bg = "#808080")
ign2.pack()
ign2.place(x=715, y= 620)



ventana.mainloop()