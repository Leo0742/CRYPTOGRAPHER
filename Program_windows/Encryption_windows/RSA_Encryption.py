'''Расположен класс Ui_Window_encr_RSA,
который описывает весь дизайн окна RSA_Encryption'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class Ui_Window_encr_RSA(object):
    '''Описывает дизайн окна RSA_Encryption'''

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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(190, 95, 411, 71))
        self.label_1.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_1.setObjectName("label_1")
        self.but_exlor = QtWidgets.QPushButton(self.centralwidget)
        self.but_exlor.setGeometry(QtCore.QRect(620, 110, 111, 41))
        self.but_exlor.setStyleSheet("font: 10pt \"Segoe Print\";")
        self.but_exlor.setObjectName("but_exlor")
        self.but_encr = QtWidgets.QPushButton(self.centralwidget)
        self.but_encr.setGeometry(QtCore.QRect(370, 270, 171, 61))
        self.but_encr.setStyleSheet("font: italic 14pt \"Courier New\";")
        self.but_encr.setObjectName("but_encr")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 420, 271, 71))
        self.label_2.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.but_copy_op = QtWidgets.QPushButton(self.centralwidget)
        self.but_copy_op.setGeometry(QtCore.QRect(720, 425, 151, 61))
        self.but_copy_op.setStyleSheet("font: italic 13pt \"Courier New\";")
        self.but_copy_op.setObjectName("but_copy_op")
        self.but_back = QtWidgets.QPushButton(self.centralwidget)
        self.but_back.setGeometry(QtCore.QRect(10, 10, 71, 61))
        self.but_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.but_back.setIcon(icon1)
        self.but_back.setIconSize(QtCore.QSize(50, 50))
        self.but_back.setObjectName("but_back")
        self.key_label_op = QtWidgets.QLineEdit(self.centralwidget)
        self.key_label_op.setGeometry(QtCore.QRect(300, 430, 341, 51))
        self.key_label_op.setStyleSheet("font: 14pt \"Arial\";")
        self.key_label_op.setObjectName("key_label_op")
        self.key_label_op.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(850, 660, 93, 71))
        self.help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help.setIcon(icon2)
        self.help.setIconSize(QtCore.QSize(60, 60))
        self.help.setObjectName("help")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 500, 271, 71))
        self.label_3.setStyleSheet("font: italic 15pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.but_copy_cl = QtWidgets.QPushButton(self.centralwidget)
        self.but_copy_cl.setGeometry(QtCore.QRect(720, 505, 151, 61))
        self.but_copy_cl.setStyleSheet("font: italic 13pt \"Courier New\";")
        self.but_copy_cl.setObjectName("but_copy_cl")
        self.key_label_cl = QtWidgets.QLineEdit(self.centralwidget)
        self.key_label_cl.setGeometry(QtCore.QRect(300, 510, 341, 51))
        self.key_label_cl.setStyleSheet("font: 14pt \"Arial\";")
        self.key_label_cl.setObjectName("key_label_cl")
        self.key_label_cl.setEchoMode(QLineEdit.Password)  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.key_op_on_off = QtWidgets.QPushButton(self.centralwidget)
        self.key_op_on_off.setGeometry(QtCore.QRect(650, 425, 61, 61))
        self.key_op_on_off.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/key_off.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.key_op_on_off.setIcon(icon3)
        self.key_op_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_op_on_off.setObjectName("key_op_on_off")
        self.key_cl_on_off = QtWidgets.QPushButton(self.centralwidget)
        self.key_cl_on_off.setGeometry(QtCore.QRect(650, 505, 61, 61))
        self.key_cl_on_off.setText("")
        self.key_cl_on_off.setIcon(icon3)
        self.key_cl_on_off.setIconSize(QtCore.QSize(30, 30))
        self.key_cl_on_off.setObjectName("key_cl_on_off")
        self.but_file = QtWidgets.QPushButton(self.centralwidget)
        self.but_file.setGeometry(QtCore.QRect(760, 100, 61, 61))
        self.but_file.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/file_NO.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.but_file.setIcon(icon4)
        self.but_file.setIconSize(QtCore.QSize(60, 100))
        self.but_file.setFlat(True)
        self.but_file.setObjectName("but_file")
        MainWindow.setCentralWidget(self.centralwidget)

        self.but_back.clicked.connect(lambda: self.go_new_window(MainWindow))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> RSA -> Encryption"))
        self.label_1.setText(_translate("MainWindow", "Выбирите файл для шифрования"))
        self.but_exlor.setText(_translate("MainWindow", "Обзор"))
        self.but_encr.setText(_translate("MainWindow", "Зашифровать"))
        self.label_2.setText(_translate("MainWindow", "Ваш открытый ключ:"))
        self.but_copy_op.setText(_translate("MainWindow", "Скопировать"))
        self.label_3.setText(_translate("MainWindow", "Ваш закрытый ключ:"))
        self.but_copy_cl.setText(_translate("MainWindow", "Скопировать"))

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
#     ui = Ui_Window_encr_RSA()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
