'''Расположен класс Ui_Window_encr_DES,
который описывает весь дизайн окна DES_Encryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class Ui_Window_encr_DES(object):
    '''Описывает дизайн окна DES_Encryption'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(220, 95, 401, 71))
        self.label_1.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_1.setObjectName("label_1")
        self.but_exlor = QtWidgets.QPushButton(self.centralwidget)
        self.but_exlor.setGeometry(QtCore.QRect(640, 110, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.but_exlor.setObjectName("but_exlor")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(360, 260, 171, 61))
        self.but_encr.setStyleSheet("font: italic 12pt \"Courier New\";")
        self.but_encr.setObjectName("but_encr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 423, 121, 71))
        self.label_2.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.but_copy_key = QtWidgets.QPushButton(self.centralwidget)
        self.but_copy_key.setGeometry(QtCore.QRect(650, 428, 141, 61))
        self.but_copy_key.setStyleSheet("font: italic 12pt \"Courier New\";")
        self.but_copy_key.setObjectName("but_copy")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon1)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setObjectName("but_back")
        self.key_label = QtWidgets.QLineEdit(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(290, 438, 341, 41))
        self.key_label.setObjectName("key_label")
        self.key_label.setReadOnly(True)     # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.key_label.setEchoMode(QLineEdit.Password)    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(850, 660, 93, 71))
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 518, 221, 71))
        self.label_3.setStyleSheet("font: italic 14pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.but_copy_iv = QtWidgets.QPushButton(self.centralwidget)
        self.but_copy_iv.setGeometry(QtCore.QRect(650, 518, 141, 61))
        self.but_copy_iv.setStyleSheet("font: italic 12pt \"Courier New\";")
        self.but_copy_iv.setObjectName("but_copy_2")
        self.iv_label = QtWidgets.QLineEdit(self.centralwidget)
        self.iv_label.setGeometry(QtCore.QRect(290, 530, 341, 41))
        self.iv_label.setObjectName("iv_label")
        self.iv_label.setReadOnly(True)   # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.iv_label.setEchoMode(QLineEdit.Password)   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> DES -> Encryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для шифрования"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_encr.setText(_translate("MainWindow", "Зашифровать"))
        self.label_2.setText(_translate("MainWindow", "Ваш ключ:"))
        self.but_copy_key.setText(_translate("MainWindow", "Скопировать"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\">Ваш вектор </p><p align=\"center\">инициализации:</p></body></html>"))
        self.but_copy_iv.setText(_translate("MainWindow", "Скопировать"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_encr_DES()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
