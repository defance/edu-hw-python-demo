#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

data = {}

print("Демонстрационная программа.")
print("Введите help для получения списка доступных команд.")

while True:

    print("\nВведите команду:")
    command = input("> ")

    if command == "help":
        print("Список допустимых команд:")
        print("  add - добавить элемент в словарь")
        print("  has - проверить вхождение элемента")
        print("  get - получить элемент")
        print("  remove - удалить элемент")
        print("  exit - выйти из программы")
        print("  help - вывести эту справку")

    elif command == "add":
        print("Добавление нового элемента")
        key = input("Ключ: ")
        value = input("Значение: ")
        data[key] = value
        print("Запись добавлена")

    elif command == "has":
        print("Проверка вхождения записи")
        key = input("Ключ: ")
        if key in data:
            print("Запись присуствует")
        else:
            print("Запись отсутствует")

    elif command == "get":
        print("Получение записи из словаря")
        key = input("Ключ: ")
        if key in data:
            print("Значение: %s" % data[key])
        else:
            print("Связанное значение отсутствует")

    elif command == "remove":
        print("Удаление записи из словаря")
        key = input("Ключ: ")
        if key in data:
            del data[key]
            print("Запись успешна удалена")
        else:
            print("Связанная с ключом запись отстуствует")

    elif command == "list":
        print("Вывод значений из словаря")
        for (key, value) in sorted(data.items()):
            print("Ключ: %s, значение: %s" % (key, value))
        if not len(data):
            print("Словарь пустой")

    elif command == "exit":
        break

    else:
        print("Неизвестная команда")

print("Завершение работы")

