'''Обработка нажатия на кнопку but_encr
Расположенна функция RSA_shifr(), которая
шифрует файл и записывает значение ключей в файлы:
RSA_priv_key.pem, RSA_pub_key.pem'''

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def RSA_shifr():
    '''Шифрует выбранный файл и записывает значение ключей в файлы:
    RSA_priv_key.pem, RSA_pub_key.pem
    Возвращает содержимое зашифрованного файла в main'''

    # Generate keys
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Get the public key
    public_key = private_key.public_key()

    # Encrypt the text
    selected_file = open("Files/selected_file.txt", "r")
    file_content = open(selected_file.read(), 'rb').read()  # Read and store the content of the selected file
    selected_file.close()

    crypt_text = public_key.encrypt(
        file_content,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open("Files/RSA_priv_key.pem", 'wb') as file:
        file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))
    with open("Files/RSA_pub_key.pem", 'wb') as file:
        file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    return crypt_text
