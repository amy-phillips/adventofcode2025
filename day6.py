
with open("day6input.txt","r") as f:
    input = f.read()

lines = input.split('\n')

# grab the operation and then remove the last line
operations = lines[-1].split()
lines.pop(-1)

totals = []
for operation in operations:
    if operation == '*':
        totals.append(1)
    elif operation == '+':
        totals.append(0)

for line in lines:
    numbers = line.split()
    for idx, number in enumerate(numbers):
        if operations[idx] == '*':
            totals[idx] *= int(number)
        elif operations[idx] == '+':
            totals[idx] += int(number)

totaltotal = 0
for total in totals:
    totaltotal += total

print(totaltotal)