#!/usr/bin/env python 
# -*- coding: utf-8 -*-

__author__ = "Dmitry Ivanyushin"

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
