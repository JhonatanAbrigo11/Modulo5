from laptopGaming import Laptop_Gaming
import tkinter as tk
from tkinter import ttk
from PIL  import Image, ImageTk
import random

class App : 
    def __init__(self,root):
        self.root = root
        self.laptos = []
        self.imagenes = [
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\img\\1.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\img\\2.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\img\\3.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\img\\4.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\img\\5.png' ]
        
        root.title('Ingresar datos')
        
        self.setup_ui()
        
    def setup_ui(self):
        ttk.Label(self.root,text='MARCA').grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)
        
        ttk.Label(self.root,text='Procesador').grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)
        
        ttk.Label(self.root,text='Memoria').grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=2,column=1)
        
        ttk.Label(self.root,text='Tarjeta Grafica').grid(row=3,column=0)
        self.tarjet_graf = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.tarjet_graf).grid(row=3,column=1)
        
        ttk.Label(self.root,text='Precio').grid(row=4,column=0)
        self.precio = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.precio).grid(row=4,column=1)
        
        ttk.Button(self.root,text='Agregar Laptop',command= self.agregarLaptop).grid(row=5,column=0)
        
        self.mostrar_laptos = tk.Text(self.root,height=10, width=50)
        self.mostrar_laptos.grid(row=6,column=1,columnspan=2)
        
        self.canva = tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=6)    
    def agregarLaptop(self):
        nuevaLaptop = Laptop_Gaming(self.marca.get(),self.procesador.get(),
        self.memoria.get(),self.tarjet_graf.get(),self.precio.get())
        self.laptos.append(nuevaLaptop)
        
        self.mostrar_laptos.insert( tk.END, f'{nuevaLaptop}')
        self.mostrar_imagen_aleatorio()
    def mostrar_imagen_aleatorio(self):
        imagen_path  = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0,anchor= tk.NW,image= photo)
        self.canva.image = photo
        
        pass
     
    
    
root = tk.Tk()
app = App(root)
root.mainloop()