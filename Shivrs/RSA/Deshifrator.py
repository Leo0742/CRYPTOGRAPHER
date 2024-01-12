from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def RSA_decrypt():
    print("RSA_1")
    file = open("Files/RSA_priv_key.pem", 'rb')  # Open the private key file
    private_key = serialization.load_pem_private_key(  # Load the private key
        file.read(),
        password=None
    )
    file.close()

    print("RSA_2")
    selected_file = open("Files/selected_file.txt", "r")
    cipher_text = open(selected_file.read(), 'rb').read()  # Read and store the content of the selected file
    selected_file.close()

    print("RSA_3")
    plaintext = private_key.decrypt(  # Decrypt the ciphertext using the private key
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("RSA_4")
    print(plaintext)
    return plaintext

#RSA_decrypt()
