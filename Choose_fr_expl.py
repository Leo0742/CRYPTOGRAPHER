'''Обработка нажатия на клавишу but_exlor
Расположена функция Choose_fr_expl, которая
Открывает Проводник и записывает местоположение
выбранного файла в файл selected_file'''

from PyQt5.QtWidgets import QFileDialog


def Choose_fr_expl():
    '''Обрабатывает и запоминает выбранный файл'''

    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)

    file = open('Files/selected_file.txt', 'w')
    file.write('')
    if file_dialog.exec_():
        file.write(file_dialog.selectedFiles()[0])

    file.close()
