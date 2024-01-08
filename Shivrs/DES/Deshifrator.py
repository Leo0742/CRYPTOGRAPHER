from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def DES_decrypt():
    file = open("Files/key.txt", 'r')
    key = file.read()
    file.close()

    file = open("Files/DES_iv.txt", 'r')
    iv = file.read()
    file.close()

    key = key.encode()
    iv = iv.encode()

    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())

    file = open("Files/shifr.txt", 'rb')  # Open the file in binary mode
    ct = file.read()
    file.close()

    # Расшифровываем сообщение
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct) + decryptor.finalize()  # Расшифровываем сообщение
    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
    pt = unpadder.update(pt) + unpadder.finalize()  # Удаляем дополнение

    # Выводим результат
    file = open("Files/shifr.txt", 'w')
    file.write(pt.decode('utf-8')) # Convert bytes to string for printing
    file.close()

#DES_decrypt()
