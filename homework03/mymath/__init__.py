#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

from .linear import *
from .trigonometry import *

def value_or_error(function, target_type):
    """
    Возвращает функцию, которая пытается вычислить значение
    переданной функции, приводя аргумент к указанному типу. 
    """
    def f(value):
        try:
            return function(target_type(value))
        except (TypeError, ValueError):
            return "(Ошибка вычислений)"
    return f
