'''Расположен класс Ui_Window_DecrProgbar,
который описывает весь дизайн окна Decr_Progress_Bar'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_DecrProgbar(object):
    '''Описывает дизайн окна Decr_Progress_Bar'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]) + 240, int(geometry[1]) + 240, 480, 270)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(480, 270)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progBar_decr = QtWidgets.QProgressBar(self.centralwidget)
        self.progBar_decr.setGeometry(QtCore.QRect(70, 110, 331, 91))
        self.progBar_decr.setProperty("value", 0)
        self.progBar_decr.setAlignment(QtCore.Qt.AlignCenter)
        self.progBar_decr.setOrientation(QtCore.Qt.Horizontal)
        self.progBar_decr.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progBar_decr.setObjectName("progrBar_decr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 361, 31))
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER ->Decr Progress Bar"))
        self.label.setText(_translate("MainWindow", "Прогресс выполнения расшифрования"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_DecrProgbar()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
