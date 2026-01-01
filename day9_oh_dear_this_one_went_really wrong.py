import numpy

with open("day9input.txt","r") as f:
    input = f.read()

def print_grid(grid):
    for y in range(0, len(grid[0])):
        for x in range(0, len(grid)):
            if grid[x][y] == True:
                print("#", end='')
            else:
                print(".", end='')
        print("")
                   

corners = []
for line in input.split('\n'):
    corner = line.split(',')
    corners.append(numpy.array([int(corner[0]),int(corner[1])]))

max_area = 0

# shift to start at the origin, but leave a border around the outside
min_corner = numpy.array([999999999,99999999])
max_corner = numpy.array([0,0])
for corner in corners:
    min_corner[0] = min(min_corner[0], corner[0])
    min_corner[1] = min(min_corner[1], corner[1])
    max_corner[0] = max(max_corner[0], corner[0])
    max_corner[1] = max(max_corner[1], corner[1])
min_corner-=numpy.array([1,1]) # leave a border so we know we're not in a wall when we got to iterate acrosswards later
max_corner+=numpy.array([1,1])
max_corner-=min_corner
for corner in corners:
    corner -= min_corner

def make_grid(corners, max_corner):
    grid = numpy.zeros(shape=(max_corner[0]+1,max_corner[1]+1),dtype=bool)
    for idx,corner in enumerate(corners):
        x = corner[0]
        y = corner[1]
        grid[x][y] = True
        if idx+1 < len(corners):
            next_corner = corners[idx+1]
        else:
            next_corner = corners[0]

        if next_corner[0] == corner[0]:
            # we're going vertically
            if corner[1]<next_corner[1]:
                increment=1
            else:
                increment=-1
            for y in range(corner[1],next_corner[1],increment):
                grid[x][y] = True
        elif next_corner[1] == corner[1]:
            # we're going horizontally
            if corner[0]<next_corner[0]:
                increment=1
            else:
                increment=-1
            for x in range(corner[0],next_corner[0],increment):
                grid[x][y] = True
        else:
            print("wtf?")
    return grid



#print_grid(grid)

def wall_is_left_and_right(grid,x,y):
    if grid[x-1][y] == True and grid[x+1][y] == True:
        return True

    return False

def wall_is_coming_from_left(grid,x,y):
    # look up one square - is it wall?
    if grid[x-1][y] == True:
        return True

    return False

def wall_is_coming_from_right(grid,x,y):
    # look up one square - is it wall?
    if grid[x+1][y] == True:
        return True

    return False

def fill_in_middle(grid):
    for x in range(0, max_corner[0]+1):
        inside=False
        inside_wall='n' # set this to 'l' for a wall coming from left, and 'r' for a wall coming from right
        for y in range(0, max_corner[1]+1):
            if grid[x][y] == False:
                if inside_wall == 'l':
                    if not wall_is_coming_from_left(grid,x,y-1):
                        inside = not inside
                elif inside_wall == 'r':
                    if wall_is_coming_from_left(grid,x,y-1):
                        inside = not inside
                inside_wall = 'n'

                if inside:
                    grid[x][y] = True
            elif grid[x][y] == True:
                if inside_wall == 'n':
                    if wall_is_left_and_right(grid,x,y):
                        inside = not inside
                    elif wall_is_coming_from_left(grid,x,y):
                        inside_wall = 'l'
                    elif wall_is_coming_from_right(grid,x,y):
                        inside_wall = 'r'
        #print_grid(grid)

#print_grid(grid)

def contains_zeroes(gid,cornera,cornerb):
    if cornera[0]<cornerb[0]:
        incrementx=1
    else:
        incrementx=-1
    if cornera[1]<cornerb[1]:
        incrementy=1
    else:
        incrementy=-1
    for x in range(cornera[0],cornerb[0],incrementx):
        for y in range(cornera[1],cornerb[1],incrementy):
            if grid[x][y] == False:
                return True
            
    return False

def check_areas(corners, grid):
    for idxa, cornera in enumerate(corners):
        for idxb in range(idxa+1, len(corners)):
            cornerb = corners[idxb]
            sides = abs(cornera - cornerb)
            area = (sides[0]+1)*(sides[1]+1)
            # are there any 0s in this box?
            if contains_zeroes(grid,cornera,cornerb):
                continue
            max_area = max(area, max_area)
    return max_area

grid = make_grid(corners, max_corner)
fill_in_middle(grid)
max_area = check_areas(corners,grid)

print(max_area)
