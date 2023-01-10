#A: rock, B: paper, C: scissor
#X: lose, Y: draw, Z: win
#Rock: 1, Paper: 2, Scissor: 3
#Win: 6, Draw: 3, Lost: 0

file = open("strategyGuide.txt", "r")
strategy = file.read()
file.close()

rounds = []

for i in range(len(strategy)):
    round_ = []
    if strategy[i] == 'A' or strategy[i] == 'B' or strategy[i] == 'C':
        round_.append(strategy[i])
        round_.append(strategy[i+2])
        rounds.append(round_)

movePoints = {'X': 1, 'Y': 2, 'Z': 3, 'A': 1, 'B': 2, 'C': 3}

roundPoints = 0

winCon = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
loseCon = [['B', 'X'], ['C', 'Y'], ['A', 'Z']]
drawCon = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]

for move in rounds:
    points = 0
    if move in drawCon:
        points += 3
        points += movePoints[move[1]]
    elif move in winCon:
        points += 6
        points += movePoints[move[1]]
    elif move in loseCon:
        points += 0
        points += movePoints[move[1]]
    roundPoints += points

print(roundPoints)

#Part2
newPoints = 0

moves = ['A', 'B', 'C']

for move in rounds:
    points = 0
    index = moves.index(move[0])
    if move[1] == 'X':
        points += 0
        if move[0] == 'A':
            points += movePoints['C']
        else:
            points += movePoints[moves[index-1]]
    elif move[1] == 'Y':
        points += 3
        points += movePoints[move[0]]
    elif move[1] == 'Z':
        points += 6
        if move[0] == 'C':
            points += movePoints['A']
        else:
            points += movePoints[moves[index+1]]
    newPoints += points
        
print(newPoints)


