import numpy

with open("day9input.txt","r") as f:
    input = f.read()

corners = []
for line in input.split('\n'):
    corner = line.split(',')
    corners.append(numpy.array([int(corner[0]),int(corner[1])]))

max_area = 0

# shift to start at the origin (this is actually part of part 2)
min_corner = numpy.array([999999999,99999999])
max_corner = numpy.array([0,0])
for corner in corners:
    min_corner[0] = min(min_corner[0], corner[0])
    min_corner[1] = min(min_corner[1], corner[1])
    max_corner[0] = max(max_corner[0], corner[0])
    max_corner[1] = max(max_corner[1], corner[1])
max_corner-=min_corner
for corner in corners:
    corner -= min_corner

# brute force - in future might remove corners that are inside boxes?
for idxa, cornera in enumerate(corners):
    for idxb in range(idxa+1, len(corners)):
        cornerb = corners[idxb]
        sides = abs(cornera - cornerb)
        area = (sides[0]+1)*(sides[1]+1)
        max_area = max(area, max_area)

print(max_area)
