import numpy

def should_merge(seta, setb):
    for a in seta:
        if a in setb:
            return True
    return False

def do_merge(seta, setb):
    for b in setb:
        if not b in seta:
            seta.append(b)
    setb.clear()

def calc_distances(box_locations):
    distances = []
    for idxa,locationa in enumerate(box_locations):
        distances.append([0]*len(box_locations))
        for idxb in range(idxa+1, len(box_locations)):
            locationb = box_locations[idxb]
            loc_dist = numpy.sum(numpy.square(abs(locationa - locationb))) # scales as distance, no need to sqrt
            distances[idxa][idxb] = loc_dist
    return distances

def add_to_sets(box_sets, min_dist_indices):
    added_to_set = False
    for set in box_sets:
        if min_dist_indices[0] in set:
            if not min_dist_indices[1] in set:
                set.append(min_dist_indices[1])
            return
        elif min_dist_indices[1] in set:
            if not min_dist_indices[0] in set:
                set.append(min_dist_indices[0])
            return

    if not added_to_set:
        box_sets.append(min_dist_indices)

def merge_sets(box_sets):
    merged = True
    while(merged):
        merged = False
        for idxa,seta in enumerate(box_sets):
            for idxb in range(idxa+1, len(box_sets)):
                setb = box_sets[idxb]
                if not should_merge(seta,setb):
                    continue
                do_merge(seta,setb)
                merged = True

    for seta in box_sets:
        if len(seta) == 0:
            box_sets.remove([])

with open("day8input.txt","r") as f:
    input = f.read()

box_locations = []
for line in input.split('\n'):
    location = line.split(',')
    box_locations.append(numpy.array([int(location[0]),int(location[1]),int(location[2])]))

# index into this two dimensional array to find the distance between point_idx_a and point_idx_b
distances = calc_distances(box_locations)

min_dist_in_set = 0
box_sets = []
all_in_one_set = False
min_dist_indices = [0,0]
while not all_in_one_set:
    min_dist_this_iteration = 99999999999999999
    
    for idxa,locationa in enumerate(box_locations):
        for idxb in range(idxa+1, len(box_locations)):
            loc_dist = distances[idxa][idxb]
            if loc_dist<min_dist_this_iteration and loc_dist>min_dist_in_set: # exclude previously joined pairs
                min_dist_this_iteration = loc_dist
                min_dist_indices = [idxa,idxb]
                
    # join idxa/idxb
    min_dist_in_set = min_dist_this_iteration # stash this to exclude this pair in future iterations so we don't repeat
    add_to_sets(box_sets, min_dist_indices)

    # maybe we have new overlap and can merge sets
    merge_sets(box_sets)
    
    all_in_one_set = (len(box_sets[0]) == len(box_locations))

# multiply the x co-ords of the last two points to be connected
multiplied = box_locations[min_dist_indices[0]][0] * box_locations[min_dist_indices[1]][0]

print(min_dist_indices)
print(multiplied)