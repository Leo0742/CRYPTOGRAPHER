from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_error_window(object):
    '''Описывает дизайн окна Error'''

    def setupUi(self, error):
        error.setObjectName("MainWindow")
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
#     ui = Ui_error_window()
#     ui.setupUi(Error_Window)
#     Error_Window.show()
#     sys.exit(app.exec_())
