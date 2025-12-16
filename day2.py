
with open("day2input.txt","r") as f:
    input = f.read()

def split_and_check(value_to_split: int, num_splits: int) -> bool :
    string_i = str(value_to_split)
    string_len = len(string_i)

    # if we can't split into n parts cleanly then it's not gonna work for this i
    if(string_len % num_splits != 0):
        return False
    
    split_strings = []
    for i in range(0, num_splits):
        sub_string = string_i[int(i*string_len/num_splits):int((i+1)*string_len/num_splits)]
        split_strings.append(sub_string)
        for j in range(0, i):
            if split_strings[i] != split_strings[j]:
                return False
            
    # they all matched - it's a repeating pattern
    return True

total = 0
for val_range in input.split(','):
    minval,maxval = val_range.split("-")

    for i in range(int(minval),int(maxval)+1):
        string_i = str(i)
        string_len = len(string_i)

        # make the number a string, split it in n, see if the parts match
        for j in range(2, string_len+1):
            if split_and_check(i, j):
                total += i
                break

print(total)