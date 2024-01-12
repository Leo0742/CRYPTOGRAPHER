'''Расположен класс Ui_Window_main_screen,
который описывает весь дизайн окна main_screen'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_main_screen(object):
    '''Описывает дизайн окна main_screen'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_start = QtWidgets.QPushButton(self.centralwidget)
        self.but_start.setGeometry(QtCore.QRect(350, 350, 261, 91))
        self.but_start.setStyleSheet("font: 15pt \"Bauhaus 93\";\n"
"font: 20pt \"Forte\";")
        self.but_start.setObjectName("but_start")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(220, 130, 501, 81))
        self.label_1.setStyleSheet("font: 24pt \"MV Boli\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(870, 10, 71, 61))
        self.settings.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.settings.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon1)
        self.settings.setIconSize(QtCore.QSize(60, 60))
        self.settings.setObjectName("settings")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 670, 131, 51))
        self.label_3.setStyleSheet("font: italic 24pt \"Palace Script MT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.help.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 680, 171, 41))
        self.label_2.setStyleSheet("font: 6pt \"Terminal\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.but_start.setText(_translate("MainWindow", "Start"))
        self.label_1.setText(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.label_3.setText(_translate("MainWindow", "Leonardo"))
        self.label_2.setText(_translate("MainWindow", "version 2024.1.0"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_main_screen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
