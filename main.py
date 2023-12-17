'''Управляющий файл. По умолчанию открывается окно main_screen
и отслеживается открытие окон Encryption и Decryption
и выполнение всех встроенных в них функций'''

import sys
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from Decryption import Ui_Window_decr
from Encryption import Ui_Window_encr
from main_screen import Ui_MainWindow
from Shivrs.DES.Shifrator import DES_shifr
from Choose_fr_expl import Choose_fr_expl
from Shivrs.DES.Deshifrator import DES_deshif

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def open_Encryption():
    ''' Открывает окно Encryption и обрабатывает действия в нём'''
    
    global Encr_Window
    Encr_Window = QtWidgets.QMainWindow()
    ui = Ui_Window_encr()
    ui.setupUi(Encr_Window)
    MainWindow.close()
    Encr_Window.show()

    def open_Main():
        ''' Обработка нажатия на кнопку but_back
        Закрывает окно Encryption и возвращaется в main_screen'''

        Encr_Window.close()
        MainWindow.show()

    ui.but_back.clicked.connect(open_Main)

    def check_shifrator():
        '''Обработка нажатия на кнопку but_encrypt
        Взависимости от выбранного шифра шифрует файл и запоминает ключ'''

        iteam = ui.comboBox.currentText()

        if (iteam == "DES"):
            def show_key(key):
                '''Шифрует ключ под * и выводит его в окно pasw_out'''

                ui.pasw_out.setText('*' * len(key))

            global key
            key = DES_shifr()
            show_key(key)

    ui.but_encrypt.clicked.connect(check_shifrator)

    def copy_clipbord():
        '''Обработка нажатия на кнопку but_insert
        Копирует ключ в буфер обмена'''

        global key
        pyperclip.copy(str(key))

    ui.but_insert.clicked.connect(copy_clipbord)

    ui.but_exlor.clicked.connect(Choose_fr_expl)

def open_Decryption():
    ''' Открывает окно Decryption и обрабатывает действия в нём'''

    global Decr_Window
    Decr_Window = QtWidgets.QMainWindow()
    ui = Ui_Window_decr()
    ui.setupUi(Decr_Window)
    MainWindow.close()
    Decr_Window.show()

    def open_Main():
        ''' Обработка нажатия на кнопку but_back
        Закрывает окно Decryption и возвращaется в main_screen'''

        Decr_Window.close()
        MainWindow.show()

    ui.but_back.clicked.connect(open_Main)

    def check_shifrator():
        '''Обработка нажатия на кнопку but_decr
        Взависимости от выбранного шифра дешифрует файл'''

        iteam = ui.comboBox.currentText()

        if (iteam == "DES"):
            global key
            print(key)
            DES_deshif(key)

    ui.but_decr.clicked.connect(check_shifrator)

    def text_insert(passwrd):
        '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

        global key
        key = passwrd

    ui.key_insert.textChanged.connect(text_insert)

    def from_clipbord():
        '''Обработка нажатия на кнопку but_insert
        Вставляет ключ из буфера'''

        global key
        key = pyperclip.paste()
        ui.key_insert.setText(key)

    ui.but_insert.clicked.connect(from_clipbord)

    ui.but_exlor.clicked.connect(Choose_fr_expl)



ui.but_encr.clicked.connect(open_Encryption)
ui.but_decr.clicked.connect(open_Decryption)

sys.exit(app.exec_())
