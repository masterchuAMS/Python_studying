import numpy as np
import re

s1 ='x4s7u3q6a6C18e16g7Q15I2T10y19o3B18f11N17e10K3N18m4W1N13F8t17V2'
print(s1)
d = ''  # числа, количество повторов
s = ''  # буквы
mal = []
p = []
p1=s1[0]

for i in range(0, len(s1)):
    if s1[i]>'A':
        d+=s1[i]
        mal.append(d)
    d=''

p=re.findall("\d+", s1)

for i in range(0,len(mal)):
    print(mal[i]*int(p[i]),end='')
print(mal)
print(p)

'''with open('dataset_3363_2.txt','w') as ouf:
    ouf.write(mal)'''
