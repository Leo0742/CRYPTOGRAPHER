'''Расположен класс Ui_Window_error,
который описывает весь дизайн окна Error'''

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Window_error(object):
    '''Описывает дизайн окна Error'''

    def setupUi(self, error):
        error.setObjectName("MainWindow")
        file = open("Files/Geometry.txt", 'r')  # !!!!!!!!!!!!!!!!!
        geometry = file.readlines()  # !!!!!!!!!!!!!!!!!
        file.close()  # !!!!!!!!!!!!!!!!!!!!!
        error.setGeometry(int(geometry[0]) + 250, int(geometry[1]) + 300, 0, 0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error.setWindowIcon(icon)
        error.setWindowTitle("Error")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok)
        error.setStyleSheet("")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Error_Window = QtWidgets.QMessageBox()
#     ui = Ui_Window_error()
#     ui.setupUi(Error_Window)
#     Error_Window.show()
#     sys.exit(app.exec_())
