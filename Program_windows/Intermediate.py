'''Расположен класс Ui_Window_inter,
который описывает весь дизайн окна Intermediate'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_inter(object):
    '''Описывает дизайн окна Intermediate'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]), int(geometry[1]), 950, 750)  # !!!!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(950, 750)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(500, 215, 201, 71))
        self.but_encr.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
                                    "font: italic 16pt \"Arial\";")
        self.but_encr.setObjectName("but_encr")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(500, 345, 211, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Arial\";")
        self.but_decr.setObjectName("but_decr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 650, 161, 41))
        self.label_2.setStyleSheet("font: 6pt \"Terminal\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(810, 640, 131, 51))
        self.label_3.setStyleSheet("font: italic 24pt \"Palace Script MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(860, 20, 71, 61))
        self.help.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.help.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.Box_encr = QtWidgets.QComboBox(self.centralwidget)
        self.Box_encr.setGeometry(QtCore.QRect(170, 225, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Box_encr.setFont(font)
        self.Box_encr.setStyleSheet("font: 75 14pt \"Nirmala UI\";")
        self.Box_encr.setEditable(False)
        self.Box_encr.setIconSize(QtCore.QSize(20, 20))
        self.Box_encr.setFrame(True)
        self.Box_encr.setObjectName("Box_encr")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.Box_decr = QtWidgets.QComboBox(self.centralwidget)
        self.Box_decr.setGeometry(QtCore.QRect(170, 360, 241, 51))
        self.Box_decr.setStyleSheet("font: 75 14pt \"Nirmala UI\";")
        self.Box_decr.setObjectName("Box_decr")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_encr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_decr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Intermediate"))
        self.but_encr.setText(_translate("MainWindow", "Зашифровать"))
        self.but_decr.setText(_translate("MainWindow", "Расшифровать"))
        self.label_2.setText(_translate("MainWindow", "version 2024.1.0"))
        self.label_3.setText(_translate("MainWindow", "Leonardo"))
        self.Box_encr.setItemText(0, _translate("MainWindow", "AES"))
        self.Box_encr.setItemText(1, _translate("MainWindow", "Triple DES"))
        self.Box_encr.setItemText(2, _translate("MainWindow", "RSA"))
        self.Box_decr.setItemText(0, _translate("MainWindow", "AES"))
        self.Box_decr.setItemText(1, _translate("MainWindow", "Triple DES"))
        self.Box_decr.setItemText(2, _translate("MainWindow", "RSA"))

    def go_new_window(self, MainWindow):
        x = MainWindow.geometry().x()
        y = MainWindow.geometry().y()

        file = open("Files/Geometry.txt", 'w')
        file.write(str(x) + '\n')
        file.write(str(y))
        file.close()

    def delete_self(self):
        del self

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_inter()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
