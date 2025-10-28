import pyodbc


class ConexionBD():
    def __init__(self):
        self.conexion = ""

    def establecerConexion(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=SALAF008-12\SQLEXPRESS;DATABASE=bdsistema;UID=sa;PWD=Password01')
            print('Conexion establecida')
        except Exception as ex:
            print('No se pudo establecer la conexion')
            print("Error=" * str(ex))


    def cerrarConexion(self):
        self.conexion.close()