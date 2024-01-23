'''Расположен класс Ui_Window_EncrProgbar,
который описывает весь дизайн окна Encr_Progress_Bar'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_EncrProgbar(object):
    '''Описывает дизайн окна Encr_Progress_Bar'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]) + 240, int(geometry[1]) + 240, 480, 270)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(480, 270)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progBar_encr = QtWidgets.QProgressBar(self.centralwidget)
        self.progBar_encr.setGeometry(QtCore.QRect(80, 120, 331, 91))
        self.progBar_encr.setProperty("value", 0)
        self.progBar_encr.setAlignment(QtCore.Qt.AlignCenter)
        self.progBar_encr.setOrientation(QtCore.Qt.Horizontal)
        self.progBar_encr.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progBar_encr.setObjectName("progBar_encr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 411, 41))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
                                 "background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 15px;\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER ->Encr Progress Bar"))
        self.label.setText(_translate("MainWindow", "Прогресс выполнения шифрования"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_EncrProgbar()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
