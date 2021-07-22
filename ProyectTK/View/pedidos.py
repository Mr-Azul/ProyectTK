from tkinter import ttk
import tkinter as Tk
from tkinter import messagebox
from tkinter import *
from Models.pedidosDB import *
from reportlab.pdfgen import canvas
from View.pedidosPDF import *
from tkdocviewer import *

class Pedidos:
	def __init__(self, window):
		self.wind = window
		self.wind.title('Lista de Pedidos')
		self.wind.geometry('1010x710+250+50')
		self.wind.config(background='#314252')
		self.createFrameLabel()
		self.createFrames()
		self.createEntrys()
		self.createButtons()
		self.createList()

	def createFrameLabel(self):
		self.framel = LabelFrame(self.wind, text='', font=('Arial, 12'), bg='#314252', fg='white', bd='5')
		self.framel.place(x=60, y=30)

	def createFrames (self):
		self.framec = Label(self.framel, fg='white', bg='#314252', text='Empleado:   ', font='10').grid(row=0, column=0)
		self.framec = Label(self.framel, fg='white', bg='#314252', text='Cliente:    ', font='10').grid(row=1, column=0)
		self.framec = Label(self.framel, fg='white', bg='#314252', text='Producto:    ', font='10').grid(row=2, column=0)
		self.framec = Label(self.framel, fg='white', bg='#314252', text='Descripción:', font='10').grid(row=3, column=0)
		self.framec = Label(self.framel, fg='white', bg='#314252', text='Teléfono:   ', font='10').grid(row=4, column=0)

	def createEntrys(self):
		self.code = StringVar()
		self.name = StringVar()
		self.supp = StringVar()
		self.price = StringVar()
		self.cant = StringVar()
		self.txt_code = Entry(self.framel, font=('Arial', 12), relief = 'flat', bg='#E7E7E7', textvariable=self.code).grid(row=0, column=1)
		self.txt_name = Entry(self.framel, font=('Arial', 12), relief = 'flat', bg='#E7E7E7', textvariable=self.name).grid(row=1, column=1)
		self.txt_supp = Entry(self.framel, font=('Arial', 12), relief = 'flat', bg='#E7E7E7', textvariable=self.supp).grid(row=2, column=1)
		self.txt_price = Entry(self.framel, font=('Arial', 12), relief = 'flat',bg='#E7E7E7', textvariable=self.price).grid(row=3, column=1)
		self.txt_cant = Entry(self.framel, font=('Arial', 12), relief = 'flat', bg='#E7E7E7', textvariable=self.cant).grid(row=4, column=1)

	def createButtons(self):
		self.btn_register = Button(self.framel, text='Registrar Pedido', fg='white', borderwidth=2, relief='flat', cursor='hand1', overrelief='raise', bg='#0051C8', command = lambda: self.registerProd()).grid(row=5, columnspan=2, sticky=W+E)
		self.btn_cancel = Button(self.framel, text='Cancelar Registro', fg='white', borderwidth=2, relief='flat', cursor='hand1', overrelief='raise', bg='#E81123', command = lambda: self.detainProcess()).grid(row=6, columnspan=2, sticky=W+E)
		self.btn_pdf = Button(self.framel, text='PDF', fg='white', borderwidth=2, relief='flat', cursor='hand1', overrelief='raise', bg='purple', command = lambda: self.drawPDF()).grid(row=7, columnspan=2, sticky=W+E)
		self.btn_close = Button(self.wind, text='Salir', fg='white', borderwidth=2, relief='flat', cursor='hand1', overrelief='raise', bg='black', command = lambda:self.closeWind()).place(x=900, y=240, width=100)
			
	def createList(self):
		self.list_elements = ttk.Treeview(self.wind, height=20, columns=("col1", "col2", "col3", "col4", "col5"))
		# Style
		style = ttk.Style()
		style.theme_use('clam')
		style.configure('Treeview.Heading', background='#0051C8', relief='flat', foreground='white')
		style.map('Treeview', background=[('selected', 'pink')], foreground=[('selected', 'black')])
		self.list_elements.heading('#0', text='ID')
		self.list_elements.heading('col1', text='Empleado')
		self.list_elements.heading('col2', text='Cliente')
		self.list_elements.heading('col3', text='Producto')
		self.list_elements.heading('col4', text='Descripción')
		self.list_elements.heading('col5', text='Teléfono')
		self.list_elements.column('#0', anchor=CENTER, width=60)
		self.list_elements.column('col1', anchor=CENTER, width=220)
		self.list_elements.column('col2', anchor=CENTER, width=220)
		self.list_elements.column('col3', anchor=CENTER, width=150)
		self.list_elements.column('col4', anchor=CENTER, width=250)
		self.list_elements.column('col5', anchor=CENTER, width=110)
		self.list_elements.bind("<Double 1>", self.getRow)	#DoubleClick Event
		#Insert table
		d = DataPedidos()
		self.rows = d.returnAllElements()
		for i in self.rows:
			self.list_elements.insert('', 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5]))
		self.list_elements.place(x=0, y=280)
		
	def getRow(self, event):
		self.co = StringVar()
		self.na = StringVar()
		self.sup = StringVar()
		self.pre = StringVar()
		self.ca = StringVar()
		rowName = self.list_elements.identify_row(event.y)
		item = self.list_elements.item(self.list_elements.focus())
		c = item ['values'][0]
		n = item ['values'][1]
		s = item ['values'][2]
		p = item ['values'][3]
		cc = item ['values'][4]
		self.co.set(c)
		self.na.set(n)
		self.sup.set(s)
		self.pre.set(p)
		self.ca.set(cc)
		self.pop = Toplevel(self.wind)
		self.pop.title('Menu de cambios')
		#pop.geometry('320x260')
		#Codigo
		Label(self.pop, text='Empleado: ', font=('Arial', 14)).grid(row=0, column=0)
		Entry(self.pop, textvariable=self.co, font=('Arial', 13), relief='flat').grid(row=0, column=1)
		#Nombre 
		Label(self.pop, text='Cliente: ', font=('Arial', 14)).grid(row=1, column=0)
		Entry(self.pop, textvariable=self.na,font=('Arial', 13)).grid(row=1, column=1)
		#Proveedor 
		Label(self.pop, text='Producto: ', font=('Arial', 14)).grid(row=3, column=0)
		Entry(self.pop, textvariable=self.sup, font=('Arial', 13)).grid(row=3, column=1)
		#Precio 
		Label(self.pop, text='Descripción: ', font=('Arial', 14)).grid(row=5, column=0)
		Entry(self.pop, textvariable=self.pre, font=('Arial', 13)).grid(row=5, column=1)
		#Stock 
		Label(self.pop, text='Teléfono: ', font=('Arial', 14)).grid(row=7, column=0)
		Entry(self.pop, textvariable=self.ca, font=('Arial', 13)).grid(row=7, column=1)
		#Buttons Pop
		bnt_update= Button(self.pop, text='Guardar Cambios', relief='flat', background='#00CE54', foreground='white', 
		command = lambda: self.editarRow(n, self.co.get(), self.na.get(), self.sup.get(), self.pre.get(), self.ca.get()) ).grid(row=9, column=0, sticky=W+E)
		bnt_delete= Button(self.pop, text='Eliminar', relief='flat', background='red', foreground='white', command = lambda: self.deleteRow(n)).grid(row=9, column=1, sticky=W+E)
	
	def validateEdit(self):
		if(len(self.co.get())>0 and len(self.na.get())>0 and len(self.sup.get())>0 and len(self.pre.get())>0 and len(self.ca.get())>0):
			return True
		else:
			return False
		
	def deleteRow(self, n):
		d = DataPedidos()
		r = messagebox.askquestion(title='Atención', message='Desea eliminar el registro seleccionado')
		if r == messagebox.YES:
			d.delete(n)
			messagebox.showinfo(title='Informe', message='Datos actualizados')
			self.pop.destroy()
		else:
			self.pop.destroy()
		self.emptyList()
		self.createList()
		self.emptyEntry()
		
		
	
	def editarRow(self, n, co, na, sup, pre, ca):
		if(self.validateEdit()):
			co = self.co.get()
			na = self.na.get()
			sup = self.sup.get()
			pre = self.pre.get()
			ca = self.ca.get()
			arr = [co, na, sup, pre, ca]
			d = DataPedidos()
			d.updateItem(arr, n)
			self.emptyList()
			self.createList()
			self.emptyEntry()
			messagebox.showinfo(title='Informe', message='Datos actualizados')
			self.pop.destroy()
			
		else:
			messagebox.showinfo(title='Informe', message='Campos Incompletos')
			self.pop.destroy()

	def emptyList(self):
		self.list_elements.delete(*self.list_elements.get_children())

	def emptyEntry(self):
		self.code.set('')
		self.name.set('')
		self.supp.set('')
		self.price.set('')
		self.cant.set('')

	def registerProd(self):
		code = self.code.get()
		name = self.name.get()
		supp = self.supp.get()
		price = self.price.get()
		cant = self.cant.get()
		if self.code.get()!='' and self.name.get()!='' and self.supp.get()!='' and self.price.get()!='' and self.cant.get()!='':
			d = DataPedidos()
			d.insertItems(code, name, supp, price, cant)
			self.emptyList()
			self.createList()
			self.emptyEntry()
			messagebox.showinfo(title='Atencion', message='Nuevo Pedido Registrado')
		else:
			messagebox.showinfo(title='Error', message='Campos incompletos')

	def detainProcess(self):
		self.emptyEntry()

	def drawPDF(self):
		d = DataPedidos()
		self.inst = d.returnAllElements()
		list=[]
		file_name = 'pedidos.pdf'
		for i in self.inst:
			list.append(i)
		ReportPdf(list, file_name)
		pdf_wind = Toplevel()
		v = DocViewer(pdf_wind)
		v.pack(side="top", expand=1, fill="both")
		v.display_file(file_name)
		
	def closeWind(self):
		self.wind.destroy()