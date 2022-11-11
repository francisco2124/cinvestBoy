
#Si importa los componentes para utilizar los elemntos graficos
from PyQt5 import QtWidgets
#Importacion que permite desplegar mensajes emergentes
from PyQt5.QtWidgets import QMessageBox
#Se accede a todas las propiedades y elementos de la vista de registrar
from vistas.registro import Ui_registros
#Se accede a todas las propiedades y elementos de la vista principal
from controladores.Controlador_Consultar import Controlador_consultar
from controladores.Controlador_Crear import Controlador_crear

from modelos.modeloRegistro import Modelo_Registros


class Controlador_registros(QtWidgets.QMainWindow):


    def __init__(self):
        super().__init__()
        print("soy la vista de registros :D")
        self.ui= Ui_registros()
        self.modelo =  Modelo_Registros()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.ui.comboBox_Dia.currentIndexChanged[str].connect(self.cargarTareas)


    def InicializarGui(self):
        self.recuperarDatos()
        self.ui.commandLinkButton_Consultar.clicked.connect(self.consultarTarea)
        self.ui.commandLinkButton_Crear.clicked.connect(self.abrirCrear)

    def recuperarDatos(self):

        datos = self.modelo.cargarTabla()
        print(datos)
        print("cargar Reportes")
        i = len(datos)
        self.ui.tableView.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tableView.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableView.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableView.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableView.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableView.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))

            tablerow +=1

    def cargarTareas(self):
        print(self.ui.comboBox_Dia.currentText())
        if self.ui.comboBox_Dia.currentText() == "Todas las tareas":
            self.recuperarDatos()
        else:
            tarea = self.modelo.recuperarTareasXdia(self.ui.comboBox_Dia.currentText())
            print(tarea)

            try:

                i = len(tarea)
                self.ui.tableView.setRowCount(i)
                tablerow = 0
                for row in tarea:
                    self.ui.tableView.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
                    self.ui.tableView.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
                    self.ui.tableView.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
                    self.ui.tableView.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
                    self.ui.tableView.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))

                    tablerow +=1

            except:
                filTareas = "-"
            #print(tarea[0])

    def consultarTarea(self):

        RowTable = self.ui.tableView.currentRow()

        if RowTable != -1:
            item = self.ui.tableView.item(RowTable, 0)
            print(item.text())

            self.abrir = Controlador_consultar(item.text())
            self.abrir.show()

        else:
            alerta = QMessageBox.information(self, 'Alerta', "No has seleccionado una tarea", QMessageBox.Ok)

    def abrirCrear(self):
        self.abrir = Controlador_crear()
        self.abrir.show()





