import tkinter as Tk
from tkinter import ttk
from PIL import ImageTk, Image
from View.productos import Productos
from View.clientes import Clientes
from View.pedidos import Pedidos

class MenuVenta(Tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title("MENU")
        self.master.geometry('1010x710+250+50')
        self.master.config(background='#c5e2f6')
        self.master.resizable(0,0)
        self.createWidgets()
        #self.inserImage()

    def createWidgets(self):
        nb = Tk.Menu(self.master)
        menu1 = Tk.Menu(nb)
        menu1.add_command(label='Producto', font=('Arial, 12'),command=self.callProducto)
        menu1.add_command(label='Clientes', font=('Arial, 12'), command=self.callCliente)
        menu1.add_command(label='Pedidos', font=('Arial, 12'), command=self.callPedidos)
        self.master.config(menu=  menu1)
        
    def inserImage(self):
        imagen = Image.open("Imagenes/portada.png")
        imagen = imagen.resize((1010, 710), Image.ANTIALIAS)
        photoImg = ImageTk.PhotoImage(imagen)
        pane1 = Tk.Label(self.master, image=photoImg).place(x=0, y=0)

    def callProducto(self):
        Productos(self.master)
          
    def callCliente(self):
        Clientes(self.master)
    
    def callPedidos(self):
        Pedidos(self.master)

'''root = Tk.Tk()
root.title('MENU')
app = MenuVenta(master=root)
app.mainloop()'''