'''Обработка нажатия на клавишу but_exlor
Расположена функция Choose_fr_expl, которая
Открывает Проводник и записывает местоположение
выбранного файла в файл selected_file'''

from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


def Choose_fr_expl():
    '''Обрабатывает и запоминает выбранный файл'''

    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)

    file = open('selected_file', 'w')
    file.write('')
    if file_dialog.exec_():
        file.write(file_dialog.selectedFiles()[0])

    file.close()
