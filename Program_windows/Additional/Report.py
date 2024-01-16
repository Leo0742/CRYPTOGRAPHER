'''Расположен класс Ui_Window_report,
который описывает весь дизайн окна Report'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window_report(object):
    '''Описывает дизайн окна Report'''

    def setupUi(self, report):
        report.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/main_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        report.setWindowIcon(icon)
        report.setWindowTitle("Report")
        report.setIcon(QtWidgets.QMessageBox.Information)
        report.setStandardButtons(QtWidgets.QMessageBox.Ok)
        report.setStyleSheet("")

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Report_Window = QtWidgets.QMessageBox()
#     ui = Ui_Window_report()
#     ui.setupUi(Report_Window)
#     Report_Window.show()
#     sys.exit(app.exec_())