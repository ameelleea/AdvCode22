import csv
import string

file = open("rucksack.csv", "r")
rucksacks = csv.reader(file)
rows = []

for row in rucksacks:
    rows.append(row)

file.close()

doubles = []

for row in rows:
    items = ''
    index = int(len(row[0])/2)
    first_half = row[0][:index]
    second_half = row[0][index:]
    for i in range(len(first_half)):
        if first_half[i] in second_half:
            items = first_half[i]
    doubles.append(items)

def findPriorities(array):
    priorities = 0
    chars = string.ascii_letters
    for i in array:
        priorities += (chars.index(i)+1)
    return priorities

print(findPriorities(doubles))

newRows = []

for row in rows:
    newRows.append(row[0])

def sortRows(array):
    index = 0
    groups = []
    while index <= (len(array) - 2):
        group = []
        group.append(array[index])
        group.append(array[index +1])
        group.append(array[index +2])
        groups.append(group)
        index += 3
    return groups
    
badgeGroups = sortRows(newRows)

badges = []

for group in badgeGroups:
    badge = ''
    for i in range(len(group[0])):
        if (group[0][i] in group[1]) and (group[0][i] in group[2]):
            badge = group[0][i]
    badges.append(badge)

print(badges)

print(findPriorities(badges))
