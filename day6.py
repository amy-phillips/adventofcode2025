
with open("day6input.txt","r") as f:
    input = f.read()

lines = input.split('\n')

# grab the operation and then remove the last line
operations = []
operation_offsets = []
totals = []
for idx,character in enumerate(lines[-1]):
    if character == '*' or character == '+':
        operations.append(character)
        operation_offsets.append(idx)
        if character == '*':
            totals.append(1)
        elif character == '+':
            totals.append(0)
operation_offsets.append(len(lines[-1])+1) # one extra entry, for the end of the line (makes subsequent loop code cleaner)
lines.pop(-1)

# start at the operation idx, look vertically, then increment, there will be an entirely blank line just before the next operation
for idx,operation in enumerate(operations):
    first_line_column = operation_offsets[idx]
    last_line_column = operation_offsets[idx+1]-1
    vertical_numbers = [0] * (last_line_column-first_line_column)
    for line_column in range(first_line_column, last_line_column):
        for line_row,line in enumerate(lines):
            if line[line_column] == ' ':
                continue

            vertical_numbers[line_column-first_line_column] *= 10
            vertical_numbers[line_column-first_line_column] += int(line[line_column])

    for vertical_number in vertical_numbers:
        if operation == '*':
            totals[idx] *= vertical_number
        elif operation == '+':
            totals[idx] += vertical_number

totaltotal = 0
for total in totals:
    totaltotal += total

print(totaltotal)