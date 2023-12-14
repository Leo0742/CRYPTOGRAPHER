import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Decryption import Ui_Window_decr
from Encryption import Ui_Window_encr
from main_screen import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def open_Encryption():
    global Encr_Window
    Encr_Window = QtWidgets.QMainWindow()
    ui = Ui_Window_encr()
    ui.setupUi(Encr_Window)
    MainWindow.close()
    Encr_Window.show()

    def open_Main():
        Encr_Window.close()
        MainWindow.show()

    ui.but_back.clicked.connect(open_Main)


def open_Decryption():
    global Decr_Window
    Decr_Window = QtWidgets.QMainWindow()
    ui = Ui_Window_decr()
    ui.setupUi(Decr_Window)
    MainWindow.close()
    Decr_Window.show()

    def open_Main():
        Decr_Window.close()
        MainWindow.show()

    ui.but_back.clicked.connect(open_Main)



ui.but_encr.clicked.connect(open_Encryption)
ui.but_decr.clicked.connect(open_Decryption)

sys.exit(app.exec_())
