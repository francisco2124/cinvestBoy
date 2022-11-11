#import pymysql
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
#from pymysql import  *
from sqlite3 import *
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton




class Modelo_Registros(QtWidgets.QMainWindow):

    def __init__(self):  
        self.connection2 = sqlite3.connect('Agenda.db')
        #print ("Opened database successfully")
        

    def cargarTabla(self):
        cursor = self.connection2.cursor()
        sql = "SELECT idRegistros, tarea, dia, prioridad, hora, descripcion FROM registros"
        cursor.execute(sql)        
        registro = cursor.fetchall()
        print(registro)   
        cursor.close()
        return registro

    def recuperarTareasXdia(self, dia):
        cursor = self.connection2.cursor()
        sql = "SELECT idRegistros, tarea, dia, prioridad, hora, descripcion  FROM registros where dia = '{}' ".format(dia)
        cursor.execute(sql)        
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def consultarTareaEspecifica(self, tarea):
        cursor = self.connection2.cursor()
        sql = "SELECT idRegistros, tarea, dia, prioridad, hora, descripcion FROM registros WHERE tarea = '{}'  ".format(tarea)
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro



    #Se reciven los valores ingresados por el usuario
    def crearRegistro(self, tareaT, diaT, horaT, prioridadT, descripcionT):
        #Se establece la conexión con la base de datos
        cursor = self.connection2.cursor()
        #Se realiza la sentencia sql que modificará la base de datos
        sql = """INSERT INTO registros(tarea, dia, prioridad, hora, descripcion) VALUES 
        ('{}', '{}', '{}', '{}', '{}')""".format( tareaT, diaT, horaT, prioridadT, descripcionT)
        true = True
        false = False
        #Sen envia la sentencia sql para agregar un nuevo registro.
        #En caso que falle se modifica una variable la cual avisar al usuario
        try:
            count = cursor.execute(sql)
            self.connection2.commit()
            cursor.close()
            state = true

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            state = false
        finally:
            #Se cierra la conexion con la base de datos
            if self.connection2:
                self.connection2.close()
                print("The SQLite connection is closed")
            return state
