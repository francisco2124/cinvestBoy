
#Si importa los componentes para utilizar los elemntos graficos
from PyQt5 import QtWidgets
#Importacion que permite desplegar mensajes emergentes
from PyQt5.QtWidgets import QMessageBox
#Se accede a todas las propiedades y elementos de la vista de registrar
from vistas.crear import Ui_crear
#Se accede a todas las propiedades y elementos del modelo
from modelos.modeloRegistro import Modelo_Registros

class Controlador_crear(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        print("soy la vista de crear:D")
        #Permite acceder desde una variable a los elemntos de la vista de registrar
        self.ui= Ui_crear()
        #Permite acceder desde una variable a los elemntos del modelo
        self.modelo =  Modelo_Registros()
        #Permite visualizar la vista al iniciar la ventana
        self.ui.setupUi(self)
        #Inicializa los componentes principales de la clase
        self.inicializarGui()


    def inicializarGui(self):
        #Realiza la vinculacion entre la funcion de valida info y el boton de guardar
        self.ui.pushButton_Guardar.clicked.connect(self.validarInfo)

    def validarInfo(self):
        #se valida que los camos no esten vacios
        #Si los campos no estan vacios de llama a la funcion guardar informacion
        #De lo contrario se manda un mensaje de alerta al usuario para ingresar
        #los datos faltantes
        if self.ui.textline_Tarea.text() != '':
             if self.ui.comboBox_Dia.currentText():
                 if self.ui.timeEdit_Hora.text() != '':
                     if self.ui.comboBox_Prioridad.currentText() != '':
                        print ('bien')
                        state = self.guardarInfo()
                        if state:
                            alerta = QMessageBox.information(self, 'Alerta', "Evento agregado exitosamente", QMessageBox.Ok)

        else :
            alerta = QMessageBox.information(self, 'Alerta', "Es necesario el nombre de la tarea", QMessageBox.Ok)

    def guardarInfo(self):
        #Se almacenan los datos ingresados por elusuario
        tareaT = self.ui.textline_Tarea.text()
        diaT = self.ui.comboBox_Dia.currentText()
        horaT =  self.ui.timeEdit_Hora.text()
        prioridadT = self.ui.comboBox_Prioridad.currentText()
        descripcionT = self.ui.textEdit_Descripcion.toPlainText()
        print(tareaT+'-'+diaT+'-'+horaT+'-'+prioridadT+'-'+descripcionT)
        states = False
        #Se llama a la funcion del modelo y se le pasan como parametros los datos ingresados
        state = self.modelo.crearRegistro(tareaT, diaT, horaT, prioridadT, descripcionT)
        return states


