from modelo.conexionbd import ConexionBD
from modelo.producto import Producto 

class ProdcutoDAO():
    def __init__(self):
        self.bd = ConexionBD()
        self.producto = Producto()

    def listarproducto(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_listar_productos]"
        cursor.execute(sp)
        filas =cursor.fetchall()
        self.bd.cerrarConexion()
        return filas

    def guardarProducto(self):
        self.bd = ConexionBD()
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_insertar_producto] @clave=?, @descripcion=?, @existencia=?, @precio=?"
        param =(self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio)
        cursor.execute(sp,param)
        cursor.commit()
        self.bd.cerrarConexion

    def actualizarProducto(self):
        self.bd = ConexionBD()
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_actualizar_producto] @id_producto=?,@clave=?, @descripcion=?, @existencia=?, Qprecio=?"
        param = (self.producto.id_producto,self.producto.clave,self.producto.descripcion,self.producto.existencia,self.producto.precio)
        cursor.execute(sp,param)
        cursor.commit()
        self.bd.cerrarConexion()

    def eliminarProdcuto(self):
        self.bd = ConexionBD()
        self.bd.establecerConexion
        cursor = self.bd.conexion.cursor()
        sp = "exec [dbo].[sp_eliminar_producto] @id_producto=?"
        param =(self.producto.id_producto)
        cursor.execute(sp,param)
        cursor.commit()
        self.bd.cerrarConexion