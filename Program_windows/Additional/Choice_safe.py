'''Расположен класс Ui_Window_Chsafe,
который описывает весь дизайн окна Choice_safe'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_Chsafe(object):
    '''Описывает дизайн окна Choice_safe'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 270)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rab_this = QtWidgets.QRadioButton(self.centralwidget)
        self.rab_this.setGeometry(QtCore.QRect(40, 50, 391, 31))
        self.rab_this.setStyleSheet("font: 12pt \"Arial\";")
        self.rab_this.setObjectName("rab_this")
        self.rab_new = QtWidgets.QRadioButton(self.centralwidget)
        self.rab_new.setGeometry(QtCore.QRect(40, 100, 471, 41))
        self.rab_new.setStyleSheet("font: 12pt \"Arial\";")
        self.rab_new.setObjectName("rab_new")
        self.but_next = QtWidgets.QPushButton(self.centralwidget)
        self.but_next.setGeometry(QtCore.QRect(160, 180, 161, 51))
        self.but_next.setStyleSheet("font: 12pt \"Arial\";")
        self.but_next.setObjectName("but_next")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setFixedSize(480, 270)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Choicesafe"))
        self.rab_this.setText(_translate("MainWindow", "Выполнить операцию с данным файлом"))
        self.rab_new.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.rab_new.setText(_translate("MainWindow", "Выполнить операцию с копией файла"))
        self.but_next.setText(_translate("MainWindow", "Продолжить"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_Chsafe()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
