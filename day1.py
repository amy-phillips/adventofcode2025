
with open("day1input.txt","r") as f:
    input = f.read()

total = 0
value = 50
for line in input.split('\n'):
    direction = line[0]
    line = line.removeprefix("L")
    line = line.removeprefix("R")
    magnitude=int(line)
    if direction == "R":
        value += magnitude
    elif direction == "L":
        value -= magnitude
    else:
        print("wot?")

    while value < 0:
        value += 100
    while value > 99:
        value -= 100

    if value == 0:
        total+=1

print(total)