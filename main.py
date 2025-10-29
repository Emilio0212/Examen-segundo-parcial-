from PyQt5 import QtWidgets
import sys
from load.load_ui_productos import Load_ui_productos 
from load.load_ui_clientes import Load_ui_clientes
from load.load_ui_login import Load_ui_login
from load.load_ui_menu import Load_ui_menu

class ApplicationController:
    def __init__(self):
        self.login_win = Load_ui_login()
        self.menu_win = Load_ui_menu()
        self.clientes_win = Load_ui_clientes()
        self.productos_win = Load_ui_productos()

        self._conectar_ventanas()
        
        self.menu_win.hide()
        self.login_win.show()


    def _conectar_ventanas(self):
        # Conexión de Login
        self.login_win.ingresar.clicked.connect(self.validar_login) 
        
        # Conexiones del Menú
        self.menu_win.clientes.clicked.connect(self.show_clientes)
        self.menu_win.productos.clicked.connect(self.show_productos)
        
        # Cerra sesión
        self.menu_win.cerrar.clicked.connect(self.logout)
        
        # Conexiones de Retorno (Volver a Menú)
        self.clientes_win.volver.clicked.connect(lambda: self.show_menu_from_crud('clientes'))
        self.productos_win.volver.clicked.connect(lambda: self.show_menu_from_crud('productos'))
        
    
    def validar_login(self):
        v = self.login_win.buscar_Usuario()

        if v == 1:
            self.show_menu()
        else:
            print("Login fallido: Usuario no encontrado o contraseña incorrecta.")


    def show_menu(self):
        self.login_win.hide()
        self.menu_win.show()
           
    def logout(self):
  
        self.menu_win.hide()
        
        try:
             self.login_win.usuario.setText("")
             self.login_win.contrasena.setText("")
        except AttributeError:
             pass
             
        self.login_win.show()

    def show_clientes(self):
        self.menu_win.hide()
        self.clientes_win.show()

    def show_productos(self):
        self.menu_win.hide()
        self.productos_win.show()
        
    def show_menu_from_crud(self, source_window_id):      
        if source_window_id == 'clientes':
            self.clientes_win.hide()
        elif source_window_id == 'productos':
            self.productos_win.hide()
        self.menu_win.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = ApplicationController()
    sys.exit(app.exec_())
