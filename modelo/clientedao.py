from modelo.cliente import Cliente
from modelo.conexionbd import ConexionBD

class ClienteDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.cliente = Cliente()

    def listarClientes(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_listar_clientes]'
        cursor.execute(sp)
        filas = cursor.fetchall()
        self.bd.cerrarConexion()

        return filas

    def actualizarCliente(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_actualizar_cliente] @nombre=?, @telefono=?, @direccion=?, @correo=?'
        param = (self.cliente.nombre, self.cliente.telefono, self.cliente.direccion, self.cliente.correo)
        cursor.execute(sp, param)
        cursor.commit()
        self.bd.cerrarConexion()

    def eliminarCliente(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_eliminar_cliente] @nombre=?'
        param = (self.cliente.nombre)
        cursor.execute(sp, param)
        cursor.commit()
        self.bd.cerrarConexion()

    def insertarCliente(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_insertar_cliente] @nombre=?, @telefono=?, @direccion=?, @correo=?'
        param = (self.cliente.nombre, self.cliente.telefono, self.cliente.direccion, self.cliente.correo)
        cursor.execute(sp, param)
        cursor.commit()
        self.bd.cerrarConexion()

    def buscar_cliente(self):
        self.bd.establecerConexion()
        cursor = self.bd.conexion.cursor()
        sp = 'exec [dbo].[sp_buscar_cliente] @nombre=?'
        param = (self.cliente.nombre)
        cursor.execute(sp, param)
        filas = cursor.fetchall()
        self.bd.cerrarConexion()

        return filas