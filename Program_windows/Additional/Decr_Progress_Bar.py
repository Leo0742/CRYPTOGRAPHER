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
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progrBar_decr = QtWidgets.QProgressBar(self.centralwidget)
        self.progrBar_decr.setGeometry(QtCore.QRect(70, 120, 331, 91))
        self.progrBar_decr.setStyleSheet("")
        self.progrBar_decr.setProperty("value", 0)
        self.progrBar_decr.setAlignment(QtCore.Qt.AlignCenter)
        self.progrBar_decr.setOrientation(QtCore.Qt.Horizontal)
        self.progrBar_decr.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progrBar_decr.setObjectName("progrBar_decr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 421, 41))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Decr Progress Bar"))
        self.label.setText(_translate("MainWindow", "Прогресс выполнения расшифровки"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_DecrProgbar()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
