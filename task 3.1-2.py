def modify_list(l):
    # put your python code here
    for x in range(len(l) - 1, -1, -1):
        if l[x] % 2 != 0:
            del l[x]
        else:
            l[x] = int(l[x] / 2)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
