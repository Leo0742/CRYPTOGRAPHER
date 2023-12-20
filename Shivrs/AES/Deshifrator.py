'''Обработка нажатия на клавишу but_decr
Расположенна функция AES_deshif(), которая
принимает ключ из main, и дешифрует файл'''

from cryptography.fernet import Fernet

def AES_deshif():
    '''Считывает ключ, кодирует его в бинарный вид
    Дешифровывает файл и сохраняет его в файл  shifr.txt'''

    file = open("Files/key.txt", 'r')
    key = file.read()
    file.close()

    key = key.encode()

    f = Fernet(key)
    file = open("Files/shifr.txt", 'rb')  # rb - будет считывать в бинарной строчке -> read binary
    crypt_text = file.read()
    file.close()

    text = f.decrypt(crypt_text)
    file = open("Files/shifr.txt", 'wb')
    file.write(text)
    file.close()
