'''Расположен класс Ui_Window_encr,
который описывает весь дизайн окна Encryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class Ui_Window_encr(object):
    '''Описывает дизайн окна Encryption'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(220, 11, 161, 71))
        self.label_1.setStyleSheet("font: 12pt \".AppleSystemUIFont\";")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 30, 141, 35))
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 110, 311, 71))
        self.label_2.setStyleSheet("font: 12pt \".AppleSystemUIFont\";")
        self.label_2.setObjectName("label_2")
        self.but_exlor = QtWidgets.QPushButton(self.centralwidget)
        self.but_exlor.setGeometry(QtCore.QRect(300, 180, 113, 32))
        self.but_exlor.setObjectName("but_exlor")
        self.but_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.but_encrypt.setGeometry(QtCore.QRect(280, 300, 151, 61))
        self.but_encrypt.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.but_encrypt.setObjectName("but_encrypt")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 400, 101, 71))
        self.label_3.setStyleSheet("font: 12pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.but_insert = QtWidgets.QPushButton(self.centralwidget)
        self.but_insert.setGeometry(QtCore.QRect(490, 405, 113, 61))
        self.but_insert.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.but_insert.setObjectName("but_insert")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 101, 61))
        self.but_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\79116\\Documents\\Encoder_ui\\../Encoder_PyQT/arow.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setObjectName("but_back")
        self.pasw_out = QtWidgets.QLineEdit(self.centralwidget)
        self.pasw_out.setGeometry(QtCore.QRect(260, 420, 201, 35))
        self.pasw_out.setObjectName("pasw_out")
        self.pasw_out.setReadOnly(True)
        self.pasw_out.setEchoMode(QLineEdit.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encoder -> Encryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите шифр:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "RSA"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "DES"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Шифр Цезаря"))
        self.label_2.setText(_translate("MainWindow", "Выбирите файл для шифрования"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.label_3.setText(_translate("MainWindow", "Ваш ключ:"))
        self.but_insert.setText(_translate("MainWindow", "Скопировать"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Encr_Window = QtWidgets.QMainWindow()
#     ui = Ui_Window_encr()
#     ui.setupUi(Encr_Window)
#     Encr_Window.show()
#     sys.exit(app.exec_())
