#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

def main():

    def help():
        print("Список допустимых команд:")
        print("  add - добавить элемент в словарь")
        print("  has - проверить вхождение элемента")
        print("  get - получить элемент")
        print("  remove - удалить элемент")
        print("  exit - выйти из программы")
        print("  help - вывести эту справку")

    def add_entry():
        print("Добавление нового элемента")
        key = input("Ключ: ")
        value = input("Значение: ")
        data[key] = value
        print("Запись добавлена")    
        
    def has_entry():
        print("Проверка вхождения записи")
        key = input("Ключ: ")
        if key in data:
            print("Запись присуствует")
        else:
            print("Запись отсутствует")        
            
    def get_entry():
        print("Получение записи из словаря")
        key = input("Ключ: ")
        if key in data:
            print("Значение: %s" % data[key])
        else:
            print("Связанное значение отсутствует")        
            
    def remove_entry():
        print("Удаление записи из словаря")
        key = input("Ключ: ")
        if key in data:
            del data[key]
            print("Запись успешна удалена")
        else:
            print("Связанная с ключом запись отстуствует")
            
    def get_entries():
        print("Вывод значений из словаря")
        for (key, value) in sorted(data.items()):
            print("Ключ: %s, значение: %s" % (key, value))
        if not len(data):
            print("Словарь пустой")
            
    def build_commands():
        return {
            'help': help,
            'add': add_entry,
            'has': has_entry,
            'get': get_entry,
            'remove': remove_entry,
            'list': get_entries,
        }

    data = {}
    commands = build_commands()

    print("Демонстрационная программа.")
    print("Введите help для получения списка доступных команд.")

    while True:

        print("\nВведите команду:")
        command = input("> ")
        
        if command in commands:
            commands[command]()
            
        elif command == "exit":
            print("Завершение работы")
            break

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()

