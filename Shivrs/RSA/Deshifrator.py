'''Обработка нажатия на кнопку but_decr
Расположенна функция RSA_decrypt(), которая принимает
закрытый и открытый ключи шифрования из main и расшифровывает файл'''

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def RSA_decrypt():
    '''Считывает ключи из файлов RSA_priv_key.pem, RSA_pub_key.pem
    Расшифрованное содержимое файла возвращает в main'''

    file = open("Files/RSA_priv_key.pem", 'rb')
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None
    )
    file.close()

    selected_file = open("Files/selected_file.txt", "r")
    cipher_text = open(selected_file.read(), 'rb').read()
    selected_file.close()

    plaintext = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext
