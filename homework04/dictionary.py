#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

class Dictionary:

    def __init__(self):
        self._data = {}

    def add_entry(self):
        print("Добавление нового элемента")
        key = input("Ключ: ")
        value = input("Значение: ")
        self._data[key] = value
        print("Запись добавлена")    
    
    def has_entry(self):
        print("Проверка вхождения записи")
        key = input("Ключ: ")
        if key in self._data:
            print("Запись присуствует")
        else:
            print("Запись отсутствует")        
        
    def get_entry(self):
        print("Получение записи из словаря")
        key = input("Ключ: ")
        if key in self._data:
            print("Значение: %s" % self._data[key])
        else:
            print("Запись отсутствует")    
        
    def remove_entry(self):
        print("Удаление записи из словаря")
        key = input("Ключ: ")
        if key in self._data:
            del self._data[key]
            print("Запись успешна удалена")
        else:
            print("Связанная с ключом запись отстуствует")
        
    def get_entries(self):
        print("Вывод значений из словаря")
        for (key, value) in sorted(self._data.items()):
            print("Ключ: %s, значение: %s" % (key, value))
        if not len(self._data):
            print("Словарь пустой")

