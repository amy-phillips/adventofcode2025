import numpy

with open("day9input.txt","r") as f:
    input = f.read()

corners = []
for line in input.split('\n'):
    corner = line.split(',')
    corners.append(numpy.array([int(corner[0]),int(corner[1])]))

max_area = 0

# brute force 
for idxa, cornera in enumerate(corners):
    for idxb in range(idxa+1, len(corners)):
        cornerb = corners[idxb]
        
        minx = min(cornera[0], cornerb[0])
        miny = min(cornera[1], cornerb[1])
        maxx = max(cornera[0], cornerb[0])
        maxy = max(cornera[1], cornerb[1])

        # is any other line segment inside the box - if it is enough inside then we have a gappy bit and cannot count this box
        gappy = False
        for idx_comp,comp_corner in enumerate(corners):
            if idx_comp+1 < len(corners):
                next_comp_corner = corners[idx_comp+1]
            else:
                next_comp_corner = corners[0]
            
            seg_minx = min(comp_corner[0], next_comp_corner[0])
            seg_miny = min(comp_corner[1], next_comp_corner[1])
            seg_maxx = max(comp_corner[0], next_comp_corner[0])
            seg_maxy = max(comp_corner[1], next_comp_corner[1])

            if seg_minx >= maxx:
                continue
            if seg_miny >= maxy:
                continue
            if seg_maxx <= minx:
                continue
            if seg_maxy <= miny :
                continue
            # this corner is inside
            gappy = True
            break
        if gappy:
            continue
        sides = abs(cornera - cornerb)
        area = (sides[0]+1)*(sides[1]+1)
        max_area = max(area, max_area)

print(max_area)
