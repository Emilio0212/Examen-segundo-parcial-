import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from modelo.usuariodao import UsuarioDAO

class Load_ui_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_loggin.ui", self)
        self.show()
        self.usuariodao = UsuarioDAO()

        self.ingresar.clicked.connect(self.buscar_Usuario)

    def buscar_Usuario(self):
        self.usuariodao.usuario.user_name = self.usuario.text().strip()
        self.usuariodao.usuario.contraseña = self.contrasena.text().strip()

        resultado_validacion = self.usuariodao.ValidarUsuario()
        return resultado_validacion