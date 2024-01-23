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
        MainWindow.setGeometry(int(geometry[0]) + 240, int(geometry[1]) + 240, 480, 270)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(480, 270)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
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
        self.but_next.setGeometry(QtCore.QRect(160, 190, 171, 51))
        self.but_next.setStyleSheet("font: 14pt \"Arial\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);")
        self.but_next.setObjectName("but_next")
        self.widget_rad = QtWidgets.QWidget(self.centralwidget)
        self.widget_rad.setGeometry(QtCore.QRect(40, 30, 411, 131))
        self.widget_rad.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 25px;")
        self.widget_rad.setObjectName("widget_rad")
        self.rab_new = QtWidgets.QRadioButton(self.widget_rad)
        self.rab_new.setGeometry(QtCore.QRect(10, 70, 381, 41))
        self.rab_new.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.rab_new.setObjectName("rab_new")
        self.rab_this = QtWidgets.QRadioButton(self.widget_rad)
        self.rab_this.setGeometry(QtCore.QRect(10, 20, 391, 31))
        self.rab_this.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: none;\n"
                                    "border: none;")
        self.rab_this.setObjectName("rab_this")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Choicesafe"))
        self.but_next.setText(_translate("MainWindow", "Продолжить"))
        self.rab_new.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.rab_new.setText(_translate("MainWindow", "Выполнить операцию с копией файла"))
        self.rab_this.setText(_translate("MainWindow", "Выполнить операцию с данным файлом"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_Chsafe()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
