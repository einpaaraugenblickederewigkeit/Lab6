with open('Students.txt', 'a+') as file: #Програма добавляет новое имя в файл
    file.write(input("Введите новое имя: ") + '\n')
    file.seek(0)
    print(file.read())