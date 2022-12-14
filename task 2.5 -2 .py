'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого \
списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, \
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход \
 ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''



# поступает набор цифр, разделяем и добавляем их в список
a = [int(i) for i in input().split()]
# добавляем пустой список, в котором будет выводиться ответ
y = []
# переменная для условия
i = 0
# цикл выполняется пока, длина нового списка меньше длины полученного списка


while len(y) < len(a):
    # условие, если один элемент в списке, что бы цикл остановился

    if len(a) == 1:
        y.append(a[0])
        print(*y, sep=' ')
        break
    # условие, для нулевого элемента в списке,так как у нулевого элемента нет соседа, мы прибавляем с конечный элемент

    elif i == 0:
        result = a[-1] + a[1]
        y.append(result )
    # условие, для конечного элемента в списке,тоже самое, но прибавляем нулевой элемент

    elif i == len(a) - 1:
        result = a[-2] + a[0]
        y.append(result)
    # условие, для всех элементов

    elif i < len(a):
        result = a[i-1] + a[i+1]
        y.append(result)
    i+=1
# вывод списка, для всех кроме, когда в списке 1 элемент
if len(a) !=1:
    print(*y, sep=' ')
