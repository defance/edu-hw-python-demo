#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

import mymath

from dictionary import add_entry, has_entry, get_entry, remove_entry, get_entries, update_entries

def main():

    def help():
        print("Список допустимых команд:")
        print("  fun - выбор хеширующей функции")
        print("  add - добавить элемент в словарь")
        print("  has - проверить вхождение элемента")
        print("  get - получить элемент")
        print("  remove - удалить элемент")
        print("  exit - выйти из программы")
        print("  help - вывести эту справку")
        
    def select_hash():
        nonlocal hash_function
        print("Список доступных функций: sin, cos, fib")
        f = input("> ")
        hash_function = hash_functions.get(f)
        if hash_function is None:
            print("Неизвестная функция")
        else:
            update_entries(data, hash_function)
            
    def build_commands():
        return {
            'help':   help,
            'add':    lambda : add_entry(data, hash_function),
            'has':    lambda : has_entry(data),
            'get':    lambda : get_entry(data, hash_function),
            'remove': lambda : remove_entry(data),
            'list':   lambda : get_entries(data),
            'fun':    select_hash,
        }
        
    def build_hash_functions():
        return {
            'sin': lambda x: mymath.value_or_error(mymath.sin, float)(x),
            'cos': lambda x: mymath.value_or_error(mymath.cos, float)(x),
            'fib': lambda x: mymath.value_or_error(mymath.fib, int)(x),
        }

    data = {}
    commands = build_commands()
    hash_functions = build_hash_functions()
    hash_function = None

    print("Демонстрационная программа.")
    print("Введите help для получения списка доступных команд.")

    while True:
    
        if hash_function is None:
            print("\nНе выбрана хеширующая функция")
            command = 'fun'            
        else:
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

