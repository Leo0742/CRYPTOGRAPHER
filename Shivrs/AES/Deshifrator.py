'''Обработка нажатия на клавишу but_decr
Расположенна функция AES_decrypt(), которая
принимает ключ из main, и расшифровывает файл'''

from cryptography.fernet import Fernet

def AES_decrypt():
    '''Считывает ключ, кодирует его в бинарный вид
    Расшифрованное содержимое файла возвращает в main'''

    file = open("Files/key.txt", 'r')
    key = file.read()
    file.close()

    key = key.encode()

    f = Fernet(key)
    selected_file = open("Files/selected_file.txt", "r")
    crypt_text = open(selected_file.read(), 'rb').read()
    selected_file.close()

    plaintext = f.decrypt(crypt_text)

    return plaintext
