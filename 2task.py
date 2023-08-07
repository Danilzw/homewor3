# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

max = int(input("Введите максимум:"))
min = int(input("Введите минимум:"))



array = []

resultarray = []

def fillarray(array):
    for i in range(8):
        array.append(random.randint(-10,+10))
    return array

print(fillarray(array))

def findindex(array,min,max,array2):
    for i in range(0,len(array)):
        if array[i] >= min and array[i] <= max:
            array2.append(i)
        
    
findindex(array,min,max,resultarray)

print(resultarray)