# ESTO ES EL INTERFACE DE USUARIO

import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 480, height= 320)
        self.root = root
        self.pack()
        
        self.campos_repuestos()
        
    def campos_repuestos(self):
        #LABEL DE CADA CAMPO
        self.label_codigo = tk.Label(self, text= 'Codigo: ')
        self.label_codigo.config(font= ('Arial', 12, 'bold'))
        self.label_codigo.grid(row= 0, column= 0, padx= 10, pady= 10)
        
        self.label_articulo = tk.Label(self, text= 'Articulo: ')
        self.label_articulo.config(font= ('Arial', 12, 'bold'))
        self.label_articulo.grid(row= 1, column= 0, padx= 10, pady= 10)
        
        self.label_stock = tk.Label(self, text= 'Stock: ')
        self.label_stock.config(font= ('Arial', 12, 'bold'))
        self.label_stock.grid(row= 2, column= 0, padx= 10, pady= 10)
        
        self.label_precio = tk.Label(self, text= 'Precio: ')
        self.label_precio.config(font= ('Arial', 12, 'bold'))
        self.label_precio.grid(row= 3, column= 0, padx= 10, pady= 10)
        
        #ENTRYS DE LABELS
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.config(width= 50, font= ('Arial', 12))
        self.entry_codigo.grid(row= 0, column= 1)
        
        self.entry_articulo = tk.Entry(self)
        self.entry_articulo.config(width= 50, font= ('Arial', 12))
        self.entry_articulo.grid(row= 1, column= 1)
        
        self.entry_stock = tk.Entry(self)
        self.entry_stock.config(width= 50, font= ('Arial', 12))
        self.entry_stock.grid(row= 2, column= 1)
        
        self.entry_precio = tk.Entry(self)
        self.entry_precio.config(width= 50, font= ('Arial', 12))
        self.entry_precio.grid(row= 3, column= 1)