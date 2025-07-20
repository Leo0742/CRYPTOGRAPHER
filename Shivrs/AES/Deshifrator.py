'''Обработка нажатия на клавишу but_decr
Расположенна функция AES_decrypt(), которая
принимает ключ из main, и расшифровывает файл'''

from cryptography.fernet import Fernet

def AES_decrypt():
    try:
        with open("Files/key.txt", 'r') as file:
            key = file.read()

        key = key.encode()

        f = Fernet(key)
        with open("Files/selected_file.txt", "r") as selected_file:
            file_path = selected_file.read()
            
        with open(file_path, 'rb') as file:
            crypt_text = file.read()

        plaintext = f.decrypt(crypt_text)
        return plaintext
    except FileNotFoundError:
        raise Exception("Файл не найден. Проверьте путь к файлу.")
    except Exception as e:
        raise Exception(f"Ошибка при дешифровании: {str(e)}")

    return plaintext
