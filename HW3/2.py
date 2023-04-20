# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n=int(input("Введите количество элементов массива"))
list=[]
for i in range(1, n+1):
    list.append(i)
print(list)
x=int(input("Введите искомое число"))
y=0
count=x
searchnumber=x
for i in range(0, len(list)):
    if x>list[i]:
        y=x-list[i]
    else:
        y=list[i]-x
    if count>y:
        count=y
        searchnumber=list[i]
for i in range(0, len(list)):
    if x==list[i]:
         searchnumber=list[i]
print(searchnumber)