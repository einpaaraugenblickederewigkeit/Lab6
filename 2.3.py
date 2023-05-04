import csv

# Открываем файл для чтения и создаем список записей
with open('Books.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    books_list = [row for row in reader]

# Запрашиваем у пользователя данные новой записи и добавляем ее в список
num_records = int(input("Сколько записей вы хотите добавить? "))
for i in range(num_records):
    new_record = []
    name = input("Введите наименование книги: ")
    author = input("Введите автора книги: ")
    country = input("Введите страну автора: ")
    year = input("Введите год издания: ")
    new_record.extend([name, author, country, year])
    books_list.append(new_record)

# Перезаписываем файл Books.csv с обновленными данными
with open('Books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(books_list)

