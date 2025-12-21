
with open("day4input.txt","r") as f:
    input = f.read()

def is_roll(lines, row_idx : int, col_idx : int):
    if col_idx < 0 or col_idx >= len(lines[0]):
        return False # fell off the side, doesn't count
    if row_idx < 0 or row_idx >= len(lines):
        return False # fell off the side, doesn't count
    return lines[row_idx][col_idx] =='@'

total = 0
lines = input.split('\n')
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
            total += 1

print(total)