'''Расположен класс Ui_Window_Chsafe,
который описывает весь дизайн окна Choice_safe'''


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_Chsafe(object):
    '''Описывает дизайн окна Choice_safe'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]) + 230, int(geometry[1]) + 230, 500, 288)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(500, 288)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_next = QtWidgets.QPushButton(self.centralwidget)
        self.but_next.setGeometry(QtCore.QRect(150, 190, 191, 61))
        self.but_next.setStyleSheet("font: 16pt \"Arial\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);")
        self.but_next.setObjectName("but_next")
        self.widget_rad = QtWidgets.QWidget(self.centralwidget)
        self.widget_rad.setGeometry(QtCore.QRect(20, 30, 461, 131))
        self.widget_rad.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 25px;")
        self.widget_rad.setObjectName("widget_rad")
        self.rab_new = QtWidgets.QRadioButton(self.widget_rad)
        self.rab_new.setGeometry(QtCore.QRect(10, 70, 421, 41))
        self.rab_new.setStyleSheet("font: 13pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.rab_new.setObjectName("rab_new")
        self.rab_this = QtWidgets.QRadioButton(self.widget_rad)
        self.rab_this.setGeometry(QtCore.QRect(10, 20, 441, 31))
        self.rab_this.setStyleSheet("font: 13pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: none;\n"
                                    "border: none;")
        self.rab_this.setObjectName("rab_this")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.rab_new.toggled.connect(self.on_radio)
        self.rab_this.toggled.connect(self.on_radio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Choicesafe"))
        self.but_next.setText(_translate("MainWindow", "Продолжить"))
        self.rab_new.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.rab_new.setText(_translate("MainWindow", "Выполнить операцию с копией файла"))
        self.rab_this.setText(_translate("MainWindow", "Выполнить операцию с данным файлом"))


    def on_radio(self):
        self.but_next.setStyleSheet("font: 75 italic 16pt \"Arial\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-style: outset;\n"
                                    "border-width: 5px;\n"
                                    "border-color: green;")

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_Chsafe()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
