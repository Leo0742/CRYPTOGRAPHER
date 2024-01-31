'''Расположен класс Ui_Window_decr_AES,
который описывает весь дизайн окна AES_Decryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_Window_decr_AES(object):
    '''Описывает дизайн окна AES_Decryption'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]), int(geometry[1]), 950, 750)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(950, 750)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_decr = QtWidgets.QPushButton(self.centralwidget)
        self.but_decr.setGeometry(QtCore.QRect(380, 560, 211, 71))
        self.but_decr.setStyleSheet("font: italic 16pt \"Courier New\";\n"
                                    "background-color: rgba(255, 255, 255, 30);\n"
                                    "border: 1px solid rgba(255, 255, 255, 40);\n"
                                    "border-radius: 25px;\n"
                                    "color: rgb(255, 255, 255);")
        self.but_decr.setObjectName("but_decr")
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
        self.widget_key = QtWidgets.QWidget(self.centralwidget)
        self.widget_key.setGeometry(QtCore.QRect(90, 310, 761, 171))
        self.widget_key.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 25px;")
        self.widget_key.setObjectName("widget_key")
        self.but_insert = QtWidgets.QPushButton(self.widget_key)
        self.but_insert.setGeometry(QtCore.QRect(590, 60, 161, 61))
        self.but_insert.setStyleSheet("font: italic 16pt \"Courier New\";\n"
                                      "color: rgb(255, 255, 255);")
        self.but_insert.setObjectName("but_insert")
        self.key_on_off = QtWidgets.QPushButton(self.widget_key)
        self.key_on_off.setGeometry(QtCore.QRect(520, 60, 61, 61))
        self.key_on_off.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/key_OFF.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.key_on_off.setIcon(icon2)
        self.key_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_on_off.setObjectName("key_on_off")
        self.label_2 = QtWidgets.QLabel(self.widget_key)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 151, 71))
        self.label_2.setStyleSheet("font: italic 16pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.key_label = QtWidgets.QLineEdit(self.widget_key)
        self.key_label.setGeometry(QtCore.QRect(170, 65, 341, 51))
        self.key_label.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "background-image: url(:/Icons/key.svg);\n"
                                     "background-position: left;\n"
                                     "background-repeat: no-repeat;\n"
                                     "padding-left: 30px;")
        self.key_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.key_label.setObjectName("key_label")
        self.key_label.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.widget_file = QtWidgets.QWidget(self.centralwidget)
        self.widget_file.setGeometry(QtCore.QRect(130, 110, 681, 121))
        self.widget_file.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 25px;")
        self.widget_file.setObjectName("widget_file")
        self.but_file = QtWidgets.QPushButton(self.widget_file)
        self.but_file.setGeometry(QtCore.QRect(610, 30, 61, 61))
        self.but_file.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.but_file.setIcon(icon3)
        self.but_file.setIconSize(QtCore.QSize(60, 100))
        self.but_file.setFlat(True)
        self.but_file.setObjectName("but_file")
        self.label_1 = QtWidgets.QLabel(self.widget_file)
        self.label_1.setGeometry(QtCore.QRect(10, 25, 431, 71))
        self.label_1.setStyleSheet("font: italic 15pt \"Arial\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.but_exlor = QtWidgets.QPushButton(self.widget_file)
        self.but_exlor.setGeometry(QtCore.QRect(460, 40, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius: 20px;")
        self.but_exlor.setObjectName("but_exlor")
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.but_back.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_file.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_exlor.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_insert.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.but_decr.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> AES -> Decryption"))
        self.but_decr.setText(_translate("MainWindow", "Расшифровать"))
        self.but_insert.setText(_translate("MainWindow", "Вставить"))
        self.label_2.setText(_translate("MainWindow", "Ваш ключ:"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для расшифровки"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))


    def go_new_window(self, MainWindow):
        x = MainWindow.geometry().x()
        y = MainWindow.geometry().y()

        file = open("Files/Geometry.txt", 'w')
        file.write(str(x) + '\n')
        file.write(str(y))
        file.close()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_Window_decr_AES()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
