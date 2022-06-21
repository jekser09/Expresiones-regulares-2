from os import cpu_count
from tkinter import *


class Prueba():    
    
    def __init__(self):
        
        self.raiz=Tk()
        self.raiz.title("prueba")    
        self.raiz.resizable(False,False)
        self.raiz.geometry("400x300")
        self.miframe=Frame(self.raiz)
        self.miframe.config(bg="white")
        self.miframe.pack(fill="both",expand="True")
        self.imagen=PhotoImage(file="iconos/ayuda.png")
        self.imagen2=PhotoImage(file="iconos/correcto.png")
        Label(self.miframe,text="prueba",bg="white",font=("Arial",20)).grid(row=0,column=0,columnspan=4,pady=10)
        Label(self.miframe,text="prueba:",bg="white",justify=CENTER).grid(row=1,column=0,padx=40)
        self.entry1=Entry(self.miframe,bg="gray")
        self.entry1.grid(row=1,column=1)
        self.labelImg=Label(self.miframe,image=self.imagen)
        self.labelImg.grid(row=1,column=2)
        self.boton1=Button(self.miframe,font=10,text="aceptar",bg="yellow",relief="groove",command=self.cambiarImg).grid(row=1,column=3)               
        self.raiz.mainloop()
        
    
    def cambiarImg(self):
        self.labelImg.config(image=self.imagen2)
        
        
    
prueba=Prueba()    

