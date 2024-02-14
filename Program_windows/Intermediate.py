'''Расположен класс Ui_Window_inter,
который описывает весь дизайн окна Intermediate'''

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtCore import QMetaObject, QCoreApplication
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
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addPixmap(QPixmap("Icons/main_icon.svg"), QIcon.Normal,
                       QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.help = QPushButton(self.centralwidget)
        self.help.setGeometry(QRect(860, 10, 81, 71))
        self.help.setFocusPolicy(Qt.WheelFocus)
        self.help.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                "border: 2px solid rgba(255, 255, 255, 40);\n"
                                "border-radius: 25px;")
        self.help.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("Icons/help.svg"), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon1)
        self.help.setIconSize(QSize(60, 60))
        self.help.setFlat(True)
        self.help.setObjectName("help")
        self.widget_ch_shif = QWidget(self.centralwidget)
        self.widget_ch_shif.setGeometry(QRect(90, 120, 761, 481))
        self.widget_ch_shif.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 25px;")
        self.widget_ch_shif.setObjectName("widget_ch_shif")
        self.label = QLabel(self.widget_ch_shif)
        self.label.setGeometry(QRect(30, 30, 721, 101))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 87 16pt \"Arial\";\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.but_decr = QPushButton(self.widget_ch_shif)
        self.but_decr.setGeometry(QRect(440, 315, 251, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("Icons/no_lock.svg"), QIcon.Normal, QIcon.Off)
        self.but_decr.setIcon(icon2)
        self.but_decr.setFlat(True)
        self.but_decr.setObjectName("but_decr")
        self.but_encr = QPushButton(self.widget_ch_shif)
        self.but_encr.setGeometry(QRect(440, 185, 251, 71))
        self.but_encr.setStyleSheet("font: italic 16pt \"Arial\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("Icons/lock.svg"), QIcon.Normal, QIcon.Off)
        self.but_encr.setIcon(icon3)
        self.but_encr.setFlat(True)
        self.but_encr.setObjectName("but_encr")
        self.Box_decr = QComboBox(self.widget_ch_shif)
        self.Box_decr.setGeometry(QRect(70, 330, 221, 51))
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
        self.Box_encr = QComboBox(self.widget_ch_shif)
        self.Box_encr.setGeometry(QRect(70, 195, 221, 51))
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
        self.but_back = QPushButton(self.centralwidget)
        self.but_back.setGeometry(QRect(10, 10, 71, 61))
        self.but_back.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "border: 2px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;")
        self.but_back.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap("Icons/back.svg"), QIcon.Normal, QIcon.Off)
        self.but_back.setIcon(icon4)
        self.but_back.setIconSize(QSize(50, 50))
        self.but_back.setFlat(True)
        self.but_back.setObjectName("but_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.but_encr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_decr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
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
