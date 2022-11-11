from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.consultar import Ui_consultar

from modelos.modeloRegistro import Modelo_Registros





class Controlador_consultar(QtWidgets.QMainWindow):


    def __init__(self,tarea):
        super().__init__()
        print("soy la vista de consultar:D")
        self.tarea = tarea
        self.ui= Ui_consultar()
        self.modelo =  Modelo_Registros()
        self.ui.setupUi(self)
        self.InicializarGui()



    def InicializarGui(self):
        self.recuperarDatos()

    def recuperarDatos(self):
        tarea = self.modelo.consultarTareaEspecifica(self.tarea)
        datos = tarea[0]
        self.ui.label_2.setText("Tarea: "+str(datos[0]))
        self.ui.label_4.setText(str(datos[2]) + " - "+str(datos[4]))
        self.ui.label.setText(str(datos[1]))
        self.ui.label_7.setText("Prioridad: "+str(datos[3]))


        if str(datos[3]) == "Alta":
            self.ui.lbImagen.setStyleSheet("image: url(:/images/gatitoAsustado.jpg);")
        elif str(datos[3]) == "Media":
            self.ui.lbImagen.setStyleSheet("image: url(:/images/alta.png);")
        else:
            self.ui.lbImagen.setStyleSheet("image: url(:/images/gatoRelajado.jpg);")


        self.ui.textEdit.setText(str(datos[5]))
        print("Los datos son: "+str(tarea))