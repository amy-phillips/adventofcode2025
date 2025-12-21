
with open("day5input.txt","r") as f:
    input = f.read()

def try_merges(ranges) -> bool:
    for range_idx1 in range(0,len(ranges)-1):
        min1,max1=ranges[range_idx1]
        if min1 ==0 and max1 == 0:
            continue
        for range_idx2 in range(range_idx1+1,len(ranges)):
            min2,max2=ranges[range_idx2]
            if min2 ==0 and max2 == 0:
                continue
            if (min2 >= min1 and min2 <= max1) or (max2 >= min1 and max2 <= max1):
                newmin = min(min1,min2)
                newmax = max(max1,max2)
                ranges[range_idx1] = [newmin,newmax]
                ranges[range_idx2] = [0,0]
                return True # min1,max1 state is now messed up, so quit and try again!
            if (min1 >= min2 and min1 <= max2) or (max1 >= min2 and max1 <= max2):
                newmin = min(min1,min2)
                newmax = max(max1,max2)
                ranges[range_idx1] = [newmin,newmax]
                ranges[range_idx2] = [0,0]
                return True # min1,max1 state is now messed up, so quit and try again!
    return False

total = 0
ranges = []
for line in input.split('\n'):
    # are we a range?
    if '-' in line:
        min1,max1=line.split('-')
        ranges.append([int(min1),int(max1)])

while try_merges(ranges):
    print("merged")

fresh_ids = 0
for minmax in ranges:
    min1,max1 = minmax
    if min1==0 and max1 == 0:
        continue
    fresh_ids += max1-min1+1
    
    

print(fresh_ids)