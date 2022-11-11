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



