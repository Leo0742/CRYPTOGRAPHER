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
    selected_file = open("Files/selected_file.txt", "r")
    crypt_text = open(selected_file.read(), 'rb').read()  # Read and store the content of the selected file
    selected_file.close()

    plaintext = f.decrypt(crypt_text)

    return plaintext
