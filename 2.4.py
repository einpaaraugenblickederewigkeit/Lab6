import csv

#Код для запроса на вывод книг указанного автора

author = input("Введите имя автора: ")

with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    found = False
    for row in reader:
        if author.lower() == row[1].lower():
            found = True
            print(row[0])
        
    if not found:
        print("Книг данного автора нет в списке")

print('===========================')

#Код для запроса на вывод книг, используя заданный промежуток времени

start_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))

with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader, 1):
        if i >= 2 and start_year <= int(row[3]) <= end_year:
            print(f"{i}. {row[0]} ({row[1]}, {row[2]}, {row[3]})")

print('===========================')

#Код для запроса на вывод данных с нумерацией строк

with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader, 1):
        print(f"{i}. {row[0]} ({row[1]}, {row[2]}, {row[3]})")

#Код для изменения данных в файле

with open("Books.csv", "r", newline="") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)

# удаляем строку с указанным порядковым номером
index = int(input("Введите номер строки, которую нужно удалить: "))
del data[index - 1]

print('===========================')

# изменяем название, автора и год издания
index = int(input("Введите номер строки, которую нужно изменить: ")) - 1
title = input("Введите новое название книги: ")
author = input("Введите новое имя автора: ")
country = input("Введите страну автора: ")
year = input("Введите год издания: ")
data[index] = [title, author, country, year]

# записываем измененные данные в файл
with open("Books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
