filename = input("Введите имя файла: ") + '.txt'

with open(filename, 'w') as f:
    text = input("Введите текст для записи в файл: ")
    text = text.upper()
    f.write(text)
    
print("Текст записан в файл", filename)