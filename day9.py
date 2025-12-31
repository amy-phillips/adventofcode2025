import numpy

with open("day9input.txt","r") as f:
    input = f.read()

corners = []
for line in input.split('\n'):
    corner = line.split(',')
    corners.append(numpy.array([int(corner[0]),int(corner[1])]))

max_area = 0

# brute force - in future might remove corners that are inside boxes?
for idxa, cornera in enumerate(corners):
    for idxb in range(idxa+1, len(corners)):
        cornerb = corners[idxb]
        sides = abs(cornera - cornerb)
        area = (sides[0]+1)*(sides[1]+1)
        max_area = max(area, max_area)

print(max_area)
