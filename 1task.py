# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

Element1 = int(input("Первый элемент:"))

Range = int(input("Разность:"))

quantity = int(input("Колл-во элементов:"))

array = []

def function(Element,Range,quantity,array):
    array.append(Element)
    for i in range(1,quantity):
        array.append(Element + Range)
        Element = Element + Range

function(Element1,Range,quantity,array)

print(array)