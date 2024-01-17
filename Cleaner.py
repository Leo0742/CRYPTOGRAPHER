'''Расположена функция Cleaner, которая
очищает содержимое всех файлов из папки Files'''

def Cleaner():
    '''Очищает содержимое файлов из папки Files'''

    file = open("Files/selected_file.txt", 'w')
    file.write('')
    file.close()

    file = open("Files/key.txt", 'w')
    file.write('')
    file.close()

    file = open("Files/RSA_pub_key.pem", 'w')
    file.write('')
    file.close()

    file = open("Files/RSA_priv_key.pem", 'w')
    file.write('')
    file.close()

    file = open("Files/DES_iv.txt", 'w')
    file.write('')
    file.close()

    file = open("Files/flag_value.txt", 'w')
    file.write('')
    file.close()
