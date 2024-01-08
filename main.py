'''Управляющий файл. По умолчанию открывается окно main_screen
и отслеживается открытие окон Encryption и Decryption
и всплывающего окна Error и выполнение всех встроенных в них функций'''

import atexit
import os.path
import sys
import pyperclip
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import cryptography.hazmat.primitives
from PyQt5 import QtWidgets
from Program_windows.Encryption_windows.AES_Encryption import Ui_Window_encr_AES
from Program_windows.Encryption_windows.RSA_Encryption import Ui_Window_encr_RSA
from Program_windows.Encryption_windows.DES_Encryption import Ui_Window_encr_DES
from Program_windows.Decryption_windows.AES_Decryption import Ui_Window_decr_AES
from Program_windows.Decryption_windows.RSA_Decryption import Ui_Window_decr_RSA
from Program_windows.Decryption_windows.DES_Decryption import Ui_Window_decr_DES
from Program_windows.main_screen import Ui_Window_main_screen
from Shivrs.AES.Shifrator import AES_shifr
from Shivrs.RSA.Deshifrator import RSA_decrypt
from Shivrs.DES.Shifrator import DES_shifr
from Shivrs.DES.Deshifrator import DES_decrypt
from Choose_fr_expl import Choose_fr_expl
from Shivrs.AES.Deshifrator import AES_deshif
from Program_windows.Error import Ui_Window_error
from Program_windows.Intermediate import Ui_Window_inter
from Shivrs.RSA.Shifrator import RSA_shifr


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_Window_main_screen()
ui.setupUi(MainWindow)
MainWindow.show()


def open_Intermediate():
    global Inter_Window

    Inter_Window = QtWidgets.QMainWindow()
    ui = Ui_Window_inter()
    ui.setupUi(Inter_Window)

    MainWindow.close()
    Inter_Window.show()

    def open_Encryption():
        ''' Открывает окно Encryption и обрабатывает действия в нём'''

        if ui.Box_encr.currentText() == "RSA":
            global Encr_Window
            Encr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_encr_RSA()
            ui_1.setupUi(Encr_Window)
            Inter_Window.close()

            def encryption():
                try:
                    def show_keys(key_cl, key_op):
                        '''Шифрует ключи под * и выводит его в окно pasw_out'''

                        ui_1.key_label_cl.setText('*' * len(key_cl))
                        ui_1.key_label_op.setText('*' * len(key_op))

                    RSA_shifr()

                    file_priv = open("Files/RSA_priv_key.pem", 'r')  # Open the private key file
                    private_key = file_priv.readlines()
                    file_priv.close()
                    file_op = open("Files/RSA_pub_key.pem", 'r')  # Open the private key file
                    public_key = file_op.readlines()
                    file_op.close()

                    key_cl = ''.join(private_key[1:26])
                    key_op = ''.join(public_key[1:8])

                    show_keys(key_cl, key_op)

                except:
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                     и предложит методы её решения'''
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)
                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Выберите файл для шифрования")
                    Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его")

                    Error_Window.show()


            ui_1.but_encr.clicked.connect(encryption)
            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в main_screen'''

                Encr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

            def copy_clipbord_cl():
                '''Обработка нажатия на кнопку but_insert
                Копирует ключ в буфер обмена'''

                file = open("Files/RSA_priv_key.pem", 'r')
                lines = file.readlines()
                key_cl = ''.join(lines[1:26])
                file.close()

                if key_cl == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key_cl))

            def copy_clipbord_op():
                '''Обработка нажатия на кнопку but_insert
                Копирует ключ в буфер обмена'''

                file = open("Files/RSA_pub_key.pem", 'r')
                lines = file.readlines()
                key_op = ''.join(lines[1:8])
                file.close()

                if key_op == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key_op))

            ui_1.but_copy_cl.clicked.connect(copy_clipbord_cl)
            ui_1.but_copy_op.clicked.connect(copy_clipbord_op)
            ui_1.but_exlor.clicked.connect(Choose_fr_expl)

            Encr_Window.show()
        elif ui.Box_encr.currentText() == "AES":
            Encr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_encr_AES()
            ui_1.setupUi(Encr_Window)
            Inter_Window.close()

            Encr_Window.show()

            def encryption():
                try:
                    def show_key(key):
                        '''Шифрует ключ под * и выводит его в окно pasw_out'''

                        ui_1.key_label.setText('*' * len(key))

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
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)
                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Выберите файл для шифрования")
                    Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его")

                    Error_Window.show()


            ui_1.but_encr.clicked.connect(encryption)
            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в main_screen'''

                Encr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

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
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key))

            ui_1.but_copy.clicked.connect(copy_clipbord)
            ui_1.but_exlor.clicked.connect(Choose_fr_expl)
        elif ui.Box_encr.currentText() == "DES":
            Encr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_encr_DES()
            ui_1.setupUi(Encr_Window)
            Inter_Window.close()
            Encr_Window.show()

            def encryption():
                try:
                    def show_key_iv(key, iv):
                        '''Шифрует ключ под * и выводит его в окно pasw_out'''

                        ui_1.key_label.setText('*' * len(key))
                        ui_1.iv_label.setText('*' * len(iv))

                    DES_shifr()

                    file = open("Files/key.txt", 'r')
                    key = file.read()
                    file.close()

                    file = open("Files/DES_iv.txt", 'r')
                    iv = file.read()
                    file.close()

                    show_key_iv(key, iv)

                except:
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                     и предложит методы её решения'''
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)
                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Выберите файл для шифрования")
                    Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его")

                    Error_Window.show()


            ui_1.but_encr.clicked.connect(encryption)
            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в main_screen'''

                Encr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

            def copy_clipbord_key():
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
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key))

            def copy_clipbord_iv():
                '''Обработка нажатия на кнопку but_insert
                Копирует ключ в буфер обмена'''

                file = open("Files/DES_iv.txt", 'r')
                iv = file.read()
                file.close()
                if iv == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ в буфера обмена, пока вы не зашифруете файл и не получите ключ")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(iv))

            ui_1.but_copy_key.clicked.connect(copy_clipbord_key)
            ui_1.but_copy_iv.clicked.connect(copy_clipbord_iv)
            ui_1.but_exlor.clicked.connect(Choose_fr_expl)


    def open_Decryption():
        ''' Открывает окно Decryption и обрабатывает действия в нём'''

        if ui.Box_decr.currentText() == "RSA":
            global Decr_Window

            Decr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_decr_RSA()
            ui_1.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()

            file = open("Files/RSA_priv_key.pem", 'w')
            file.write("-----BEGIN RSA PRIVATE KEY-----\n")
            file.close()
            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в main_screen'''

                Decr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

            def decruption():
                file = open("Files/RSA_priv_key.pem", 'a')
                file.write("-----END RSA PRIVATE KEY-----\n")
                file.close()
                file = open("Files/RSA_priv_key.pem", 'r')
                lines = file.readlines()
                key = ''.join(lines[1:26])
                file.close()

                try:
                    RSA_decrypt()

                except:
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

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

            ui_1.but_decr.clicked.connect(decruption)

            def text_insert(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

                file = open("Files/RSA_priv_key.pem", 'a')
                file.write(passwrd)
                file.close()

            ui_1.key_label.textChanged.connect(text_insert)

            def from_clipbord():
                '''Обработка нажатия на кнопку but_insert
                Вставляет ключ из буфера'''

                file = open("Files/RSA_priv_key.pem", 'a')
                key = pyperclip.paste()
                print(key)

                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете")

                    Error_Window.show()
                else:
                    ui_1.key_label.setText(key)
                    file.write(key)

                    with open('Files/RSA_priv_key.pem', 'r') as file:
                        lines = file.readlines()

                    # Удаление пустых строк
                    lines = [line for line in lines if line.strip()]

                    with open('Files/RSA_priv_key.pem', 'w') as file:
                        file.writelines(lines)

                file.close()

            ui_1.but_insert.clicked.connect(from_clipbord)

            ui_1.but_exlor.clicked.connect(Choose_fr_expl)
        elif ui.Box_decr.currentText() == "AES":
            Decr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_decr_AES()
            ui_1.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()

            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в main_screen'''

                Decr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

            def decruption():
                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()


                try:
                    AES_deshif()

                except:
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

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

            ui_1.but_decr.clicked.connect(decruption)

            def text_insert(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

                file = open("Files/key.txt", 'w')
                file.write(str(passwrd))
                file.close()

            ui_1.key_label.textChanged.connect(text_insert)

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
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете")

                    Error_Window.show()
                else:
                    ui_1.key_label.setText(key)
                    file.write(key)

                file.close()

            ui_1.but_insert.clicked.connect(from_clipbord)

            ui_1.but_exlor.clicked.connect(Choose_fr_expl)

        elif ui.Box_decr.currentText() == "DES":
            Decr_Window = QtWidgets.QMainWindow()
            ui_1 = Ui_Window_decr_DES()
            ui_1.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()

            def open_Main():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в main_screen'''

                Decr_Window.close()
                Inter_Window.show()

            ui_1.but_back.clicked.connect(open_Main)

            def decruption():
                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()

                file = open("Files/DES_iv.txt", 'r')
                iv = file.read()
                file.close()


                try:
                    DES_decrypt()

                except:
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

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

            ui_1.but_decr.clicked.connect(decruption)

            def text_insert_key(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

                file = open("Files/key.txt", 'w')
                file.write(str(passwrd))
                file.close()

            def text_insert_iv(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_insert'''

                file = open("Files/DES_iv.txt", 'w')
                file.write(str(passwrd))
                file.close()

            ui_1.key_label.textChanged.connect(text_insert_key)
            ui_1.iv_label.textChanged.connect(text_insert_iv)

            def from_clipbord_key():
                '''Обработка нажатия на кнопку but_insert
                Вставляет ключ из буфера'''

                file = open("Files/key.txt", 'w')
                key = pyperclip.paste()

                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете")

                    Error_Window.show()
                else:
                    ui_1.key_label.setText(key)
                    file.write(key)

                file.close()

            def from_clipbord_iv():
                '''Обработка нажатия на кнопку but_insert
                Вставляет ключ из буфера'''

                file = open("Files/DES_iv.txt", 'w')
                iv = pyperclip.paste()

                if iv == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_2 = Ui_Window_error()
                    ui_2.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете")

                    Error_Window.show()
                else:
                    ui_1.iv_label.setText(iv)
                    file.write(iv)

                file.close()

            ui_1.but_in_key.clicked.connect(from_clipbord_key)
            ui_1.but_in_iv.clicked.connect(from_clipbord_iv)

            ui_1.but_exlor.clicked.connect(Choose_fr_expl)


    ui.but_encr.clicked.connect(open_Encryption)
    ui.but_decr.clicked.connect(open_Decryption)



ui.but_start.clicked.connect(open_Intermediate)


def delete_file():
    '''При завершении программы очищает содержимое selected_file'''

    file = open("Files/selected_file.txt", 'w')
    file.write('')
    file.close()

    file = open("Files/key.txt", 'w')
    file.write('')
    file.close()

    file = open("Files/RSA_pub_key.pem", 'w')
    file.write('')
    file.close()

    file = open("Files/RSA_priv_key.pem", 'w')
    file.write('')
    file.close()

    file = open("Files/DES_iv.txt", 'w')
    file.write('')
    file.close()


atexit.register(delete_file)  # регестрирует функцию, которая будет выполняться после окончания программы

sys.exit(app.exec_())
