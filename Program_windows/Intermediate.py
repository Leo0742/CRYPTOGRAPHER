'''Расположен класс Ui_Window_inter,
который описывает весь дизайн окна Intermediate'''

from PyQt5 import QtCore, QtGui, QtWidgets
import res


class Ui_Window_inter(object):
    '''Описывает дизайн окна Intermediate'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]), int(geometry[1]), 950, 750)  # !!!!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(950, 750)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.widget_ch_shif = QtWidgets.QWidget(self.centralwidget)
        self.widget_ch_shif.setGeometry(QtCore.QRect(90, 120, 761, 481))
        self.widget_ch_shif.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 25px;")
        self.widget_ch_shif.setObjectName("widget_ch_shif")
        self.label = QtWidgets.QLabel(self.widget_ch_shif)
        self.label.setGeometry(QtCore.QRect(30, 30, 721, 101))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 87 16pt \"Arial\";\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.but_decr = QtWidgets.QPushButton(self.widget_ch_shif)
        self.but_decr.setGeometry(QtCore.QRect(440, 315, 251, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/no_lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_decr.setIcon(icon2)
        self.but_decr.setFlat(True)
        self.but_decr.setObjectName("but_decr")
        self.but_encr = QtWidgets.QPushButton(self.widget_ch_shif)
        self.but_encr.setGeometry(QtCore.QRect(440, 185, 251, 71))
        self.but_encr.setStyleSheet("font: italic 16pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_encr.setIcon(icon3)
        self.but_encr.setFlat(True)
        self.but_encr.setObjectName("but_encr")
        self.Box_decr = QtWidgets.QComboBox(self.widget_ch_shif)
        self.Box_decr.setGeometry(QtCore.QRect(70, 330, 221, 51))
        self.Box_decr.setStyleSheet("font: 75 15pt \"Nirmala UI\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;\n"
                                    "background-image: url(:/Icons/security.svg);\n"
                                    "background-position: left;\n"
                                    "background-repeat: no-repeat;\n"
                                    "padding-left: 40px;")
        self.Box_decr.setObjectName("Box_decr")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        self.Box_decr.addItem("")
        self.Box_encr = QtWidgets.QComboBox(self.widget_ch_shif)
        self.Box_encr.setGeometry(QtCore.QRect(70, 195, 221, 51))
        self.Box_encr.setStyleSheet("font: 75 15pt \"Nirmala UI\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 20px;\n"
                                      "background-image: url(:/Icons/security.svg);\n"
                                      "background-position: left;\n"
                                      "background-repeat: no-repeat;\n"
                                      "padding-left: 40px;")
        self.Box_encr.setObjectName("Box_decr_2")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.Box_encr.addItem("")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border: 2px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;")
        self.but_back.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon4)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setFlat(True)
        self.but_back.setObjectName("but_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_encr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_decr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Intermediate"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\">Выберите алгоритм шифрования и операцию,</p><p align=\"center\">которую хотите выполнить с вашим файлом</p></body></html>"))
        self.but_decr.setText(_translate("MainWindow", "   Расшифровка"))
        self.but_encr.setText(_translate("MainWindow", "   Шифрование"))
        self.Box_decr.setItemText(0, _translate("MainWindow", "AES"))
        self.Box_decr.setItemText(1, _translate("MainWindow", "Triple DES"))
        self.Box_decr.setItemText(2, _translate("MainWindow", "RSA"))
        self.Box_encr.setItemText(0, _translate("MainWindow", "AES"))
        self.Box_encr.setItemText(1, _translate("MainWindow", "Triple DES"))
        self.Box_encr.setItemText(2, _translate("MainWindow", "RSA"))

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
#     ui = Ui_Window_inter()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
