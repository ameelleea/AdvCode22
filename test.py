crates = [['Z', 'N'],['M', 'C', 'D'],['P']]

coordinates = [[1, 2, 1],[3, 1, 3],[2, 2, 1],[1, 1, 2]]

for tuplet in coordinates:
    for i in range(tuplet[0]):
          item = crates[tuplet[1]-1][-1]
          crates[tuplet[1]-1].remove(item)
          crates[tuplet[2]-1].append(item)
print(crates)

