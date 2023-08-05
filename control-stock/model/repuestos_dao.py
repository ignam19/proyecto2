from .conexion_db import ConexionDB
from tkinter import messagebox  

def crear_tabla():
    
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE repuestos(
        id_repuestos INTEGER,
        codigo VARCHAR(50),
        articulo VARCHAR(100),
        stock INTEGER,
        precio INTEGER,
        PRIMARY KEY(id_repuestos AUTOINCREMENT)
    )
    '''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos.'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya existe.'
        messagebox.showwarning(titulo, mensaje)
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = '''DROP TABLE repuestos'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'Se borro la tabla con exito.'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No existe tabla para borrar.'
        messagebox.showerror(titulo, mensaje)
        
        
class Repuesto:
    def __init__(self, codigo, articulo, stock, precio):
        self.id_repuesto = None
        self.codigo = codigo
        self.articulo = articulo
        self.stock = stock
        self.precio = precio
        
    def __str__(self):
        return f'Repuesto[{self.codigo}, {self.articulo}, {self.stock}, {self.precio}]'
    
    
def guardar(repuesto):
    conexion = ConexionDB()
    
    sql = f'''INSERT INTO repuestos(codigo, articulo, stock, precio) 
    VALUES('{repuesto.codigo}', '{repuesto.articulo}', '{repuesto.stock}', '{repuesto.precio}')'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion Registro'
        mensaje = 'No se ha podido insertar la tabla, el registro no existe.'
        messagebox.showerror(titulo, mensaje)
        

def listar():
    
    conexion = ConexionDB()
    
    lista_repuestos = []
    
    sql = 'SELECT * FROM repuestos'
    
    try:
        conexion.cursor.execute(sql)
        lista_repuestos = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Debes crear una tabla en la base de datos.'
        messagebox.showwarning(titulo, mensaje)
        
        
    return lista_repuestos