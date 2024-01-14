'''Обработка нажатия на клавишу but_decr
Расположенна функция DES_decrypt(), которая
принимает ключ и вектор инициализации из main, и расшифровывает файл'''

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def DES_decrypt():
    '''Считывает ключ и вектор инициализации
    из файлов key.txt, DES_iv.txt
    Расшифрованное содержимое файла возвращает в main'''

    file = open("Files/key.txt", 'r')
    key = file.read()
    file.close()

    file = open("Files/DES_iv.txt", 'r')
    iv = file.read()
    file.close()

    key = key.encode()
    iv = iv.encode()

    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

    selected_file = open("Files/selected_file.txt", "r")
    crypt_text = open(selected_file.read(), 'rb').read()  # Read and store the content of the selected file
    selected_file.close()

    # Расшифровываем сообщение
    decryptor = cipher.decryptor()
    pt = decryptor.update(crypt_text) + decryptor.finalize()  # Расшифровываем сообщение
    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    plaintext = unpadder.update(pt) + unpadder.finalize()  # Удаляем дополнения

    #plaintext = plaintext.decode('utf-8')
    return plaintext

#DES_decrypt()
