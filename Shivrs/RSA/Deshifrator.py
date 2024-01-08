from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def RSA_decrypt():
    file = open("Files/RSA_priv_key.pem", 'rb')  # Open the private key file
    private_key = serialization.load_pem_private_key(  # Load the private key
        file.read(),
        password=None
    )
    file.close()

    file = open("Files/shifr.txt", 'rb')
    cipher_text = file.read()
    file.close()

    plaintext = private_key.decrypt(  # Decrypt the ciphertext using the private key
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    file = open("Files/shifr.txt", 'wb')  # Open the plaintext file in write mode
    file.write(plaintext)  # Write the decrypted plaintext to the file
    file.close()

# RSA_decrypt()
