#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

def add_entry(data, hash_function):
    print("Добавление нового элемента")
    key = input("Ключ: ")
    data[key] = hash_function(key)
    print("Запись добавлена")    
    
def has_entry(data):
    print("Проверка вхождения записи")
    key = input("Ключ: ")
    if key in data:
        print("Запись присуствует")
    else:
        print("Запись отсутствует")        
        
def get_entry(data, hash_function):
    print("Получение записи из словаря")
    key = input("Ключ: ")
    if not key in data:
        data[key] = hash_function(key)
    print("Значение: %s" % data[key])  
        
def remove_entry(data):
    print("Удаление записи из словаря")
    key = input("Ключ: ")
    if key in data:
        del data[key]
        print("Запись успешна удалена")
    else:
        print("Связанная с ключом запись отстуствует")
        
def get_entries(data):
    print("Вывод значений из словаря")
    for (key, value) in sorted(data.items()):
        print("Ключ: %s, значение: %s" % (key, value))
    if not len(data):
        print("Словарь пустой")

def update_entries(data, hash_function):
    for key in data.keys():
        data[key] = hash_function(key)

