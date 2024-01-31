'''Расположен класс Ui_Window_main_screen,
который описывает весь дизайн окна main_screen'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_main_screen(object):
    '''Описывает дизайн окна main_screen'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]), int(geometry[1]), 950, 750) # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(950, 750) # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_start = QtWidgets.QPushButton(self.centralwidget)
        self.but_start.setGeometry(QtCore.QRect(340, 400, 261, 91))
        self.but_start.setStyleSheet("font: 22pt \"Forte\";\n"
                                     "background-color: rgba(255, 255, 255, 30);\n"
                                     "border: 1px solid rgba(255, 255, 255, 40);\n"
                                     "border-radius: 25px;\n"
                                     "color: rgb(255, 255, 255);")
        self.but_start.setFlat(True)
        self.but_start.setObjectName("but_start")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(220, 160, 501, 121))
        self.label_1.setStyleSheet("font: 30pt \"MV Boli\";\n"
                                   "background-color: rgba(255, 255, 255, 30);\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 30px;\n"
                                   "color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_sign = QtWidgets.QLabel(self.centralwidget)
        self.label_sign.setGeometry(QtCore.QRect(780, 648, 151, 51))
        self.label_sign.setStyleSheet("font: italic 30pt \"Palace Script MT\";\n"
                                   "color: rgb(255, 170, 0);\n"
                                   "background-color: rgba(255, 255, 255, 30);\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "border: none;\n"
                                   "border-radius: 20px;")
        self.label_sign.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sign.setObjectName("label_3")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(860, 10, 81, 71))
        self.help.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.help.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "border: 2px solid rgba(255, 255, 255, 40);\n"
                                "border-radius: 25px;")
        self.help.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setFlat(True)
        self.help.setObjectName("help")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(30, 650, 191, 41))
        self.label_version.setStyleSheet("font: 6pt \"Terminal\";\n"
                                   "background-color: rgba(255, 255, 255, 30);\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "border: none;\n"
                                   "border-radius: 20px;\n"
                                   "color: rgb(255, 170, 0);\n")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_4")

        self.but_icon = QtWidgets.QPushButton(self.centralwidget)
        self.but_icon.setGeometry(QtCore.QRect(15, 15, 81, 71))
        self.but_icon.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;")
        self.but_icon.setText("")
        self.but_icon.setIcon(icon)
        self.but_icon.setIconSize(QtCore.QSize(60, 60))
        self.but_icon.setFlat(True)
        self.but_icon.setObjectName("but_icon")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_start.clicked.connect(lambda: self.go_new_window(MainWindow)) # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.but_start.setText(_translate("MainWindow", "Start"))
        self.label_1.setText(_translate("MainWindow", "CRYPTOGRAPHER"))
        self.label_sign.setText(_translate("MainWindow", "Leonardo"))
        self.label_version.setText(_translate("MainWindow", "version 2024.1.0"))

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
#     ui = Ui_Window_main_screen()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
