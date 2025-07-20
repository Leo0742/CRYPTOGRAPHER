'''Расположена функция Cleaner, которая
очищает содержимое всех файлов из папки Files'''

def Cleaner():
    '''Очищает содержимое файлов из папки Files'''
    
    files_to_clean = [
        "Files/selected_file.txt",
        "Files/key.txt",
        "Files/RSA_pub_key.pem",
        "Files/RSA_priv_key.pem",
        "Files/DES_iv.txt",
        "Files/flag_value.txt"
    ]
    
    for file_path in files_to_clean:
        with open(file_path, 'w') as file:
            file.write('')
