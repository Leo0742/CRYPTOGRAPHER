'''Расположена функция Documentation, которая
выводит на экран руководство пользователя'''

import os
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

def Documentation():
    '''Выводит на экран Руководство пользователя'''

    global web
    web = QWebEngineView()
    web.resize(700, 400)
    web.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
    web.setWindowTitle("CRYPTOGRAPHER -> Documentation")  # Установка заголовка окна
    web.setWindowIcon(QIcon("Icons/main_icon.svg"))  # Установка иконки окна

    file_name = "Руководство пользователя.pdf"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    real_path = ''

    for i in file_path:
        if i == '\\':
            real_path += "/"
        else:
            real_path += i

    web.load(QUrl(real_path))
    web.show()
