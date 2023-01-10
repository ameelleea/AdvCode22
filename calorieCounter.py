file = open("calorieCounter.txt", "r")
lines = file.read()
file.close()


lines = lines.split('\n\n')

for i in range(len(lines)):
    lines[i] = lines[i].split('\n')

lines[-1].pop(-1)
calorieList = []

for i in lines:
    calories = 0
    for j in range(len(i)):
        calories += int(i[j])
    calorieList.append(calories)       


print("The maximum calorie amount is: ", max(calorieList))

calorieList = sorted(calorieList)

print(calorieList)
print(calorieList[-3:])
maxThree = sum(calorieList[-3:])

print(maxThree)
