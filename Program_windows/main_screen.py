'''Расположен класс Ui_MainWindow ,
который описывает весь дизайн окна main_screen
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    '''Описывает дизайн окна main_screen'''
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # !!!!!!!!!!!!!!!!!!!!!!!!!!1
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(170, 270, 201, 71))
        self.but_encr.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
                                    "font: italic 16pt \"Arial\";")
        self.but_encr.setObjectName("but_encr")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(170, 420, 211, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Arial\";")
        self.but_decr.setObjectName("but_decr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 100, 501, 81))
        self.label.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.docum = QtWidgets.QPushButton(self.centralwidget)
        self.docum.setGeometry(QtCore.QRect(600, 340, 211, 71))
        self.docum.setStyleSheet("font: italic 16pt \"Arial\";")
        self.docum.setObjectName("docum")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(840, 30, 71, 61))
        self.settings.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/settings.svg"), QtGui.QIcon.Normal, # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                       QtGui.QIcon.Off)
        self.settings.setIcon(icon)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.but_encr.setText(_translate("MainWindow", "Зашифровать"))
        self.but_decr.setText(_translate("MainWindow", "Дешифровать"))
        self.label.setText(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.docum.setText(_translate("MainWindow", "Документация"))
        self.label_2.setText(_translate("MainWindow", "version 2024.1.0"))
        self.label_3.setText(_translate("MainWindow", "Leonardo"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
