a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('\t', end='')
for k in range(c, d + 1):
    print(k, '\t', end='')
print()

for i in range(a, b + 1):
    print(i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, end='')
    print()
