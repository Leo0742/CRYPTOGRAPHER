'''Обработка нажатия на клавишу but_decr
Расположенна функция DES_deshif(), которая
принимает ключ из main, и дешифрует файл'''

from cryptography.fernet import Fernet

def DES_deshif(key):
    '''Считывает ключ, кодирует его в бинарный вид
    Дешифровывает файл и сохраняет его в файл  shifr.txt'''

    key = key.encode()

    f = Fernet(key)
    file = open("Files/shifr.txt", 'rb')  # rb - будет считывать в бинарной строчке -> read binary
    crypt_text = file.read()
    file.close()

    text = f.decrypt(crypt_text)
    file = open("Files/shifr.txt", 'wb')
    file.write(text)
    file.close()
