'''Расположен класс Ui_Window_decr_RSA,
который описывает весь дизайн окна RSA_Decryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_Window_decr_RSA(object):
    '''Описывает дизайн окна RSA_Decryption'''

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
        self.but_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon1)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setFlat(True)
        self.but_back.setObjectName("but_back")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(850, 10, 93, 71))
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setFlat(True)
        self.help.setObjectName("help")
        self.widget_file = QtWidgets.QWidget(self.centralwidget)
        self.widget_file.setGeometry(QtCore.QRect(130, 120, 681, 121))
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
        self.label_1.setGeometry(QtCore.QRect(10, 25, 431, 71))
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
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(380, 590, 211, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Courier New\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);")
        self.but_decr.setObjectName("but_decr")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 330, 851, 171))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                  "border: 1px solid rgba(255, 255, 255, 40);\n"
                                  "border-radius: 25px;")
        self.widget.setObjectName("widget")
        self.but_insert = QtWidgets.QPushButton(self.widget)
        self.but_insert.setGeometry(QtCore.QRect(680, 50, 161, 61))
        self.but_insert.setStyleSheet("font: italic 16pt \"Courier New\";\n"
                                      "color: rgb(255, 255, 255);")
        self.but_insert.setObjectName("but_insert")
        self.key_on_off = QtWidgets.QPushButton(self.widget)
        self.key_on_off.setGeometry(QtCore.QRect(610, 50, 61, 61))
        self.key_on_off.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/key_OFF.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.key_on_off.setIcon(icon4)
        self.key_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_on_off.setObjectName("key_on_off")
        self.key_label = QtWidgets.QLineEdit(self.widget)
        self.key_label.setGeometry(QtCore.QRect(260, 55, 341, 51))
        self.key_label.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "background-image: url(:/Icons/key.svg);\n"
                                     "background-position: left;\n"
                                     "background-repeat: no-repeat;\n"
                                     "padding-left: 30px;")
        self.key_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.key_label.setObjectName("key_label")
        self.key_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 221, 81))
        self.label_2.setStyleSheet("font: italic 15pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_back.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_file.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_exlor.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_insert.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_decr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> RSA -> Decryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для расшифровки"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_decr.setText(_translate("MainWindow", "Расшифровать"))
        self.but_insert.setText(_translate("MainWindow", "Вставить"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\">Ваш закрытый </p><p align=\"center\">ключ:</p></body></html>"))

    def go_new_window(self, MainWindow):
        x = MainWindow.geometry().x()
        y = MainWindow.geometry().y()

        file = open("Files/Geometry.txt", 'w')
        file.write(str(x) + '\n')
        file.write(str(y))
        file.close()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_decr_RSA()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
