'''Расположен класс Ui_Window_inter,
который описывает весь дизайн окна Intermediate'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_inter(object):
    '''Описывает дизайн окна Intermediate'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(500, 210, 201, 71))
        self.but_encr.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
                                    "font: italic 16pt \"Arial\";")
        self.but_encr.setObjectName("but_encr")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(500, 340, 211, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Arial\";")
        self.but_decr.setObjectName("but_decr")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(850, 20, 71, 61))
        self.settings.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/settings.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setIconSize(QtCore.QSize(60, 60))
        self.settings.setObjectName("settings")
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
        self.help.setGeometry(QtCore.QRect(20, 20, 71, 61))
        self.help.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.Box_encr = QtWidgets.QComboBox(self.centralwidget)
        self.Box_encr.setGeometry(QtCore.QRect(170, 225, 241, 41))
        self.Box_encr.setStyleSheet("font: 75 12pt \"Nirmala UI\";")
        self.Box_encr.setObjectName("Box_encr")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.Box_decr = QtWidgets.QComboBox(self.centralwidget)
        self.Box_decr.setGeometry(QtCore.QRect(170, 360, 241, 41))
        self.Box_decr.setStyleSheet("font: 75 12pt \"Nirmala UI\";")
        self.Box_decr.setObjectName("Box_decr")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_inter()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
