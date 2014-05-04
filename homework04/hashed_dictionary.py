#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

import dictionary

class HashedDictionary(dictionary.Dictionary):

    @property
    def hash_function(self): return self._hash_function
    
    @hash_function.setter
    def hash_function(self, value):
        if value is not None:
            self._hash_function = value
            self._update_entries()

    def __init__(self, hash_function=None):
        super().__init__()
        self._hash_function = hash_function
        
    def add_entry(self):
        print("Добавление нового элемента")
        key = input("Ключ: ")
        self._data[key] = self._hash_function(key)
        print("Запись добавлена")  
        
    def get_entry(self):
        print("Получение записи из словаря")
        key = input("Ключ: ")
        if not key in self._data:
            self._data[key] = self._hash_function(value)
        print("Значение: %s" % self._data[key])

    def _update_entries(self):
        for key in self._data.keys():
            self._data[key] = self._hash_function(key)

