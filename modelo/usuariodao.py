from modelo.usuario import Usuario
from modelo.conexionbd import ConexionBD
import pyodbc # Necesario para referenciar pyodbc.Error

class UsuarioDAO:
    def __init__(self):
        self.bd = ConexionBD()
        self.usuario = Usuario()

    def ValidarUsuario(self):
        try:
            self.bd.establecerConexion()
            cursor = self.bd.conexion.cursor()
            sp = 'exec [dbo].[ValidarUsuario] @nombre=?, @contrasena=?'
            param = (self.usuario.user_name, self.usuario.contraseña)
            cursor.execute(sp, param)
            resultado = cursor.fetchone()

            if resultado is not None and resultado[0] == 1:
                return 1 
            else:
                return 0 

        except pyodbc.Error as ex:
            print(f"Error al validar usuario: {ex}")
            return 0 
            
        finally:
            if self.bd.conexion:
                self.bd.cerrarConexion()
