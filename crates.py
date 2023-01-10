file = open("crates.txt", "r")
stacks = file.read().split()
file.close()

for i in range(len(stacks)):
    stack = []
    for j in range(len(stacks[i])):
        stack.append(stacks[i][j])
    stacks[i] = stack

file = open("instructions.txt", "r")
guide = file.read().split('\n')
file.close()

guide.pop(-1)

coordinates = []

for i in range(len(guide)):
    guide[i] = guide[i].split()
    tuplet = []
    for j in range(len(guide[i])):
        if guide[i][j].isnumeric():
            tuplet.append(int(guide[i][j]))
    coordinates.append(tuplet)
#[6, 6, 5]

for tuplet in coordinates:
    for i in range(tuplet[0]):
        item = stacks[tuplet[1]-1][-1]
        stacks[tuplet[1]-1].remove(item)
        stacks[tuplet[2]-1].append(item)

print('\n\n')
for stack in stacks:
    print(stack, '\n')
    print(stack[-1])
