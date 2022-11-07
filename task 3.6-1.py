import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/699.txt')
r1 = r.text.splitlines()
print(r1)
d=[]
i=0
r=0
for x in r1:
    r+=1
    if x != '':
        d.append(x)
        i+=1


print(d)
print(len(d))
print(i)
x = 'abc'
type(id(x))