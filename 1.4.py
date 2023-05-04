filename = input("Введите имя файла: ") + '.txt' #Программа создает файл имя которого указал пользователь и пользователь вписывает в него текст

with open(filename, 'w') as f:
    text = input("Введите текст для записи в файл: ")
    text = text.upper()
    f.write(text)
    
print("Текст записан в файл", filename)