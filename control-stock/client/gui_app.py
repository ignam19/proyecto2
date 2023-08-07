# ESTO ES EL INTERFACE DE USUARIO
import tkinter as tk
from tkinter import ttk, messagebox
from model.repuestos_dao import crear_tabla, borrar_tabla, Repuesto, guardar, listar, editar, eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu= barra_menu, width= 300, height= 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label= 'Inicio', menu= menu_inicio)
    
    menu_inicio.add_cascade(label= 'Crear Registro DB', command= crear_tabla)
    menu_inicio.add_cascade(label= 'Borrar Registro DB', command= borrar_tabla)
    

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 480, height= 320)
        self.root = root
        self.pack()
        self.id_repuesto = None
        
        self.campos_repuestos()
        
        self.tabla_repuestos()
        
       
        
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
        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable= self.mi_codigo)
        self.entry_codigo.config(width= 30, font= ('Arial', 12))
        self.entry_codigo.grid(row= 0, column= 1, padx= 5, pady= 5)
        
        self.mi_articulo = tk.StringVar()
        self.entry_articulo = tk.Entry(self, textvariable= self.mi_articulo)
        self.entry_articulo.config(width= 30, font= ('Arial', 12))
        self.entry_articulo.grid(row= 1, column= 1, padx= 5, pady= 5)
        
        self.mi_stock = tk.StringVar()
        self.entry_stock = tk.Entry(self, textvariable= self.mi_stock)
        self.entry_stock.config(width= 30, font= ('Arial', 12))
        self.entry_stock.grid(row= 2, column= 1, padx= 5, pady= 5)
        
        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable= self.mi_precio)
        self.entry_precio.config(width= 30, font= ('Arial', 12))
        self.entry_precio.grid(row= 3, column= 1, padx= 5, pady= 5)
        
        #BOTONES
        self.boton_guardar = tk.Button(self, text= 'Guardar', command= self.guardar)
        self.boton_guardar.config(width= 20, font= ('Arial', 12, 'bold'),
                                fg= '#DAD5D6', bg= '#158645', cursor= 'hand2')
        self.boton_guardar.grid(row= 0, column= 2, padx= 10, pady= 10)
        
        self.boton_limpiar = tk.Button(self, text= 'Limpiar', command= self.limpiar)
        self.boton_limpiar.config(width= 20, font= ('Arial', 12, 'bold'),
                                fg= '#DAD5D6', bg= '#038BBB', cursor= 'hand2')
        self.boton_limpiar.grid(row= 1, column= 2, padx= 10, pady= 10)
        
        self.boton_modificar = tk.Button(self, text= 'Modificar', command= self.modificar)
        self.boton_modificar.config(width= 20, font= ('Arial', 12, 'bold'),
                                fg= '#DAD5D6', bg= '#F6AA3D', cursor= 'hand2')
        self.boton_modificar.grid(row= 2, column= 2, padx= 10, pady= 10)
        
        self.boton_eliminar = tk.Button(self, text= 'Eliminar', command= self.eliminar_datos)
        self.boton_eliminar.config(width= 20, font= ('Arial', 12, 'bold'),
                                fg= '#DAD5D6', bg= '#FF1F4C', cursor= 'hand2')
        self.boton_eliminar.grid(row= 3, column= 2, padx= 10, pady= 10)
        
        
    def guardar(self):
        
        repuesto = Repuesto(
            self.mi_codigo.get(),
            self.mi_articulo.get(),
            self.mi_stock.get(),
            self.mi_precio.get()
        )
        
        if self.id_repuesto == None:
            guardar(repuesto)
        else:
            editar(repuesto, self.id_repuesto)
        
        self.tabla_repuestos()
            
        #Limpiar campos
        self.limpiar()
        
    def limpiar(self):
        self.id_repuesto = None
        self.mi_codigo.set('')
        self.mi_articulo.set('')
        self.mi_stock.set('')
        self.mi_precio.set('')
            
    
    def tabla_repuestos(self):
        
        self.lista_repuestos = listar()
        self.lista_repuestos.reverse()
        
        self.tabla = ttk.Treeview(self,
        columns= ('Codigo', 'Articulo', 'Stock', 'Precio'))
        self.tabla.grid(row= 4, column= 0, columnspan= 5, sticky= 'nse')
        
        #Scrollbar
        self.scroll = ttk.Scrollbar(self, 
        orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row= 4, column= 5, sticky= 'nse') 
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text= 'ID')
        self.tabla.heading('#1', text= 'CODIGO')
        self.tabla.heading('#2', text= 'ARTICULO')
        self.tabla.heading('#3', text= 'STOCK')
        self.tabla.heading('#4', text= 'PRECIO')
        
        #Iterador de lista
        for p in self.lista_repuestos:
            self.tabla.insert('', 0, text= p[0],
            values= (p[1], p[2], p[3], p[4]))
            
    def modificar(self):
        
        try:
            #Recuperar los datos de la tabla
            self.id_repuesto = self.tabla.item(
                self.tabla.selection())['text']
            self.codigo_repuesto = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.articulo_repuesto = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.stock_repuesto = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.precio_repuesto = self.tabla.item(
                self.tabla.selection())['values'][3]
            
            
            #Cargar los entrys
            self.entry_codigo.insert(0, self.codigo_repuesto)
            self.entry_articulo.insert(0, self.articulo_repuesto)
            self.entry_stock.insert(0, self.stock_repuesto)
            self.entry_precio.insert(0, self.precio_repuesto)  
            
            
              
            
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No ha seleccionado ningun registro.'
            messagebox.showerror(titulo, mensaje)
            
            
    def eliminar_datos(self):
        
        try:
            self.id_repuesto = self.tabla.item(
                self.tabla.selection())['text']
            eliminar(self.id_repuesto)
            
            self.tabla_repuestos()
            self.id_repuesto = None
        except:
            titulo = 'Eliminacion de datos'
            mensaje = 'No ha seleccionado ningun registro..'
            messagebox.showerror(titulo, mensaje)
        