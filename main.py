'''Управляющий файл. По умолчанию открывается окно main_screen
и отслеживается открытие окон Intermediate, Encryption и Decryption
и всплывающих окон Error, Choice_safe, Decr_Progress_Bar, Encr_Progress_Bar, Report,
а так же выполнение всех встроенных в них функций'''

import atexit
import os
import os.path
import sys
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
from Program_windows.Encryption_windows.AES_Encryption import Ui_Window_encr_AES
from Program_windows.Encryption_windows.RSA_Encryption import Ui_Window_encr_RSA
from Program_windows.Encryption_windows.DES_Encryption import Ui_Window_encr_DES
from Program_windows.Decryption_windows.AES_Decryption import Ui_Window_decr_AES
from Program_windows.Decryption_windows.RSA_Decryption import Ui_Window_decr_RSA
from Program_windows.Decryption_windows.DES_Decryption import Ui_Window_decr_DES
from Program_windows.Additional.Encr_Progress_Bar import Ui_Window_EncrProgbar
from Program_windows.Additional.Decr_Progress_Bar import Ui_Window_DecrProgbar
from Program_windows.Additional.Choice_safe import Ui_Window_Chsafe
from Program_windows.Intermediate import Ui_Window_inter
from Program_windows.Additional.Error import Ui_Window_error
from Choose_fr_expl import Choose_fr_expl
from Program_windows.Additional.Report import Ui_Window_report
from Program_windows.main_screen import Ui_Window_main_screen
from Shivrs.AES.Shifrator import AES_shifr
from Shivrs.DES.Shifrator import DES_shifr
from Shivrs.RSA.Shifrator import RSA_shifr
from Shivrs.RSA.Deshifrator import RSA_decrypt
from Shivrs.DES.Deshifrator import DES_decrypt
from Shivrs.AES.Deshifrator import AES_decrypt
from Cleaner import Cleaner


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_Window_main_screen()
ui.setupUi(MainWindow)
MainWindow.show()


def open_Intermediate():
    ''' Открывает окно Intermediate и обрабатывает действия в нём'''

    global Inter_Window

    Inter_Window = QtWidgets.QMainWindow()
    ui_1 = Ui_Window_inter()
    ui_1.setupUi(Inter_Window)

    MainWindow.close()
    Inter_Window.show()
    Inter_Window.close()
    Inter_Window.deleteLater()
    ui_1.delete_self()

    Inter_Window = QtWidgets.QMainWindow()
    ui_1 = Ui_Window_inter()
    ui_1.setupUi(Inter_Window)

    Inter_Window.show()

    def open_Encryption():
        ''' Открывает окно Encryption и обрабатывает действия в нём'''

        if ui_1.Box_encr.currentText() == "RSA":
            '''Открывает открывает окно RSA_Encryption и обрабатывает действия в нём'''

            global Encr_Window
            Encr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_encr_RSA()
            ui_2.setupUi(Encr_Window)
            Inter_Window.close()
            Encr_Window.show()


            def encryption():
                '''Обработка нажатия на кнопку but_encr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()


                def Encrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    selected_file = open("Files/selected_file.txt", "r")
                    print(selected_file.read())
                    if selected_file.read() != '':
                        size = os.path.getsize(selected_file.read()) >= 190
                    else:
                        size = False

                    selected_file.close()

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '' or size:
                            print(end)

                        '''Открывает окно Encr_Progress_Bar которое отслеживает выполнение шифрования'''

                        global EncrProgbar_Window

                        EncrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_EncrProgbar()
                        ui_4.setupUi(EncrProgbar_Window)
                        EncrProgbar_Window.show()

                        ui_4.progBar_encr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        def show_keys(key_cl, key_op):
                            '''Шифрует ключи под * и выводит его в окна key_label_cl и key_label_op'''

                            ui_2.key_label_cl.setText(key_cl)
                            ui_2.key_label_op.setText(key_op)

                        crypt_text = RSA_shifr()

                        ui_4.progBar_encr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(crypt_text)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(crypt_text)  # Read and store the content of the selected file
                            file.close()

                        ui_4.progBar_encr.setValue(75)
                        QtWidgets.QApplication.processEvents()

                        file_cl = open("Files/RSA_priv_key.pem", 'r')  # Open the private key file
                        close_key = file_cl.readlines()
                        file_cl.close()
                        file_op = open("Files/RSA_pub_key.pem", 'r')  # Open the private key file
                        open_key = file_op.readlines()
                        file_op.close()

                        key_cl = ''.join(close_key[1:26])
                        key_op = ''.join(open_key[1:8])

                        show_keys(key_cl, key_op)

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                        ui_4.progBar_encr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        EncrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешном шифровании файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Шифрование вашего файла было выполнено успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        selected_file = open("Files/selected_file.txt", "r")
                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()


                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)
                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        if os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для шифрования")
                            Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его.")
                        elif os.path.getsize(selected_file.read()) > 190:
                            Error_Window.setInformativeText("Данный файл не может быть зашифрован")
                            Error_Window.setDetailedText(
                                "Выбранный вами файл невозможно зашифровать при помощи алгоритма RSA, из-за особенностей его реализации."
                                " Выберите другой алгоритм шифрования.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Возникла непредвиденная ошибка")
                            Error_Window.setDetailedText(
                                "Скорее всего вы наткнулись на программную ошибку. В скором времени она будет исправлена.")

                            EncrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_EncrProgbar()
                            ui_4.setupUi(EncrProgbar_Window)
                            EncrProgbar_Window.show()
                            EncrProgbar_Window.close()

                        selected_file.close()
                        Error_Window.show()

                ui_3.but_next.clicked.connect(Encrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в Intermediate'''

                Cleaner()
                Encr_Window.close()
                open_Intermediate()

            def copy_clipbord_cl():
                '''Обработка нажатия на кнопку but_copy_cl
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
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Ключ не получится скопировать в буфер обмена, пока вы не зашифруете файл и не получите свой закрытый ключ.")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key_cl))

            def copy_clipbord_op():
                '''Обработка нажатия на кнопку but_copy_op
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
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Ключ не получится скопировать в буфер обмена, пока вы не зашифруете файл и не получите свой открытый ключ.")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key_op))

            def chang_text_label_cl():
                '''Обработка нажатия на кнопку key_cl_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label_cl'''

                echo_mode = ui_2.key_label_cl.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_cl_on_off.setIcon(icon3)
                    ui_2.key_cl_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label_cl.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_cl_on_off.setIcon(icon3)
                    ui_2.key_cl_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label_cl.setEchoMode(QLineEdit.Password)

            def chang_text_label_op():
                '''Обработка нажатия на кнопку key_op_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label_op'''

                echo_mode = ui_2.key_label_op.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_op_on_off.setIcon(icon3)
                    ui_2.key_op_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label_op.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_op_on_off.setIcon(icon3)
                    ui_2.key_op_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label_op.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для шифрования не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для шифрования выбран.")
                Report_Window.show()
                file.close()

            ui_2.but_encr.clicked.connect(encryption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.but_copy_cl.clicked.connect(copy_clipbord_cl)
            ui_2.but_copy_op.clicked.connect(copy_clipbord_op)
            ui_2.key_cl_on_off.clicked.connect(chang_text_label_cl)
            ui_2.key_op_on_off.clicked.connect(chang_text_label_op)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)
        elif ui_1.Box_encr.currentText() == "AES":
            '''Открывает открывает окно AES_Encryption и обрабатывает действия в нём'''

            Encr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_encr_AES()
            ui_2.setupUi(Encr_Window)
            Inter_Window.close()
            Encr_Window.show()


            def encryption():
                '''Обработка нажатия на кнопку but_encr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()

                def Encrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '':
                            print(end)

                        '''Открывает окно Encr_Progress_Bar которое отслеживает выполнение шифрования'''

                        global EncrProgbar_Window

                        EncrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_EncrProgbar()
                        ui_4.setupUi(EncrProgbar_Window)
                        EncrProgbar_Window.show()

                        ui_4.progBar_encr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        def show_key(key):
                            '''Шифрует ключ под * и выводит его в окно pasw_out'''

                            ui_2.key_label.setText(key)

                        crypt_text = AES_shifr()

                        ui_4.progBar_encr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(crypt_text)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(crypt_text)  # Read and store the content of the selected file
                            file.close()

                        ui_4.progBar_encr.setValue(75)
                        QtWidgets.QApplication.processEvents()

                        file = open("Files/key.txt", 'r')
                        key = file.read()
                        file.close()

                        show_key(key)

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                        ui_4.progBar_encr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        EncrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешном шифровании файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Шифрование вашего файла было выполнено успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()

                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)
                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        if os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для шифрования")
                            Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Возникла непредвиденная ошибка")
                            Error_Window.setDetailedText(
                                "Скорее всего вы наткнулись на программную ошибку.В скором времени она будет исправлена.")

                            EncrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_EncrProgbar()
                            ui_4.setupUi(EncrProgbar_Window)
                            EncrProgbar_Window.show()
                            EncrProgbar_Window.close()

                        Error_Window.show()

                ui_3.but_next.clicked.connect(Encrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в Intermediate'''

                Cleaner()

                Encr_Window.close()
                open_Intermediate()

            def copy_clipbord():
                '''Обработка нажатия на кнопку but_copy
                Копирует ключ в буфер обмена'''

                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()
                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Ключ не получится скопировать в буфер обмена, пока вы не зашифруете файл и не получите свой ключ для расшифровки.")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key))

            def text_insert(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_label'''

                file = open("Files/key.txt", 'w')
                file.write(passwrd)
                file.close()

            def chang_text_label():
                '''Обработка нажатия на кнопку key_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label'''

                echo_mode = ui_2.key_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для шифрования не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для шифрования выбран.")

                Report_Window.show()
                file.close()


            ui_2.but_encr.clicked.connect(encryption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.but_copy.clicked.connect(copy_clipbord)
            ui_2.key_label.textChanged.connect(text_insert)
            ui_2.key_on_off.clicked.connect(chang_text_label)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)
        elif ui_1.Box_encr.currentText() == "Triple DES":
            '''Открывает открывает окно DES_Encryption и обрабатывает действия в нём'''

            Encr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_encr_DES()
            ui_2.setupUi(Encr_Window)
            Inter_Window.close()
            Encr_Window.show()


            def encryption():
                '''Обработка нажатия на кнопку but_encr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()

                def Encrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '':
                            print(end)

                        '''Открывает окно Encr_Progress_Bar которое отслеживает выполнение шифрования'''

                        global EncrProgbar_Window

                        EncrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_EncrProgbar()
                        ui_4.setupUi(EncrProgbar_Window)
                        EncrProgbar_Window.show()

                        ui_4.progBar_encr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        def show_key_iv(key, iv):
                            '''Шифрует ключ под * и выводит его в окно pasw_out'''

                            ui_2.key_label.setText(key)
                            ui_2.iv_label.setText(iv)

                        crypt_text = DES_shifr()

                        ui_4.progBar_encr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(crypt_text)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(crypt_text)  # Read and store the content of the selected file
                            file.close()

                        ui_4.progBar_encr.setValue(75)
                        QtWidgets.QApplication.processEvents()

                        file = open("Files/key.txt", 'r')
                        key = file.read()
                        file.close()

                        file = open("Files/DES_iv.txt", 'r')
                        iv = file.read()
                        file.close()

                        show_key_iv(key, iv)

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                        ui_4.progBar_encr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        EncrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешном шифровании файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Шифрование вашего файла было выполнено успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()

                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)
                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        if os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для шифрования")
                            Error_Window.setDetailedText("Программа не сможет зашифровать файл, пока вы не выберите его.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Возникла непредвиденная ошибка")
                            Error_Window.setDetailedText(
                                "Скорее всего вы наткнулись на программную ошибку.В скором времени она будет исправлена.")

                            EncrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_EncrProgbar()
                            ui_4.setupUi(EncrProgbar_Window)
                            EncrProgbar_Window.show()
                            EncrProgbar_Window.close()

                        Error_Window.show()

                ui_3.but_next.clicked.connect(Encrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Encryption и возвращaется в Intermediate'''

                Cleaner()

                Encr_Window.close()
                open_Intermediate()

            def copy_clipbord_key():
                '''Обработка нажатия на кнопку but_copy_key
                Копирует ключ в буфер обмена'''

                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()
                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода ключа пусто")
                    Error_Window.setDetailedText(
                        "Ключ не получится скопировать в буфер обмена, пока вы не зашифруете файл и не получите свой ключ для расшифровки.")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(key))

            def copy_clipbord_iv():
                '''Обработка нажатия на кнопку but_copy_iv
                Копирует вектор инициализации в буфер обмена'''

                file = open("Files/DES_iv.txt", 'r')
                iv = file.read()
                file.close()
                if iv == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Поле ввода вектора инициализации пусто")
                    Error_Window.setDetailedText(
                        "Вектор инициализации не получится скопировать в буфер обмена, пока вы не зашифруете файл и не получите свой вектор инициализации для расшифровки.")

                    Error_Window.show()
                else:
                    pyperclip.copy(str(iv))

            def text_insert_key(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_label'''

                file = open("Files/key.txt", 'w')
                file.write(passwrd)
                file.close()

            def text_insert_iv(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа iv_label'''

                file = open("Files/DES_iv.txt", 'w')
                file.write(passwrd)
                file.close()

            def chang_text_key_label():
                '''Обработка нажатия на кнопку key_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label'''

                echo_mode = ui_2.key_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Password)

            def chang_text_iv_label():
                '''Обработка нажатия на кнопку iv_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в iv_label'''

                echo_mode = ui_2.iv_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.iv_on_off.setIcon(icon3)
                    ui_2.iv_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.iv_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.iv_on_off.setIcon(icon3)
                    ui_2.iv_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.iv_label.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для шифрования не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для шифрования выбран.")
                Report_Window.show()
                file.close()


            ui_2.but_encr.clicked.connect(encryption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.but_copy_key.clicked.connect(copy_clipbord_key)
            ui_2.but_copy_iv.clicked.connect(copy_clipbord_iv)
            ui_2.key_label.textChanged.connect(text_insert_key)
            ui_2.iv_label.textChanged.connect(text_insert_iv)
            ui_2.key_on_off.clicked.connect(chang_text_key_label)
            ui_2.iv_on_off.clicked.connect(chang_text_iv_label)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)


    def open_Decryption():
        ''' Открывает окно Decryption и обрабатывает действия в нём'''

        if ui_1.Box_decr.currentText() == "RSA":
            '''Открывает открывает окно RSA_Decryption и обрабатывает действия в нём'''

            global Decr_Window

            Decr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_decr_RSA()
            ui_2.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()


            def decruption():
                '''Обработка нажатия на кнопку but_decr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                file = open("Files/RSA_priv_key.pem", 'a')
                file.write("\n-----END RSA PRIVATE KEY-----\n")
                file.close()

                file = open("Files/RSA_priv_key.pem", 'r')
                lines = file.readlines()
                print(lines)
                file.close()

                file = open("Files/RSA_priv_key.pem", 'w')
                file.write("-----BEGIN RSA PRIVATE KEY-----\n")
                file.close()

                file = open("Files/RSA_priv_key.pem", 'a')
                file.writelines(lines)
                file.close()

                file = open("Files/RSA_priv_key.pem", 'r')
                lines = file.readlines()
                file.close()

                key = ''.join(lines[1:26])

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()

                def Decrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '':
                            print(end)

                        '''Открывает окно Decr_Progress_Bar которое отслеживает выполнение расшифровки'''

                        global DecrProgbar_Window

                        DecrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_DecrProgbar()
                        ui_4.setupUi(DecrProgbar_Window)
                        DecrProgbar_Window.show()

                        ui_4.progBar_decr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        plaintext = RSA_decrypt()

                        ui_4.progBar_decr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(plaintext)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(plaintext)  # Read and store the content of the selected file
                            file.close()

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                        ui_4.progBar_decr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        DecrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешной расшифровки файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Расшифровка вашего файла была выполнена успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()

                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)

                        if os.path.getsize("Files/selected_file.txt") == 0 and key == '':
                            Error_Window.setInformativeText("Выберите файл для расшифровки и вставьте свой закрытый ключ")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не выберите его и не вставите в поле ввода ключа свой закрытый ключ.")
                        elif os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для расшифровки")
                            Error_Window.setDetailedText("Программа не сможет расшифровать файл, пока вы не выберите его.")
                        elif key == '':
                            Error_Window.setInformativeText("Вставьте свой закрытый ключ в поле ввода ключа")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не вставите в поле ввода ключа свой закрытый ключ.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Неверный алгоритм шифрования или ключ")
                            Error_Window.setDetailedText(
                                "Вами был выбран неверный алгоритм для расшифровки вашего файла(шифрование/расшифровка файла должны выполняться одним алгоритмом) "
                                "или вы предоставили неверный ключ.")

                            DecrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_DecrProgbar()
                            ui_4.setupUi(DecrProgbar_Window)
                            DecrProgbar_Window.show()
                            DecrProgbar_Window.close()

                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        Error_Window.show()

                ui_3.but_next.clicked.connect(Decrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в Intermediate'''

                Cleaner()

                Decr_Window.close()
                open_Intermediate()

            def text_insert(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_label'''

                if len(passwrd) > 1588:
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setInformativeText("Ошибка во время введения ключа")
                    Error_Window.setDetailedText(
                        f"Закрытый ключ алгоритма шифрования RSA состоит из 1588 символов, вы ввели {len(passwrd)}. "
                        f"Ваш ключ будет сокращён до 1588 символов.")

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.show()

                    passwrd = passwrd[:1588]
                    ui_2.key_label.setText(passwrd)

                else:
                    file = open("Files/RSA_priv_key.pem", 'w')
                    file.write('')
                    file.close()

                    file = open("Files/RSA_priv_key.pem", 'a')

                    cnt = 0
                    for i in passwrd:
                        if (cnt == 64):
                            file.write('\n')
                            cnt = 0

                        cnt += 1
                        file.write(i)

                    file.close()

            def from_clipbord():
                '''Обработка нажатия на кнопку but_insert
                Вставляет ключ из буфера'''

                key = pyperclip.paste()

                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете.")

                    Error_Window.show()
                else:
                    key = [i for i in key if i.strip()]

                    for i in range(len(key)):
                        key[i] = key[i].strip()

                    key = ''.join(key)

                    ui_2.key_label.setText(key)

            def chang_text_label():
                '''Обработка нажатия на кнопку key_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label'''

                echo_mode = ui_2.key_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для расшифровки не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для расшифровки выбран.")
                Report_Window.show()
                file.close()


            ui_2.but_decr.clicked.connect(decruption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.key_label.textChanged.connect(text_insert)
            ui_2.but_insert.clicked.connect(from_clipbord)
            ui_2.key_on_off.clicked.connect(chang_text_label)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)
        elif ui_1.Box_decr.currentText() == "AES":
            '''Открывает открывает окно AES_Decryption и обрабатывает действия в нём'''

            Decr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_decr_AES()
            ui_2.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()


            def decruption():
                '''Обработка нажатия на кнопку but_decr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()

                def Decrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '':
                            print(end)

                        '''Открывает окно Decr_Progress_Bar которое отслеживает выполнение расшифровки'''

                        global DecrProgbar_Window

                        DecrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_DecrProgbar()
                        ui_4.setupUi(DecrProgbar_Window)
                        DecrProgbar_Window.show()

                        ui_4.progBar_decr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        plaintext = AES_decrypt()

                        ui_4.progBar_decr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(plaintext)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(plaintext)  # Read and store the content of the selected file
                            file.close()

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                        ui_4.progBar_decr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        DecrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешной расшифровки файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Расшифровка вашего файла была выполнена успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()

                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)

                        if os.path.getsize("Files/selected_file.txt") == 0 and key == '':
                            Error_Window.setInformativeText("Выберите файл для расшифровки и вставьте свой ключ")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не выберите его и не вставите в поле ввода ключа свой ключ.")
                        elif os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для расшифровки")
                            Error_Window.setDetailedText("Программа не сможет расшифровать файл, пока вы не выберите его.")
                        elif key == '':
                            Error_Window.setInformativeText("Вставьте свой ключ в поле ввода ключа")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не вставите в поле ввода ключа свой ключ.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Неверный алгоритм шифрования или ключ")
                            Error_Window.setDetailedText(
                                "Вами был выбран неверный алгоритм для расшифровки вашего файла (шифрование/расшифровка файла должны выполняться одним алгоритмом) "
                                "или вы предоставили неверный ключ.")

                            DecrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_DecrProgbar()
                            ui_4.setupUi(DecrProgbar_Window)
                            DecrProgbar_Window.show()
                            DecrProgbar_Window.close()

                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        Error_Window.show()

                ui_3.but_next.clicked.connect(Decrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в Intermediate'''

                Cleaner()

                Decr_Window.close()
                open_Intermediate()

            def text_insert(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_label'''

                if len(passwrd) > 44:
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setInformativeText("Ошибка во время введения ключа")
                    Error_Window.setDetailedText(
                        f"Ключ алгоритма шифрования AES состоит из 44 символов, вы ввели {len(passwrd)}. "
                        f"Ваш ключ будет сокращён до 44 символов.")

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.show()

                    passwrd = passwrd[:44]
                    ui_2.key_label.setText(passwrd)

                else:
                    file = open("Files/key.txt", 'w')
                    file.write(str(passwrd))
                    file.close()

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
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете.")

                    Error_Window.show()
                else:
                    ui_2.key_label.setText(key)
                    file.write(key)

                file.close()

            def chang_text_label():
                '''Обработка нажатия на кнопку key_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label'''

                echo_mode = ui_2.key_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для расшифровки не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для расшифровки выбран.")
                Report_Window.show()
                file.close()


            ui_2.but_decr.clicked.connect(decruption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.key_label.textChanged.connect(text_insert)
            ui_2.but_insert.clicked.connect(from_clipbord)
            ui_2.key_on_off.clicked.connect(chang_text_label)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)
        elif ui_1.Box_decr.currentText() == "Triple DES":
            '''Открывает открывает окно DES_Decryption и обрабатывает действия в нём'''

            Decr_Window = QtWidgets.QMainWindow()
            ui_2 = Ui_Window_decr_DES()
            ui_2.setupUi(Decr_Window)
            Inter_Window.close()
            Decr_Window.show()


            def decruption():
                '''Обработка нажатия на кнопку but_decr
                Открывает окно Choice_safe и обрабатывает действия в нём'''

                file = open("Files/key.txt", 'r')
                key = file.read()
                file.close()

                file = open("Files/DES_iv.txt", 'r')
                iv = file.read()
                file.close()

                global Chsafe_Window
                Chsafe_Window = QtWidgets.QMainWindow()
                ui_3 = Ui_Window_Chsafe()
                ui_3.setupUi(Chsafe_Window)
                Chsafe_Window.show()

                def Decrwind():
                    '''Обработка нажатия на кнопку but_next
                    Обрабатывает действия в окне Choice_safe'''

                    global flag
                    global end

                    flag = None

                    try:
                        if ui_3.rab_new.isChecked():
                            flag = True
                        elif ui_3.rab_this.isChecked():
                            flag = False
                        file = open("Files/flag_value.txt", 'w')
                        file.write(str(flag))
                        file.close()

                        Chsafe_Window.close()

                        file = open("Files/selected_file.txt", 'r')
                        selection = file.read()
                        file.close()

                        if flag == None or selection == '':
                            print(end)

                        '''Открывает окно Decr_Progress_Bar которое отслеживает выполнение расшифровки'''

                        global DecrProgbar_Window

                        DecrProgbar_Window = QtWidgets.QMainWindow()
                        ui_4 = Ui_Window_DecrProgbar()
                        ui_4.setupUi(DecrProgbar_Window)
                        DecrProgbar_Window.show()

                        ui_4.progBar_decr.setValue(25)
                        QtWidgets.QApplication.processEvents()

                        plaintext = DES_decrypt()

                        ui_4.progBar_decr.setValue(50)
                        QtWidgets.QApplication.processEvents()

                        if flag:
                            '''Открывает окно Проводника для названия и сохранения файла в выбранном месте'''

                            options = QFileDialog.Options()
                            file_name, _ = QFileDialog.getSaveFileName(Encr_Window, "Сохранить файл", "",
                                                                       "All Files (*)",
                                                                       options=options)
                            if file_name:
                                with open(file_name, 'wb') as f:
                                    f.write(plaintext)
                                    f.close()
                        else:
                            '''Перезаписывает содержимое файла на зашифрованный текст'''

                            file = open("Files/selected_file.txt", "r")
                            open(file.read(), 'wb').write(plaintext)  # Read and store the content of the selected file
                            file.close()

                        file = open("Files/selected_file.txt", 'w')
                        file.write('')
                        file.close()

                        icon3 = QtGui.QIcon()
                        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
                        ui_2.but_file.setIcon(icon3)
                        ui_2.but_file.setIconSize(QtCore.QSize(30, 30))
                        
                        ui_4.progBar_decr.setValue(100)
                        QtWidgets.QApplication.processEvents()
                        DecrProgbar_Window.close()

                        '''Открывает окно Report которое сообщает об успешной расшифровки файла'''

                        global Report_Window

                        Report_Window = QtWidgets.QMessageBox()
                        ui_5 = Ui_Window_report()
                        ui_5.setupUi(Report_Window)
                        Report_Window.setText("Расшифровка вашего файла была выполнена успешно !")

                        Report_Window.show()

                    except:
                        '''Появится всплывающие окно Error, которое предупредит об ошибке
                        и предложит методы её решения'''

                        flag_value = open("Files/flag_value.txt", 'r')
                        flag = flag_value.read()
                        flag_value.close()

                        global Error_Window

                        Error_Window = QtWidgets.QMessageBox()
                        ui_6 = Ui_Window_error()
                        ui_6.setupUi(Error_Window)

                        if os.path.getsize("Files/selected_file.txt") == 0 and key == '' and iv == '':
                            Error_Window.setInformativeText("Выберите файл для расшифровки, вставьте свой ключ и вектор инициализации")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не выберите его и не вставите в поля ввода свой ключ и вектор инициализации.")
                        elif os.path.getsize("Files/selected_file.txt") == 0 and key == '':
                            Error_Window.setInformativeText("Выберите файл для расшифровки и вставьте свой ключ")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не выберите его и не вставите в поле ввода ключа свой ключ.")
                        elif os.path.getsize("Files/selected_file.txt") == 0 and iv == '':
                            Error_Window.setInformativeText("Выберите файл для расшифровки и вставьте свой вектор инициализации")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не выберите его и не вставите в поле ввода вектора инициализации свой вектор инициализации.")
                        elif os.path.getsize("Files/selected_file.txt") == 0:
                            Error_Window.setInformativeText("Выберите файл для расшифровки")
                            Error_Window.setDetailedText("Программа не сможет расшифровать файл, пока вы не выберите его.")
                        elif key == '':
                            Error_Window.setInformativeText("Вставьте свой ключ в поле ввода ключа")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не вставите в поле ввода ключа свой ключ.")
                        elif iv == '':
                            Error_Window.setInformativeText("Вставьте свой вектор инициализации в поле ввода вектора инициализации")
                            Error_Window.setDetailedText(
                                "Программа не сможет расшифровать файл, пока вы не вставите в поле ввода вектора инициализации свой вектор инициализации.")
                        elif flag == "None":
                            Error_Window.setInformativeText("Выберите вариант сохранения вашего файла")
                            Error_Window.setDetailedText(
                                "Программа не сможет сохранить файл пока вы не выберите вариант его сохранения.")
                        else:
                            Error_Window.setInformativeText("Неверный алгоритм шифрования или ключ")
                            Error_Window.setDetailedText(
                                "Вами был выбран неверный алгоритм для расшифровки вашего файла(шифрование/расшифровка файла должны выполняться одним алгоритмом) "
                                "или вы предоставили неверный ключ.")

                            DecrProgbar_Window = QtWidgets.QMainWindow()
                            ui_4 = Ui_Window_DecrProgbar()
                            ui_4.setupUi(DecrProgbar_Window)
                            DecrProgbar_Window.show()
                            DecrProgbar_Window.close()

                        Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                        Error_Window.show()
                ui_3.but_next.clicked.connect(Decrwind)

            def back_Intermediate():
                ''' Обработка нажатия на кнопку but_back
                Закрывает окно Decryption и возвращaется в Intermediate'''

                Cleaner()

                Decr_Window.close()
                open_Intermediate()

            def text_insert_key(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа key_label'''

                if len(passwrd) > 16:
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setInformativeText("Ошибка во время введения ключа")
                    Error_Window.setDetailedText(
                        f"Ключ алгоритма шифрования Triple DES состоит из 16 символов, вы ввели {len(passwrd)}. "
                        f"Ваш ключ будет сокращён до 16 символов.")

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.show()

                    passwrd = passwrd[:16]
                    ui_2.key_label.setText(passwrd)

                else:
                    file = open("Files/key.txt", 'w')
                    file.write(str(passwrd))
                    file.close()

            def text_insert_iv(passwrd):
                '''Обрабатывает ввод значений в поле ввода ключа iv_label'''

                if len(passwrd) > 8:
                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setInformativeText("Ошибка во время введения ключа")
                    Error_Window.setDetailedText(
                        f"Вектор инициализации алгоритма шифрования Triple DES состоит из 8 символов, вы ввели {len(passwrd)}. "
                        f"Ваш ключ будет сокращён до 8 символов.")

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.show()

                    passwrd = passwrd[:8]
                    ui_2.key_label.setText(passwrd)

                else:
                    file = open("Files/DES_iv.txt", 'w')
                    file.write(str(passwrd))
                    file.close()

            def from_clipbord_key():
                '''Обработка нажатия на кнопку but_in_key
                Вставляет ключ из буфера'''

                file = open("Files/key.txt", 'w')
                key = pyperclip.paste()

                if key == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_6 = Ui_Window_error()
                    ui_6.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш ключ с буфера обмена, пока вы его не скопируете.")

                    Error_Window.show()
                else:
                    ui_2.key_label.setText(key)
                    file.write(key)

                file.close()

            def from_clipbord_iv():
                '''Обработка нажатия на кнопку but_in_iv
                Вставляет вектор инициализации из буфера'''

                file = open("Files/DES_iv.txt", 'w')
                iv = pyperclip.paste()

                if iv == '':
                    '''Появится всплывающие окно Error, которое предупредит об ошибке
                    и предложит методы её решения'''

                    global Error_Window

                    Error_Window = QtWidgets.QMessageBox()
                    ui_3 = Ui_Window_error()
                    ui_3.setupUi(Error_Window)

                    Error_Window.setText("Сейчас выполнить данное действие невозможно !")
                    Error_Window.setInformativeText("Буфер обмена пуст")
                    Error_Window.setDetailedText(
                        "Программа не сможет считать ваш вектор инициализации с буфера обмена, пока вы его не скопируете.")

                    Error_Window.show()
                else:
                    ui_2.iv_label.setText(iv)
                    file.write(iv)

                file.close()

            def chang_text_key_label():
                '''Обработка нажатия на кнопку key_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в key_label'''

                echo_mode = ui_2.key_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.key_on_off.setIcon(icon3)
                    ui_2.key_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.key_label.setEchoMode(QLineEdit.Password)

            def chang_text_iv_label():
                '''Обработка нажатия на кнопку iv_on_off
                Меняет иконку у данной кнопки и
                включает отображения пароля в iv_label'''

                echo_mode = ui_2.iv_label.echoMode()

                if echo_mode == QLineEdit.Password:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_on.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.iv_on_off.setIcon(icon3)
                    ui_2.iv_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.iv_label.setEchoMode(QLineEdit.Normal)

                else:
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.iv_on_off.setIcon(icon3)
                    ui_2.iv_on_off.setIconSize(QtCore.QSize(30, 30))

                    ui_2.iv_label.setEchoMode(QLineEdit.Password)

            def choose_file():
                '''Обработка нажатия на клавишу but_exlor
                Вызывает функцию Choose_fr_expl,
                чтобы запомнить местоположение выбранного файла.
                Меняет иконку кнопки but_file если местоположение сохранилось'''

                Choose_fr_expl()

                file = open("Files/selected_file.txt", 'r')

                if file.read() != '':
                    icon3 = QtGui.QIcon()
                    icon3.addPixmap(QtGui.QPixmap("Icons/file_YES.svg"), QtGui.QIcon.Normal,
                                    QtGui.QIcon.Off)
                    ui_2.but_file.setIcon(icon3)
                    ui_2.but_file.setIconSize(QtCore.QSize(30, 30))

                file.close()

            def cur_state_file():
                '''Обработка нажатия на клавишу but_file
                Вызов окна Report'''

                file = open("Files/selected_file.txt", 'r')

                global Report_Window

                Report_Window = QtWidgets.QMessageBox()
                ui_5 = Ui_Window_report()
                ui_5.setupUi(Report_Window)

                if file.read() == '':
                    Report_Window.setText("В данный момент файл для расшифровки не выбран.")
                else:
                    Report_Window.setText("В данный момент файл для расшифровки выбран.")
                Report_Window.show()
                file.close()


            ui_2.but_decr.clicked.connect(decruption)
            ui_2.but_back.clicked.connect(back_Intermediate)
            ui_2.key_label.textChanged.connect(text_insert_key)
            ui_2.iv_label.textChanged.connect(text_insert_iv)
            ui_2.but_in_key.clicked.connect(from_clipbord_key)
            ui_2.but_in_iv.clicked.connect(from_clipbord_iv)
            ui_2.key_on_off.clicked.connect(chang_text_key_label)
            ui_2.iv_on_off.clicked.connect(chang_text_iv_label)
            ui_2.but_exlor.clicked.connect(choose_file)
            ui_2.but_file.clicked.connect(cur_state_file)


    ui_1.but_encr.clicked.connect(open_Encryption)
    ui_1.but_decr.clicked.connect(open_Decryption)


ui.but_start.clicked.connect(open_Intermediate)


def upd_Geom():
    '''При выходе из приложения задаёт
     стартовые координаты окна для следующего включения'''

    file = open("Files/Geometry.txt", 'w')
    file.write('485' + '\n')
    file.write('165')
    file.close()

atexit.register(Cleaner)  # регестрирует функцию, которая будет выполняться после окончания программы
atexit.register(upd_Geom) # регестрирует функцию, которая будет выполняться после окончания программы

sys.exit(app.exec_())
