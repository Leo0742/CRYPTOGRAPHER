'''Расположен класс Ui_Window_encr_DES,
который описывает весь дизайн окна DES_Encryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QApplication
from Program_windows.Additional.Close_Report import Ui_Window_close_Report

class MyMainWindow(object):
    '''Описывает дизайн окна DES_Encryption'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]), int(geometry[1]), 950, 750)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(950, 750)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border: 2px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;")
        self.but_back.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon4)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setFlat(True)
        self.but_back.setObjectName("but_back")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(860, 10, 81, 71))
        self.help.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.help.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "border: 2px solid rgba(255, 255, 255, 40);\n"
                                "border-radius: 25px;")
        self.help.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setFlat(True)
        self.help.setObjectName("help")
        self.widget_file = QtWidgets.QWidget(self.centralwidget)
        self.widget_file.setGeometry(QtCore.QRect(120, 90, 681, 121))
        self.widget_file.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 25px;")
        self.widget_file.setObjectName("widget_file")
        self.but_file = QtWidgets.QPushButton(self.widget_file)
        self.but_file.setGeometry(QtCore.QRect(610, 30, 61, 61))
        self.but_file.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.but_file.setIcon(icon3)
        self.but_file.setIconSize(QtCore.QSize(60, 100))
        self.but_file.setFlat(True)
        self.but_file.setObjectName("but_file")
        self.label_1 = QtWidgets.QLabel(self.widget_file)
        self.label_1.setGeometry(QtCore.QRect(20, 25, 421, 71))
        self.label_1.setStyleSheet("font: italic 15pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.but_exlor = QtWidgets.QPushButton(self.widget_file)
        self.but_exlor.setGeometry(QtCore.QRect(460, 40, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.but_exlor.setObjectName("but_exlor")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(370, 290, 211, 71))
        self.but_encr.setStyleSheet("font: italic 17pt \"Courier New\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);")
        self.but_encr.setObjectName("but_encr")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(40, 430, 861, 231))
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;")
        self.widget_2.setObjectName("widget_2")
        self.but_copy_iv = QtWidgets.QPushButton(self.widget_2)
        self.but_copy_iv.setGeometry(QtCore.QRect(670, 130, 171, 61))
        self.but_copy_iv.setStyleSheet("font: italic 15pt \"Courier New\";\n"
                                       "color: rgb(255, 255, 255);")
        self.but_copy_iv.setObjectName("but_copy_iv")
        self.key_label = QtWidgets.QLineEdit(self.widget_2)
        self.key_label.setGeometry(QtCore.QRect(250, 45, 341, 51))
        self.key_label.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "background-image: url(:/Icons/key.svg);\n"
                                     "background-position: left;\n"
                                     "background-repeat: no-repeat;\n"
                                     "padding-left: 30px;")
        self.key_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.key_label.setObjectName("key_label")
        self.key_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_copy_key = QtWidgets.QPushButton(self.widget_2)
        self.but_copy_key.setGeometry(QtCore.QRect(670, 40, 171, 61))
        self.but_copy_key.setStyleSheet("font: italic 15pt \"Courier New\";\n"
                                        "color: rgb(255, 255, 255);")
        self.but_copy_key.setObjectName("but_copy_key")
        self.iv_on_off = QtWidgets.QPushButton(self.widget_2)
        self.iv_on_off.setGeometry(QtCore.QRect(600, 130, 61, 61))
        self.iv_on_off.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.iv_on_off.setIcon(icon4)
        self.iv_on_off.setIconSize(QtCore.QSize(30, 30))
        self.iv_on_off.setObjectName("iv_on_off")
        self.iv_label = QtWidgets.QLineEdit(self.widget_2)
        self.iv_label.setGeometry(QtCore.QRect(250, 137, 341, 51))
        self.iv_label.setStyleSheet("font: 14pt \"Arial\";\n"
                                    "background-image: url(:/Icons/iv.svg);\n"
                                    "background-position: left;\n"
                                    "background-repeat: no-repeat;\n"
                                    "padding-left: 30px;")
        self.iv_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.iv_label.setObjectName("iv_label")
        self.iv_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.key_on_off = QtWidgets.QPushButton(self.widget_2)
        self.key_on_off.setGeometry(QtCore.QRect(600, 40, 61, 61))
        self.key_on_off.setText("")
        self.key_on_off.setIcon(icon4)
        self.key_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_on_off.setObjectName("key_on_off")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 221, 81))
        self.label_2.setStyleSheet("font: italic 15pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 221, 81))
        self.label_3.setStyleSheet("font: italic 15pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_back.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_file.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_exlor.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_copy_key.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_copy_iv.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_encr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> DES -> Encryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для шифрования"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_encr.setText(_translate("MainWindow", "Зашифровать"))
        self.but_copy_iv.setText(_translate("MainWindow", "Скопировать"))
        self.but_copy_key.setText(_translate("MainWindow", "Скопировать"))
        self.label_2.setText(_translate("MainWindow", "Ваш ключ:"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\">Ваш вектор </p><p align=\"center\">инициализации:</p></body></html>"))

    def go_new_window(self, MainWindow):
        x = MainWindow.geometry().x()
        y = MainWindow.geometry().y()

        file = open("Files/Geometry.txt", 'w')
        file.write(str(x) + '\n')
        file.write(str(y))
        file.close()

class Ui_Window_encr_DES(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.wind = MyMainWindow()
        self.wind.setupUi(self)

    def closeEvent(self, event):
        event.ignore()

        file = open("Files/DES_RSA_flag.txt", 'r')
        data = file.readlines()
        file.close()
        data[0] = data[0][:-1]
        data[1] = data[1][:-1]

        if (data[0] == "true" and (data[1] == "0" or data[2] == "0")):
            def close_wind(btn):
                if btn.text() == "Cancel":
                    QApplication.quit()

            global Report_Window
            Report_Window = QtWidgets.QMessageBox()
            ui = Ui_Window_close_Report()
            ui.setupUi(Report_Window)

            if (data[1] == "0" and data[2] == "0"):
                Report_Window.setText("Вы не скопировали ключ и вектор инициализации!")
                Report_Window.setDetailedText("Если вы хотите вернуться и скопировать ключ и вектор инициализации, нажмите Cancel.\n"
                                              "Если вы переписали ключ и вектор инициализации вручную и хотите закончить работу с приложением, нажмите OK.")

            elif (data[1] == "0"):
                Report_Window.setText("Вы не скопировали ключ !")
                Report_Window.setDetailedText("Если вы хотите вернуться и скопировать ключ, нажмите Cancel.\n"
                                              "Если вы переписали ключ вручную и хотите закончить работу с приложением, нажмите OK.")

            elif (data[2] == "0"):
                Report_Window.setText("Вы не скопировали вектор инициализации !")
                Report_Window.setDetailedText("Если вы хотите вернуться и скопировать вектор инициализации, нажмите Cancel.\n"
                                              "Если вы переписали вектор инициализации вручную и хотите закончить работу с приложением, нажмите OK.")

            Report_Window.buttonClicked.connect(close_wind)
            Report_Window.show()


        else:
            event.accept()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_encr_DES()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
