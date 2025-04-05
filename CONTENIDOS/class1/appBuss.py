from laptoBussines import Lapto_Business
import tkinter as tk
from tkinter import ttk
from PIL  import Image, ImageTk
import random

class AppBuss : 
    def __init__(self,root):
        self.root= root
        self.laptos = []
        self.imagenes = [
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\imgBuss\\1.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\imgBuss\\2.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\imgBuss\\3.png',
            'C:\\Users\\HP\\Documents\\Programación_Jhonatan\\Modulo5\\CONTENIDOS\\class1\\imgBuss\\4.png']
        
        root.title('Ingresar datos')
        
        self.setup_iu()
        
    def setup_iu (self):
        ttk.Label(self.root, text='Marca').grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.marca).grid(row=0,column=1)
        
        ttk.Label(self.root, text='Procesador').grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.procesador).grid(row=1,column=1)
        
        ttk.Label(self.root, text='Espacio Disco').grid(row=2,column=0)
        self.espacioDisco = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.espacioDisco).grid(row=2,column=1)
        
        ttk.Label(self.root, text='Duracio Bateria').grid(row=3,column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.duracion_bateria).grid(row=3,column=1)
        
        ttk.Label(self.root, text='MEMORIA').grid(row=4,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.memoria).grid(row=4,column=1)
        
        ttk.Label(self.root, text='COSTO').grid(row=5,column=0)
        self.costo = tk.StringVar()
        ttk.Entry(self.root,textvariable=self.costo).grid(row=5,column=1)
        
        ttk.Button(self.root,text='AGREGAR LAPTOP',command=self.agregarLaptop).grid(row=6,column=1)
        
        self.mostrar_laptos = tk.Text(self.root,height=10, width=50)
        self.mostrar_laptos.grid(row=7,column=1,columnspan=2)
        self.canva = tk.Canvas(self.root,width=200,height=200)
        self.canva.grid(row=1,column=3,rowspan=7)  
        
    def agregarLaptop(self):
        nuevaLapto = Lapto_Business (self.marca.get(),self.procesador.get(),self.espacioDisco.get(),
                                    self.duracion_bateria.get(),self.memoria.get(),self.costo.get())
        self.laptos.append(nuevaLapto)
        self.mostrar_laptos.insert( tk.END, f'{nuevaLapto}')
        self.mostrarImagenes()
        
    def mostrarImagenes (self):
        imagen_path  = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200),Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        self.canva.create_image(0,0,anchor= tk.NW,image= photo)
        self.canva.image = photo
        pass
    

root = tk.Tk()
app = AppBuss(root)
root.mainloop()