
with open("day7input.txt","r") as f:
    input = f.read()

lines = input.split('\n')

# beams is 0 for no beam, 1 for a beam
beams = [0] * len(lines[0])

# first find the S - the entry point
for idx, character in enumerate(lines[0]):
    if character == 'S':
        beams[idx] = 1
        break
lines.pop(0)

splitters_hit = 0

# now for each line we take the beams and see if we hit a splitter
for line in lines:
    for idx, character in enumerate(line):
        if beams[idx] == 0:
            continue

        # there is a beam in this column - split it?
        if character == '^':
            beams[idx] = 0
            beams[idx-1] = 1
            beams[idx+1] = 1 # assume not gonna immediately hit a splitter?  if that happens need to cache not update here!
            splitters_hit+=1

print(splitters_hit)