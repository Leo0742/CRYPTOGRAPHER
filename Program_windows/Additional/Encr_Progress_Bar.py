'''Расположен класс Ui_Window_EncrProgbar,
который описывает весь дизайн окна Encr_Progress_Bar'''


from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QProgressBar, QLabel

class Ui_Window_EncrProgbar(object):
    '''Описывает дизайн окна Encr_Progress_Bar'''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        MainWindow.setGeometry(int(geometry[0]) + 240, int(geometry[1]) + 240, 480, 270)  # !!!!!!!!!!!!!!!!!
        MainWindow.setFixedSize(480, 270)  # !!!!!!!!!!!!!!!!!!!!!!!!!!
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progBar_encr = QProgressBar(self.centralwidget)
        self.progBar_encr.setGeometry(70, 110, 331, 91)
        self.progBar_encr.setValue(0)
        self.progBar_encr.setAlignment(QtCore.Qt.AlignCenter)
        self.progBar_encr.setOrientation(QtCore.Qt.Horizontal)
        self.progBar_encr.setTextDirection(QProgressBar.BottomToTop)
        self.progBar_encr.setObjectName("progBar_encr")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(70, 40, 331, 31)
        self.label.setStyleSheet("font: 12pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTOGRAPHER -> Encr Progress Bar"))
        self.label.setText(_translate("MainWindow", "Прогресс выполнения шифрования"))


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = Ui_Window_EncrProgbar()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
