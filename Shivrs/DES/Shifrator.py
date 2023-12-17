'''Обработка нажатия на кнопку but_encrypt'''

from cryptography.fernet import Fernet

def DES_shifr():
    '''Шифрует выбранный файл, сохраняет его и сохраняет ключ'''

    key = Fernet.generate_key()
    f = Fernet(key)

    selected_file = open("selected_file", "r")
    file = open(str(selected_file.read()), 'rb')  # rb - будет считывать в бинарной строчке -> read binary
    text = file.read()
    file.close()

    crypt_text = f.encrypt(text)
    file = open("shifr.txt", 'wb')
    file.write(crypt_text)
    file.close()

    return key.decode('utf-8')


