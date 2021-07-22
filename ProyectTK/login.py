import  tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb
from Models import loginDB
from menu import *

global mL
mL = loginDB.DataLogin()
color = '#c5e2f6'
root=tk.Tk()
root.geometry('200x100')
root.title('Inicio de Sesión')
root.geometry('300x520+550+150')
root.resizable(0,0)
root.config(background=color)

#Textos
Label(root, bg=color, text='Login', font=('Arial Black', 16)).place(x=100, y=10)
Label(root, text='Usuario: ', bg=color, font=('Arial Black', 12)).place(x=105, y=230)
Label(root, text='Contraseña: ', bg=color, font=('Arial Black', 12)).place(x=95, y=290)
Label(root, text='¿No tienes una cuenta?', bg=color,font=("Arial Black",12)).place(x=55, y=400)

#Entradas
entry_user = Entry(root, font=("Arial", 12), relief = 'flat')
entry_user.focus()
entry_user.place(x=55, y=260)
entry_pass = Entry(root, font=("Arial", 12), relief = 'flat', show='*')
entry_pass.place(x=55, y=320)

#Convertir e insertar primera imagen
imagen = Image.open("Imagenes/logo.jpg")
imagen = imagen.resize((180, 180), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(imagen)
pane1 = tk.Label(root, image=photoImg).place(x=50, y=40)

#Convertir segunda imagen
imagen2 = Image.open("Imagenes/logo2.jpg")
imagen2 = imagen2.resize((100, 220), Image.ANTIALIAS)
photoImg2 = ImageTk.PhotoImage(imagen2)

def callMenu():
    wind_menu = Tk.Tk()
    menu_wind = MenuVenta(wind_menu)
    wind_menu.mainloop()

def login():
    user = entry_user.get()
    contra = entry_pass.get()
    arranque = mL.loginValidate(user, contra)
    if arranque:
        root.destroy()
        callMenu()
    else:
        mb.showinfo(title="Informe", message="Usuario y/o Contraseña incorrectos")
    
def newRoot():
    root2 = tk.Toplevel(root)
    root2.title("Nuevo Usuario")
    root2.geometry("300x290+1000+250")
    root2.config(bg=color)

    #Insertar segunda imagen
    labelExample = tk.Label(root2, text="Registro: ", bg=color, font=("Arial Black",12)).pack(side="top")
    pane2 = tk.Label(root2, image=photoImg2).pack(side="left")

    #Textos y Entradas - Root2
    Label(root2, text="Nombre: ", bg=color, font=("Arial Black",12)).pack()
    entry_name = Entry(root2, font=("Arial", 12), relief = 'flat')
    entry_name.focus()
    entry_name.pack()
    Label(root2, text="Apellido: ", bg=color, font=("Arial Black",12)).pack()
    entry_surname = Entry(root2, font=("Arial", 12), relief = 'flat')
    entry_surname.pack()
    Label(root2, text="Usuario: ", bg=color, font=("Arial Black",12)).pack()
    entry_RegistUser = Entry(root2, font=("Arial", 12), relief = 'flat')
    entry_RegistUser.pack()
    Label(root2, text="Contraseña: ", bg=color, font=("Arial Black",12)).pack()
    entry_RegistPass = Entry(root2, font=("Arial", 12), relief = 'flat', show="*")
    entry_RegistPass.pack()
    Label(root2, text="Repita la Contraseña: ", bg=color, font=("Arial Black",12)).pack()
    entry_PassValid = Entry(root2, font=("Arial", 12), relief = 'flat', show="*")
    entry_PassValid.pack()

    def registerUser():
        name = entry_name.get()
        surname = entry_surname.get()
        userRegist = entry_RegistUser.get()
        contra = entry_RegistPass.get()
        contraValid = entry_PassValid.get()
        if(entry_name.get()!='' and entry_surname.get()!='' and entry_RegistUser.get()!='' and entry_RegistPass.get()!='' and entry_PassValid.get()!=''):
            if (contra ==contraValid):
                mL.insertItems(name, surname, userRegist, contra)
                mb.showinfo(title="Informe", message="Hola "+name+" ¡¡ \nSu registro fue Exitoso")
                root2.destroy()
            else:
                mb.showinfo(title="Informe", message="Error!! \nLas contraseñas no coinciden")
        else:
            mb.showinfo(title="Informe", message="Campos incompletos")
    
    #Boton registro
    bnt_regist = tk.Button(root2, text="Registrar!", bg =color, font=("Arial Rounded MT Bold", 10), command=registerUser).pack(side='bottom')

#Botones
bnt_entrar = Button(root, text ='ENTRAR', bg='#a6d4f2', font=("Arial Rounded MT Bold",10), command=login)
bnt_entrar.place(x=100, y=360)
btn_registro = Button(root, text = 'REGISTRO', bg='#a6d4f2', font=("Arial Rounded MT Bold",10,), command=newRoot)
btn_registro.place(x=93, y=440)

root.mainloop()