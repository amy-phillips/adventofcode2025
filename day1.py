
with open("day1input.txt","r") as f:
    input = f.read()

total = 0
value = 50
prev_value = 50
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
        total+=1
        value += 100
    while value > 100:
        total+=1
        value -= 100

    # did we actually land on 0
    if value == 100 or value == 0:
        total+=1
        value = 0

    if prev_value == 0 and direction == "L":
        total-=1

    prev_value = value

print(total)