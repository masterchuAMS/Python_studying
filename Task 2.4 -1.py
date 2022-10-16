'''Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.'''


# наш геном, который надо ввести
genome = input()

# cчетчик повтора букв
d = 0
# переменная буквы
i = ''
# переменная для первой буквы
genome1 = genome[0]
# добавляем в цикл условие, когда переменная буквы равна первой букве и включаем счетчик
for i in genome:
    if i == genome1:
        d += 1
    # когда буква меняется, обнуляем счетчик и выводим предыдущую букву и количество ее повторов. Там же обнуляем счетчик
    elif i != genome1:
        print(genome1 + str(d), end='')
        d = 1
    # перезапускаем цикл
    genome1 = i
# выводим последнюю букву и количество повторов
print(genome1+str(d), end='')

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'