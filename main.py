'''Управляющий файл. По умолчанию открывается окно main_screen
и отслеживается открытие окон Encryption и Decryption
и всплывающего окна Error и выполнение всех встроенных в них функций'''

import atexit
import os.path
import sys
import pyperclip
from PyQt5 import QtWidgets
from Program_windows.Decryption import Ui_Window_decr
from Program_windows.Encryption import Ui_Window_encr
from Program_windows.main_screen import Ui_MainWindow
from Shivrs.AES.Shifrator import AES_shifr
from Choose_fr_expl import Choose_fr_expl
from Shivrs.AES.Deshifrator import AES_deshif
from Program_windows.Error import Ui_error_window

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

        try:
            iteam = ui.shifrs.currentText()

            if (iteam == "AES"):
                def show_key(key):
                    '''Шифрует ключ под * и выводит его в окно pasw_out'''

                    ui.key_label.setText('*' * len(key))


                AES_shifr()

                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()

                show_key(key)

        except:
            '''Появится всплывающие окно Error, которое предупредит об ошибке
             и предложит методы её решения'''

            global Error_Window

            Error_Window = QtWidgets.QMessageBox()
            ui_1 = Ui_error_window()
            ui_1.setupUi(Error_Window)
            Error_Window.setText("Сейчас выполнить данное действие невозможно !")
            Error_Window.setInformativeText("Выберите файл для шифрования")
            Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его")

            Error_Window.show()

    ui.but_encr.clicked.connect(check_shifrator)

    def copy_clipbord():
        '''Обработка нажатия на кнопку but_insert
        Копирует ключ в буфер обмена'''

        file = open("Files/key.txt", 'r')
        key = file.read()
        file.close()

        if key == '':
            '''Появится всплывающие окно Error, которое предупредит об ошибке
            и предложит методы её решения'''

            global Error_Window

            Error_Window = QtWidgets.QMessageBox()
            ui_1 = Ui_error_window()
            ui_1.setupUi(Error_Window)

            Error_Window.setText("Сейчас выполнить данное действие невозможно !")
            Error_Window.setInformativeText("Поле ввода ключа пусто")
            Error_Window.setDetailedText(
                "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

            Error_Window.show()
        else:
            pyperclip.copy(str(key))


    ui.but_copy.clicked.connect(copy_clipbord)

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

        file = open("Files/key.txt", 'r')
        key = file.read()
        file.close()

        try:
            iteam = ui.shifrs.currentText()

            if (iteam == "AES"):
                AES_deshif()

        except:
            '''Появится всплывающие окно Error, которое предупредит об ошибке
            и предложит методы её решения'''

            global Error_Window

            Error_Window = QtWidgets.QMessageBox()
            ui_1 = Ui_error_window()
            ui_1.setupUi(Error_Window)

            if os.path.getsize("Files/selected_file.txt") == 0 and key == '':
                Error_Window.setInformativeText("Выберите файл для дешифрования и вставьте ключ")
                Error_Window.setDetailedText(
                    "Программа не сможет дешифровать файл, пока вы не выберите его и не вставите в поле ввода ключа свой ключ")
            elif os.path.getsize("Files/selected_file.txt") == 0:
                Error_Window.setInformativeText("Выберите файл для дешифрования")
                Error_Window.setDetailedText("Программа не сможет дешифровать файл, пока вы не выберите его")
            else:
                Error_Window.setInformativeText("Вставьте свой ключ в поле ввода ключа")
                Error_Window.setDetailedText(
                    "Программа не сможет дешифровать файл, пока вы не вставите в поле ввода ключа свой ключ")

            Error_Window.setText("Сейчас выполнить данное действие невозможно !")
            Error_Window.show()

    ui.but_decr.clicked.connect(check_shifrator)

    def text_insert(passwrd):
        '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

        file = open("Files/key.txt", 'w')
        file.write(str(passwrd))
        file.close()

    ui.key_label.textChanged.connect(text_insert)

    def from_clipbord():
        '''Обработка нажатия на кнопку but_insert
        Вставляет ключ из буфера'''

        file = open("Files/key.txt", 'w')
        key = pyperclip.paste()

        if key == '':
            '''Появится всплывающие окно Error, которое предупредит об ошибке
            и предложит методы её решения'''

            global Error_Window

            Error_Window = QtWidgets.QMessageBox()
            ui_1 = Ui_error_window()
            ui_1.setupUi(Error_Window)

            Error_Window.setText("Сейчас выполнить данное действие невозможно !")
            Error_Window.setInformativeText("Буфер обмена пуст")
            Error_Window.setDetailedText(
                "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете")

            Error_Window.show()
        else:
            ui.key_label.setText(key)
            file.write(key)

        file.close()

    ui.but_insert.clicked.connect(from_clipbord)

    ui.but_exlor.clicked.connect(Choose_fr_expl)


ui.but_encr.clicked.connect(open_Encryption)
ui.but_decr.clicked.connect(open_Decryption)


def delete_file():
    '''При завершении программы очищает содержимое selected_file'''

    file = open("Files/selected_file.txt", 'w')
    file.write('')

    file = open("Files/key.txt", 'w')
    file.write('')


atexit.register(delete_file)  # регестрирует функцию, которая будет выполняться после окончания программы

sys.exit(app.exec_())
