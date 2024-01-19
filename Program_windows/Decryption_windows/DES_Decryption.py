'''Расположен класс Ui_Window_decr_DES,
который описывает весь дизайн окна DES_Decryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_Window_decr_DES(object):
    '''Описывает дизайн окна DES_Decryption'''

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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(160, 95, 431, 71))
        self.label_1.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.but_exlor = QtWidgets.QPushButton(self.centralwidget)
        self.but_exlor.setGeometry(QtCore.QRect(600, 110, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.but_exlor.setObjectName("but_exlor")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon1)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setObjectName("but_back")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(850, 670, 93, 71))
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(390, 540, 171, 61))
        self.but_decr.setStyleSheet("font: italic 13pt \"Courier New\";")
        self.but_decr.setObjectName("but_decr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 290, 131, 71))
        self.label_2.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.but_in_iv = QtWidgets.QPushButton(self.centralwidget)
        self.but_in_iv.setGeometry(QtCore.QRect(690, 385, 141, 61))
        self.but_in_iv.setStyleSheet("font: italic 14pt \"Courier New\";")
        self.but_in_iv.setObjectName("but_in_iv")
        self.iv_label = QtWidgets.QLineEdit(self.centralwidget)
        self.iv_label.setGeometry(QtCore.QRect(270, 392, 341, 51))
        self.iv_label.setStyleSheet("font: 14pt \"Arial\";")
        self.iv_label.setObjectName("iv_label")
        self.iv_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.key_label = QtWidgets.QLineEdit(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(270, 300, 341, 51))
        self.key_label.setStyleSheet("font: 14pt \"Arial\";")
        self.key_label.setObjectName("key_label")
        self.key_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_in_key = QtWidgets.QPushButton(self.centralwidget)
        self.but_in_key.setGeometry(QtCore.QRect(690, 295, 141, 61))
        self.but_in_key.setStyleSheet("font: italic 14pt \"Courier New\";")
        self.but_in_key.setObjectName("but_in_key")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 385, 221, 71))
        self.label_3.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.iv_on_off = QtWidgets.QPushButton(self.centralwidget)
        self.iv_on_off.setGeometry(QtCore.QRect(620, 385, 61, 61))
        self.iv_on_off.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.iv_on_off.setIcon(icon3)
        self.iv_on_off.setIconSize(QtCore.QSize(30, 30))
        self.iv_on_off.setObjectName("iv_on_off")
        self.key_on_off = QtWidgets.QPushButton(self.centralwidget)
        self.key_on_off.setGeometry(QtCore.QRect(620, 295, 61, 61))
        self.key_on_off.setText("")
        self.key_on_off.setIcon(icon3)
        self.key_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_on_off.setObjectName("key_on_off")
        self.but_file = QtWidgets.QPushButton(self.centralwidget)
        self.but_file.setGeometry(QtCore.QRect(740, 100, 61, 61))
        self.but_file.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.but_file.setIcon(icon4)
        self.but_file.setIconSize(QtCore.QSize(60, 100))
        self.but_file.setFlat(True)
        self.but_file.setObjectName("but_file")
        MainWindow.setCentralWidget(self.centralwidget)

        self.but_back.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> DES -> Decryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для расшифровки"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_decr.setText(_translate("MainWindow", "Расшифровать"))
        self.label_2.setText(_translate("MainWindow", "Ваш ключ:"))
        self.but_in_iv.setText(_translate("MainWindow", "Вставить"))
        self.but_in_key.setText(_translate("MainWindow", "Вставить"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\">Ваш вектор </p><p align=\"center\">инициализации:</p></body></html>"))

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
#     ui = Ui_Window_decr_DES()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
