from .conexion_db import ConexionDB

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
    
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
def borrar_tabla():
    conexion = ConexionDB()
    
    sql = '''DROP TABLE repuestos'''
    
    conexion.cursor.execute(sql)
    conexion.cerrar()