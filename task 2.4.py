'''GC-состав является важной характеристикой геномных последовательностей и определяется как процентное соотношение суммы всех гуанинов и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.

Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов G и C равно \dfrac4{10} \cdot 100 = 40.0
10
4
​
 ⋅100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.'''


# Объявляем переменную и приводим регистер к маленьким буквам, чтобы не было ошибок при заглавных
genome = input()

# с помощью  метода count находим сколько раз попадается в выражении 'c' и 'g' и складываем в новую переменную
how_much = genome.lower().count('c') + genome.lower().count('g')

# вывожу переменные для проверки, все ли правильно
print(how_much)
print(len(genome))

# Ответ на задачку
print((how_much/len(genome))*100)