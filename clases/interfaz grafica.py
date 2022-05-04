from cgitb import text
from logging import root
from tkinter import*
from tkinter import messagebox

from setuptools import Command

def obtener_usuario_clave():
    usuarios = {"genesis":"clave1", "johan": "clave2", "ramiro":"clave3", "jose":"clave4", "joaquin":"clave5"} 
    return usuarios

def validar_informacion(user_name, contrasenia):
    clave = user_name.get() 
    valor = contrasenia.get()

    diccionario = obtener_usuario_clave()

    if clave in diccionario and diccionario[clave] == valor:

        messagebox.showinfo("", "Usuario y Clave Correctos")

    else:

        messagebox.showwarning("", "Alguno de los datos ingresados es incorrecto")
        
def crear_ventana():
    raiz=Tk()
    
    raiz.title("Login Fortaleza")
    raiz.resizable(0,0)
    raiz.iconbitmap("nubes.ico")
    raiz.config(width="300" , height="130" , bg="grey" )
    
    miFrame=Frame(raiz,width="300" , height="130" )
    miFrame.pack()
    cuadroTexto_user_name=Entry(miFrame)
    cuadroTexto_user_name.grid(row=0, column=1)
    user_name= Label(miFrame,text = "Username")
    user_name.grid(row=0,column=0)
    cuadroTexto_password=Entry(miFrame)
    password= Label(miFrame, text = "Password")
    password.grid(row=1, column=0)
    cuadroTexto_password.grid(row=1, column=1)
    cuadroTexto_password.config(show="*")
    boton_aceptar = Button(miFrame, text="Ingresar", command = lambda: validar_informacion(cuadroTexto_user_name,cuadroTexto_password))
    boton_aceptar.grid(row=2,column=1)
    raiz.mainloop() 

def main():

    crear_ventana()

main()
