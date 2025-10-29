import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, uic  
from modelo.clientedao import ClienteDAO

class Load_ui_clientes(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_clientes.ui", self)
        self.show()
        self.clientedao = ClienteDAO()

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.boton_salir.clicked.connect(lambda: self.close())
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        self.boton_menu.clicked.connect(self.mover_menu)
        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tabla_consulta.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Conectar botones a funciones

        self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
        self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

        self.accion_guardar.clicked.connect(self.guardar_cliente)
        self.accion_actualizar.clicked.connect(self.actualizar_cliente)
        self.accion_eliminar.clicked.connect(self.eliminar_cliente)
        self.accion_limpiar.clicked.connect(self.limpiar_cliente)

        self.buscar_actualizar.clicked.connect(self.buscar_cliente_actualizar)
        self.buscar_eliminar.clicked.connect(self.buscar_cliente_eliminar)
        self.buscar_buscar.clicked.connect(self.buscar_cliente_buscar)
        self.boton_refresh.clicked.connect(self.actualizar_tabla)

    # Operaciones con el modelo de datos  
    def actualizar_tabla(self):
        datos = self.clientedao.listarClientes()
        self.tabla_consulta.setRowCount(len(datos))
        fila = 0
        for item in datos:
            self.tabla_consulta.setItem(fila,0, QtWidgets.QTableWidgetItem(str(item[1])))
            self.tabla_consulta.setItem(fila,1, QtWidgets.QTableWidgetItem(str(item[2])))
            self.tabla_consulta.setItem(fila,2, QtWidgets.QTableWidgetItem(str(item[3])))
            self.tabla_consulta.setItem(fila,3, QtWidgets.QTableWidgetItem(str(item[4])))
            fila += 1

    def guardar_cliente(self):
        self.clientedao.cliente.nombre = self.nombre_agregar.text()
        self.clientedao.cliente.telefono = self.telefono_agregar.text()
        self.clientedao.cliente.direccion = self.direccion_agregar.text()
        self.clientedao.cliente.correo = self.correo_agregar.text()

        self.clientedao.insertarCliente()

    def actualizar_cliente(self):
        self.clientedao.cliente.nombre = self.nombre_actualizar.text()
        self.clientedao.cliente.telefono = self.telefono_actualizar.text()
        self.clientedao.cliente.direccion = self.direccion_actualizar.text()
        self.clientedao.cliente.correo = self.correo_actualizar.text()

        print(f"Nombre a buscar (WHERE): {self.clientedao.cliente.nombre}")
        print(f"Nuevos datos: Tel={self.clientedao.cliente.telefono}, Dir={self.clientedao.cliente.direccion}, Correo={self.clientedao.cliente.correo}")

        self.clientedao.actualizarCliente()
        
    def eliminar_cliente(self):
        self.clientedao.cliente.nombre = self.nombre_agregar.text()
        self.clientedao.cliente.telefono = self.telefono_agregar.text()
        self.clientedao.cliente.direccion = self.direccion_agregar.text()
        self.clientedao.cliente.correo = self.correo_agregar.text()

        self.clientedao.eliminarCliente()

    def limpiar_cliente(self):
        self.nombre_buscar.setText('')
        self.telefono_buscar.setText('')
        self.direccion_buscar.setText('')
        self.correo_buscar.setText('')

    def buscar_cliente_actualizar(self):
        self.clientedao.cliente.nombre = self.nombre_actualizar.text()
        datos = self.clientedao.buscar_cliente()
        self.tabla_consulta.setRowCount(len(datos))
        if len(datos) > 0:
            self.telefono_actualizar.setText(datos[0][1])
            self.direccion_actualizar.setText(datos[0][2])
            self.correo_actualizar.setText(datos[0][3])
        else:
            pass

    def buscar_cliente_eliminar(self):
        self.clientedao.cliente.nombre = self.nombre_eliminar.text()
        datos = self.clientedao.buscar_cliente()
        self.tabla_consulta.setRowCount(len(datos))
        if len(datos) > 0:
            self.telefono_eliminar.setText(str(datos[0][1]))
            self.direccion_eliminar.setText(str(datos[0][2]))
            self.correo_eliminar.setText(str(datos[0][3]))
        
        else:
            pass

    def buscar_cliente_buscar(self):
        self.clientedao.cliente.nombre= self.nombre_buscar.text()
        datos = self.clientedao.buscar_cliente()
        self.tabla_consulta.setRowCount(len(datos))
        if len(datos) > 0:
            self.telefono_buscar.setText(str(datos[0][1]))
            self.direccion_buscar.setText(str(datos[0][2]))
            self.correo_buscar.setText(str(datos[0][3]))
            
        else:
            pass
        
       
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()
            
 
    def mover_menu(self):
        if True:			
            width = self.frame_lateral.width()
            widthb = self.boton_menu.width()
            normal = 0
            if width==0:
                extender = 200
                self.boton_menu.setText("Menú")
            else:
                extender = normal
                self.boton_menu.setText("")
                
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            
            self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
        
            self.animacionb.setStartValue(width)
            self.animacionb.setEndValue(extender)
            self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacionb.start()