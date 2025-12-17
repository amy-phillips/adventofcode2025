
with open("day3input.txt","r") as f:
    input = f.read()

def get_next_digit(battery: str, start_offset: int, remaining: int) -> [int,int] :
    for high_val in range(9, 0, -1):
        # don't look at the last few digits as then no space after it!
        for battery_index in range(start_offset, len(battery)-remaining+1):
            digit = int(battery[battery_index])

            if digit != high_val:
                continue

            return digit, battery_index+1


total = 0
for battery in input.split('\n'):
    # first find the position of the highest digit
    digits = []
    num_digits_wanted = 12
    offset = 0
    for digit_index in range(0,num_digits_wanted):
        if len(digits)==num_digits_wanted:
            break
        
        remaining = num_digits_wanted - len(digits)
        digit,offset = get_next_digit(battery, offset, remaining)
        digits.append(digit)
        
    number = 0
    for digit in digits:
        number *= 10
        number += digit
    total += number

print(total)