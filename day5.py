
with open("day5input.txt","r") as f:
    input = f.read()

total = 0
ranges = []
for line in input.split('\n'):
    # are we a range?
    if '-' in line:
        min,max=line.split('-')
        ranges.append([int(min),int(max)])

    elif len(line):
        value = int(line)
        for range in ranges:
            min,max = range
            if value >= min and value <= max:
                total+=1
                break

print(total)