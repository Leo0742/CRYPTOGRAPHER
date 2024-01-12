import string
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding as padding_asymmetric

def DES_shifr():
    # Генерируем ключ и вектор инициализации
    all_characters = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(all_characters) for _ in range(16))
    iv = ''.join(random.choice(all_characters) for _ in range(8))
    key = key.encode()
    iv = iv.encode()

    # Создаем объект шифра и режим шифрования
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Шифруем сообщение
    message = b'Hello, world!'
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(message) + padder.finalize()
    crypt_text = encryptor.update(padded_data) + encryptor.finalize()

    file = open("Files/key.txt", 'wb')
    file.write(key)
    file.close()

    file = open("Files/DES_iv.txt", 'wb')
    file.write(iv)
    file.close()

    return crypt_text

#DES_shifr()
