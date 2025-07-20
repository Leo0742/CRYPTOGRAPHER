'''Обработка нажатия на кнопку but_encr
Расположенна функция AES_shifr(), которая
шифрует файл и записывает значение ключа в файл key.txt'''

from cryptography.fernet import Fernet

def AES_shifr():
    '''Шифрует выбранный файл и записывает значение ключа в файл key.txt
    Возвращает содержимое зашифрованного файла в main'''

    key = Fernet.generate_key()
    f = Fernet(key)

    with open("Files/selected_file.txt", "r") as selected_file:
        file_path = selected_file.read()
        
    with open(file_path, 'rb') as file:
        text = file.read()
    
    crypt_text = f.encrypt(text)

    with open("Files/key.txt", 'w') as file:
        file.write(key.decode('utf-8'))
    file.close()

    return crypt_text
