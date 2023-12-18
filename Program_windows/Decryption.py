'''Расположен класс Ui_Window_decr,
который описывает весь дизайн окна Encryption
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class Ui_Window_decr(object):
    '''Описывает дизайн окна Decryption'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(240, 45, 201, 71))
        self.label_1.setStyleSheet("font: 75 italic 14pt \"Arial\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.shifrs = QtWidgets.QComboBox(self.centralwidget)
        self.shifrs.setGeometry(QtCore.QRect(460, 60, 181, 41))
        self.shifrs.setStyleSheet("font: 75 12pt \"Nirmala UI\";")
        self.shifrs.setObjectName("shifrs")
        self.shifrs.addItem("")
        self.shifrs.addItem("")
        self.shifrs.addItem("")
        self.shifrs.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 225, 411, 71))
        self.label_2.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.but_exlor = QtWidgets.QPushButton(self.centralwidget)
        self.but_exlor.setGeometry(QtCore.QRect(630, 240, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.but_exlor.setObjectName("but_exlor")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(365, 550, 171, 61))
        self.but_decr.setStyleSheet("font: italic 12pt \"Courier New\";")
        self.but_decr.setObjectName("but_decr")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 405, 131, 71))
        self.label_3.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.but_insert = QtWidgets.QPushButton(self.centralwidget)
        self.but_insert.setGeometry(QtCore.QRect(620, 410, 141, 61))
        self.but_insert.setStyleSheet("font: italic 12pt \"Courier New\";")
        self.but_insert.setObjectName("but_insert")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.but_back.setIcon(icon)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setObjectName("but_back")
        self.key_label = QtWidgets.QLineEdit(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(300, 420, 301, 41))
        self.key_label.setObjectName("password")
        self.key_label.setObjectName("lineEdit")  # !!!!!!!!!!!!!!!!!!!!!!!!
        self.key_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!

        self.question = QtWidgets.QPushButton(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(850, 620, 93, 71))
        self.question.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.question.setIcon(icon1)
        self.question.setIconSize(QtCore.QSize(60, 60))
        self.question.setObjectName("question")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Decryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите шифр:"))
        self.shifrs.setItemText(0, _translate("MainWindow", "RSA"))
        self.shifrs.setItemText(1, _translate("MainWindow", "AES"))
        self.shifrs.setItemText(2, _translate("MainWindow", "DES"))
        self.shifrs.setItemText(3, _translate("MainWindow", "Шифр Цезаря"))
        self.label_2.setText(_translate("MainWindow", "Выбирите файл для дешифрования"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_decr.setText(_translate("MainWindow", "Дешифровать"))
        self.label_3.setText(_translate("MainWindow", "Ваш ключ:"))
        self.but_insert.setText(_translate("MainWindow", "Вставить"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Decr_Window = QtWidgets.QMainWindow()
#     ui = Ui_Window_decr()
#     ui.setupUi(Decr_Window)
#     Decr_Window.show()
#     sys.exit(app.exec_())
