'''Обработка нажатия на кнопку but_encrypt'''

from cryptography.fernet import Fernet

def AES_shifr():
    '''Шифрует выбранный файл, сохраняет его и сохраняет ключ'''

    key = Fernet.generate_key()
    f = Fernet(key)

    selected_file = open("Files/selected_file.txt", "r")
    file = open(str(selected_file.read()), 'rb')  # rb - будет считывать в бинарной строчке -> read binary
    text = file.read()
    selected_file.close()
    file.close()

    crypt_text = f.encrypt(text)

    file = open("Files/key.txt", 'w')
    file.write(key.decode('utf-8'))
    file.close()

    return crypt_text
