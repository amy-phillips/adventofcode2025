
with open("day4input.txt","r") as f:
    input = f.read()

def is_roll(lines, row_idx : int, col_idx : int):
    if col_idx < 0 or col_idx >= len(lines[0]):
        return False # fell off the side, doesn't count
    if row_idx < 0 or row_idx >= len(lines):
        return False # fell off the side, doesn't count
    return lines[row_idx][col_idx] =='@'

def remove_rolls(lines) -> int:
    removed_count = 0
    for row_idx in range(0, len(lines)):
        row = lines[row_idx]
        for col_idx in range(0, len(row)):
            if not is_roll(lines, row_idx, col_idx):
                continue

            spot_count = 0
            if is_roll(lines, row_idx, col_idx-1):
                spot_count += 1
            if is_roll(lines, row_idx, col_idx+1):
                spot_count += 1
            if is_roll(lines, row_idx-1, col_idx-1):
                spot_count += 1
            if is_roll(lines, row_idx-1, col_idx):
                spot_count += 1
            if is_roll(lines, row_idx-1, col_idx+1):
                spot_count += 1
            if is_roll(lines, row_idx+1, col_idx-1):
                spot_count += 1
            if is_roll(lines, row_idx+1, col_idx):
                spot_count += 1
            if is_roll(lines, row_idx+1, col_idx+1):
                spot_count += 1

            if spot_count < 4:
                removed_count += 1
                lines[row_idx][col_idx] = '.'
    return removed_count

total = 0
str_lines = input.split('\n')
lines = []
for line in str_lines:
    lines.append(list(line))

removed_count = 1
while removed_count > 0:
    removed_count = remove_rolls(lines)
    total += removed_count

print(total)