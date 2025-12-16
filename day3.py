
with open("day3input.txt","r") as f:
    input = f.read()


total = 0
for battery in input.split('\n'):
    # first find the position of the highest digit
    first_digit = 0
    first_digit_pos = -1
    for high_val in range(9, 0, -1):
        if first_digit > 0:
            break

        # don't look at the very last digit as it has no space after it!
        for battery_index in range(0, len(battery)-1):
            digit = int(battery[battery_index])

            if digit != high_val:
                continue

            first_digit = digit
            first_digit_pos = battery_index
            break

    # now find the highest digit after that first digit
    second_digit = 0
    for high_val in range(9, 0, -1):
        if second_digit > 0:
            break

        for battery_index in range(first_digit_pos+1, len(battery)):
            digit = int(battery[battery_index])

            if digit != high_val:
                continue

            second_digit = digit
            break

    number = first_digit * 10 + second_digit
    total += number

print(total)