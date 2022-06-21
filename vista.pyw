from os import system
import os
from tkinter import *  #importar libreria tkinter con todos sus metodos
from tkinter import messagebox
from tkinter.font import BOLD
from typing import Sized
from validacion import Validacion
class Ventana():
    def __init__(self):        
        
        self.__raiz=Tk() #raiz es la ventana principal "primera capa", aqui se usa la clase Tk() y se guarda en raiz
        self.__raiz.title("validacion") #lo idea es crear primero la ventana y sobre la ventana agregar luego frames y wdigets
        self.__raiz.resizable(False,False) #metodo para que que el alto y ancho de la ventana sean modificables o no
        self.__raiz.geometry("700x416") # metodo para dimensionar la ventana
        self.__raiz.iconbitmap("iconos/_cubitos.ico") #metodo para cambiar el icono de la ventana en la aprte superior izquierda
        self.__validar=Validacion()
        self.__imgLogo=PhotoImage(file="iconos/_buscar.png")
        self.__imgAyuda=PhotoImage(file="iconos/_ayuda.png")
        self.__imagen1=PhotoImage(file="iconos/_pregunta.png")
        self.__imagen2=PhotoImage(file="iconos/_esperar.png")
        self.__imagen3=PhotoImage(file="iconos/_correcto.png")
        self.__imagen4=PhotoImage(file="iconos/_error.png")
        self.__imagen5=PhotoImage(file="iconos/_anterior.png")
        self.__cEntero=StringVar()
        self.__cReal=StringVar()
        self.__cNotC=StringVar()
        self.__cCorreo=StringVar()          
        self.__myFrame=Frame(bg="#6D9897",bd=10,relief="raised",cursor="pirate") #*myFrame es un objeto de la clase Frame() y con este comenzamos a crear el frame que ira en la ventana
        self.__myFrame.pack(fill="both",expand="True")#con este metodo enpaquetamos al frame en la ventana principal pack()
        #el metodo config() nos permite modificar todas las propiedades del frame e incluso de la ventana
        #con la clase Label() creamos los labels que iran en nuestro frame en este caso "expresiones regulares"
        #aqui se indica que el label se creara en myFrame y con el metodo grid() terminamos de indicar donde debe aparecer
        #el metodo grid() va a dividir el frame como si fuese una matriz por ejemplo el primer label (row=0,column=1) esta en la fila 0 y columna 1
        #el valor columnspan nos indica cuandtas columnas va a ocupar el label o cualquier widget
        #el valor sticky nos dice que dentro de la celda se va a posicionar en la posicion West (W) osea a la izquierda
        #los valores padx y pady nos sirven para dimensionar la celda en sus coordenadas X y Y
        #los valores ipadx y ipady nos sirven para dimensionar el label o cualquier widget dentro de la celda en sus coordenadas X y Y
        Label(self.__myFrame,text="Expresiones Regulares",bg="#6D9897",fg="Black",font=("Calibri Light",25,BOLD)).grid(row=0,column=1,columnspan=2,ipady=15,sticky=W)    
        Label(self.__myFrame,image=self.__imgLogo,bg="#6D9897").grid(row=0,column=0)        
        self.__btnAyuda=Button(self.__myFrame,image=self.__imgAyuda,command=self.btnA_ayuda)
        self.__btnAyuda.grid(row=0,column=3)        
        #--CREACION WIDGETS PARA VALIDAR ENTEROS--
        Label(self.__myFrame,text="Enteros.........:",bg="#6D9897",fg="Black",font=("Calibri Light",20,BOLD)).grid(row=1,column=0) #el metodo grid() nos permitira acomodar los elementos de una manera mas sencilla
        self.__enteroEntry=Entry(self.__myFrame,textvariable=self.__cEntero,fg="Black",font=("Calibri Light",15),bg="#E6D375",relief="groove",justify=CENTER).grid(row=1,column=1,sticky=W,ipadx=50)
        #la Clase Entry() nos permitira crear cuadros de texto en los que se puede digitar, en los parametros especificar a quien pertenece
        self.__lbEnt=Label(self.__myFrame,image=self.__imagen2,bg="#6D9897",fg="Black",font=("Calibri Light",20))
        self.__lbEnt.grid(row=1,column=2,sticky=W)
        Button(self.__myFrame,image=self.__imagen1,bg="#CAA94D",relief="groove",command=self.btnA_e).grid(row=1,column=3,) #la Clase Button() nos permitira crear botones    
        Label(self.__myFrame,text="--------------------------------------------------------------------------------------------------------------",bg="#6D9897",fg="Black",font=("Calibri Light",16)).grid(row=2,column=0,columnspan=4)
        #--CREACION WIDGETS PARA VALIDAR REALES--
        Label(self.__myFrame,text="Reales...........:",bg="#6D9897",fg="Black",font=("Calibri Light",20,BOLD)).grid(row=3,column=0)
        Entry(self.__myFrame,textvariable=self.__cReal,fg="Black",font=("Calibri Light",15),bg="#E6D375",relief="groove",justify=CENTER).grid(row=3,column=1,sticky=W,ipadx=50) 
        self.__lbReal=Label(self.__myFrame,image=self.__imagen2,bg="#6D9897",fg="Black",font=("Calibri Light",20))
        self.__lbReal.grid(row=3,column=2,sticky=W)
        Button(self.__myFrame,image=self.__imagen1,bg="#CAA94D",relief="groove",command=self.btnA_r).grid(row=3,column=3)
        Label(self.__myFrame,text="--------------------------------------------------------------------------------------------------------------",bg="#6D9897",fg="Black",font=("Calibri Light",16)).grid(row=4,column=0,columnspan=4)
        #--CREACION WIDGETS PARA VALIDAR NOTACION CIENTIFICA--
        Label(self.__myFrame,text="Not.C............:",bg="#6D9897",fg="Black",font=("Calibri Light",20,BOLD)).grid(row=5,column=0)
        Entry(self.__myFrame,textvariable=self.__cNotC,fg="Black",font=("Calibri Light",15),bg="#E6D375",relief="groove",justify=CENTER).grid(row=5,column=1,sticky=W,ipadx=50) 
        self.__lbNotc=Label(self.__myFrame,image=self.__imagen2,bg="#6D9897",fg="Black",font=("Calibri Light",20))
        self.__lbNotc.grid(row=5,column=2,sticky=W)
        Button(self.__myFrame,image=self.__imagen1,bg="#CAA94D",relief="groove",command=self.btnA_notC).grid(row=5,column=3)
        Label(self.__myFrame,text="--------------------------------------------------------------------------------------------------------------",bg="#6D9897",fg="Black",font=("Calibri Light",16)).grid(row=6,column=0,columnspan=4)
        #--CREACION WIDGETS PARA VALIDAR CORREOS--
        Label(self.__myFrame,text="Correo...........:",bg="#6D9897",fg="Black",font=("Calibri Light",20,BOLD)).grid(row=7,column=0)
        Entry(self.__myFrame,textvariable=self.__cCorreo,fg="Black",font=("Calibri Light",15),bg="#E6D375",relief="groove",justify=CENTER).grid(row=7,column=1,sticky=W,ipadx=50)
        self.__lbCor=Label(self.__myFrame,image=self.__imagen2,bg="#6D9897",fg="Black",font=("Calibri Light",20))
        self.__lbCor.grid(row=7,column=2,sticky=W)
        Button(self.__myFrame,image=self.__imagen1,bg="#CAA94D",relief="groove",command=self.btnA_corr).grid(row=7,column=3)
        Label(self.__myFrame,text="--------------------------------------------------------------------------------------------------------------",bg="#6D9897",fg="Black",font=("Calibri Light",16)).grid(row=8,column=0,columnspan=4)
        #--NOMBRE AUTOR--
        Label(self.__myFrame,text="AUTOR:Johand Estebam Castro Rodriguez C.C: 1018506713",bg="#49E3E0",relief="groove",bd=5,font=("Calibri Light",10,BOLD)).grid(row=9,columnspan=4,sticky=W)
        #--OPCIONALES
        # self.myFrame.columnconfigure(0,weight=1) #con este metodo podemos ajustar las columnas (columna,ajuste)
        # self.myFrame.columnconfigure(1,weight=1) 
        # self.myFrame.columnconfigure(2,weight=0)
        # self.myFrame.columnconfigure(3,weight=1)
        # self.myFrame.rowconfigure(0,weight=0) #si se necesita ajustar las filas seria con el metodo rowconfigure(fila,ajuste)
        # self.myFrame.rowconfigure(1,weight=1)
        # self.myFrame.rowconfigure(2,weight=2)
        # self.myFrame.rowconfigure(3,weight=3)
        #------------------------------------------
        self.__raiz.mainloop() #este metodo nos permite siempre mostrar la ventana y siempre debe ir al final de la creacion de la ventana y los widgets
    
    
    def btnA_ayuda(self):
        self.__myFrame.pack_forget()
        self.__frameA1=Frame(self.__raiz,bg="#6D9897",bd=9,relief="groove",cursor="spider",width=191,height=56)
        self.__frameA1.grid(row=0,ipadx=253,padx=2)
        self.__frameA1.grid_propagate(False)
        Label(self.__frameA1,text="EJEMPLOS CORRECTOS",font=("Calibri Light",18,BOLD),bg="#6D9897").grid(row=0,column=1,padx=170)
        Button(self.__frameA1,command=self.btnA_volver,image=self.__imagen5,bg="#CAA94D").grid(row=0,column=0,sticky=W)
        self.__frameA2=Frame(self.__raiz,bg="#FC90E3",bd=9,relief="groove",cursor="spider",width=191,height=89.5)
        self.__frameA2.grid(row=1,ipadx=253,padx=2)
        self.__frameA2.grid_propagate(False)
        Label(self.__frameA2,text="EJEMPLO ENTEROS: 150050, +150100, -152000",anchor="w",bg="#FC90E3",font=("Calibri Light",18,BOLD)).grid(row=0,pady=16)
        self.__frameA3=Frame(self.__raiz,bg="#77FCFA",bd=9,relief="groove",cursor="spider",width=191,height=89.5)
        self.__frameA3.grid(row=2,ipadx=253,padx=2)
        self.__frameA3.grid_propagate(False)
        Label(self.__frameA3,text="EJEMPLO REALES: 700.015, +700.45, -700.78",anchor="w",bg="#77FCFA",font=("Calibri Light",18,BOLD)).grid(row=0,pady=16)
        self.__frameA4=Frame(self.__raiz,bg="#FCE25D",bd=9,relief="groove",cursor="spider",width=191,height=89.5)
        self.__frameA4.grid(row=3,ipadx=253,padx=2)
        self.__frameA4.grid_propagate(False)
        Label(self.__frameA4,text="EJEMPLO NOTACION C: 100.50E90, +100.50e+90, -100.50E-90",anchor="w",bg="#FCE25D",font=("Calibri Light",18,BOLD)).grid(row=0,pady=16)
        self.__frameA5=Frame(self.__raiz,bg="#B09F4A",bd=9,relief="groove",cursor="spider",width=191,height=89.5)
        self.__frameA5.grid(row=4,ipadx=253,padx=2)
        self.__frameA5.grid_propagate(False)
        Label(self.__frameA5,text="EJEMPLO CORREOS: Algo_algo78@correo.com.co, aaa@aaa.a",anchor="w",bg="#B09F4A",font=("Calibri Light",18,BOLD)).grid(row=0,pady=16)
       
    def btnA_volver(self):
        self.__frameA1.grid_forget()
        self.__frameA2.grid_forget()
        self.__frameA3.grid_forget()
        self.__frameA4.grid_forget()
        self.__frameA5.grid_forget()
        self.__myFrame.pack(fill="both",expand="True")

    def btnA_e(self):
        if self.__cEntero.get()=="":
            self.__lbEnt.config(image=self.__imagen2)
            messagebox.showerror("!Alerta¡","Por favor introduzca un dato")            
        else:
            if self.__validar.validarEntero(self.__cEntero.get()):
                self.__lbEnt.config(image=self.__imagen3)                        
            else:
                self.__lbEnt.config(image=self.__imagen4)

    def btnA_r(self):
        if self.__cReal.get()=="":            
            self.__lbReal.config(image=self.__imagen2)
            messagebox.showerror("!Alerta¡","Por favor introduzca un dato")
        else:
            if self.__validar.validarReal(self.__cReal.get()):
                self.__lbReal.config(image=self.__imagen3)
            else:
                self.__lbReal.config(image=self.__imagen4)
    
    def btnA_notC(self):
        if self.__cNotC.get()=="":                    
            self.__lbNotc.config(image=self.__imagen2)
            messagebox.showerror("!Alerta¡","Por favor introduzca un dato")  
        else:
            if self.__validar.validarNotC(self.__cNotC.get()):
                self.__lbNotc.config(image=self.__imagen3)                
            else:
                self.__lbNotc.config(image=self.__imagen4)
    
    def btnA_corr(self):
        if self.__cCorreo.get()=="":            
            self.__lbCor.config(image=self.__imagen2)
            messagebox.showerror("!Alerta¡","Por favor introduzca un dato") 
        else:
            if self.__validar.validarCorreo(self.__cCorreo.get()):
                self.__lbCor.config(image=self.__imagen3)
            else:
                self.__lbCor.config(image=self.__imagen4)
                
Ventana()
