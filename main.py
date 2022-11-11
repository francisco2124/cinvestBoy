
#Codigos necesarios :D

# pyuic5 -x .ui -o .py


from PyQt5 import QtWidgets
from controladores.Controlador_Registros import Controlador_registros
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hola mundo, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    app = QtWidgets.QApplication(sys.argv)
    windowExample = Controlador_registros()
    windowExample.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
