file = open("cleaning.txt", "r")
pairs = file.read().split()
file.close()

for i in range(len(pairs)):
    pairs[i] = pairs[i].split(',')

for pair in pairs:
    for i in range(len(pair)):
        pair[i] = pair[i].split('-')

for pair in pairs:
    for elf in pair:
        for i in range(len(elf)):
            elf[i] = int(elf[i])

counter = 0

for pair in pairs:
    if (min(pair[0]) >= min(pair[1]) and max(pair[0]) <= max(pair[1])) or (min(pair[1]) >= min(pair[0]) and max(pair[1]) <= max(pair[0])):
        counter += 1
        
print(counter)

newCounter = []

for pair in pairs:
    listed = []
    rangeOne = range(pair[0][0], (pair[0][1]+1))
    rangeTwo = range(pair[1][0], (pair[1][1]+1))
    for i in rangeOne:
        if i in rangeTwo:
            listed.append(i)
    if listed != []:
        newCounter.append(listed)

print(len(newCounter))

