a = [int(i) for i in input().split()]
y = []
i = 0
while len(y) < len(a):

    if len(a) == 1:
        y.append(a[0])
        print(*y, sep=' ')
        break
    elif i == 0:
        result = a[-1] + a[1]
        y.append(result )
    elif i == len(a) - 1:
        result = a[-2] + a[0]
        y.append(result)
    elif i < len(a):
        result = a[i-1] + a[i+1]
        y.append(result)
    i+=1

if len(a) !=1:
    print(*y, sep=' ')
