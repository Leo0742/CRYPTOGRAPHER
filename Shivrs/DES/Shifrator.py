'''Обработка нажатия на кнопку but_encr
Расположенна функция DES_shifr(), которая
шифрует файл и записывает значение ключа в файл key.txt,
значение вектора инициализации в DES_iv.txt'''

import string
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def DES_shifr():
    '''Шифрует выбранный файл и записывает значение ключа в файл key.txt,
    вектора инициализации в файл DES_iv.txt
    Возвращает содержимое зашифрованного файла в main'''

    # Генерируем ключ и вектор инициализации
    all_characters = string.ascii_letters + string.digits + '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~'''
    key = ''.join(random.choice(all_characters) for _ in range(16))
    iv = ''.join(random.choice(all_characters) for _ in range(8))
    key = key.encode()
    iv = iv.encode()

    # Создаем объект шифра и режим шифрования
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Шифруем сообщение
    selected_file = open("Files/selected_file.txt", "r")
    plaintext = open(selected_file.read(), 'rb').read()
    selected_file.close()

    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    crypt_text = encryptor.update(padded_data) + encryptor.finalize()

    file = open("Files/key.txt", 'wb')
    file.write(key)
    file.close()

    file = open("Files/DES_iv.txt", 'wb')
    file.write(iv)
    file.close()

    return crypt_text
