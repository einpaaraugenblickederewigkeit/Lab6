with open("Students.txt", "r") as f1:
    ask = input('Показать содержимое файла? (да/нет): ')
    data = f1.read()
    if ask == 'да':
        print('====Информация о файле====')
        print(data)

#Выбор имени, которое присутствует в файле
name = input("Введите имя для поиска: ")
if name in data:
    print("Это имя есть в файле")
else:
    print("Это имя отсутствует в файле")

# Сохранение имени в отдельный файл
ask1 = input('Сохранить имя в отдельный файл? (да/нет): ')
if ask1 == 'да':
    with open("Name.txt", "w") as f2:
        f2.write(name)
        print('Имя сохранено в "Name.txt"')
# Сохранение информации без выбранного имени в отдельный файл
ask2 = input('Сохранить информацию без этого имени в отдельный файл? (да/нет): ')
if ask2 == 'да':
    new_data = data.replace(name, "").strip()

    with open("Students_new.txt", "w") as f2:
        f2.write(new_data)
    print('Информация сохранена в "Students_new.txt"')