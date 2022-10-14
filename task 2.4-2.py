genome = input()
genome4 = genome[0]
for i in genome[1:]:
    genome3 = genome.find(i)
    genome2 = genome.count(i)
    if i != genome4[-1]:
        genome4 + = i
    print(i, genome2)'''

'''oldstring = input()
newstring = oldstring[0]
genome2=0
for char in oldstring[1:]:
    if char != newstring[-1]:
        newstring += char
        genome2+=1
print(newstring+str(genome2))'''