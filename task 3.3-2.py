a= input().lower().split()
d={}
value=0
for x in a:
    value = a.count(x)
    d[x]=list()
    d[x]+=[value]
for x,value in d.items():
    print(x,*value)

