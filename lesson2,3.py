#coding=utf-8

x = raw_input('Введите знак:\n')
str = raw_input('Введите строку:\n')
y = str.split(x)
print min(y, key = len)