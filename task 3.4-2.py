text = open("C:\\Users\\Валентин\\Downloads\\dataset_3363_3 (2).txt", 'r')
s1 = text.read().replace('\n', ' ').lower().split()
text.close()

print(s1)

d={}
value=0

for x in s1:
    value = s1.count(x)
    d[x]=list()
    d[x]+=[value]

final_dict = dict([max(d.items(), key=lambda k_v: k_v[1])])
print(final_dict)