genome = input()

# cчетчик букв
d = 0
# индекс числа
i = ''
j = len(genome)
genome1 = genome[0]
for i in genome:
    if i == genome1:
        d += 1
    elif i != genome1:
        print(genome1+ str(d), end='')
        d = 1
    genome1 = i

print(genome1+str(d), end='')

'''print(j)a

print(d)
count= genome.count('a')
count = str(count)
print(genome[i],d, sep='')'''