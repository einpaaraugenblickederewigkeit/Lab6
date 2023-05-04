with open('Books.csv', mode='a') as file: #Файл вписывает в Books.csv данные о новой книге и выводит содержмое файла
    book_data = input("Введите новую запись в формате 'Наименование книги, Писатель / Автор, Страна автора, Год издания': ")
    file.write(book_data + '\n')

import csv

with open('Books.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)