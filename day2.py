
with open("day2input.txt","r") as f:
    input = f.read()

total = 0
for val_range in input.split(','):
    minval,maxval = val_range.split("-")

    for i in range(int(minval),int(maxval)+1):
        # make the number a string, split it in half, see if the halves match
        string_i = str(i)
        string_len = len(string_i)
        first_string = string_i[0:int(string_len/2)]
        second_string = string_i[int(string_len/2):string_len]

        if first_string == second_string:
            total += i

print(total)