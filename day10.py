import re
from copy import deepcopy

with open("day10input.txt","r") as f:
    input = f.read()

def joltage_too_big(joltages, wanted_joltages):
    for idx, iv in enumerate(joltages):
        if iv > wanted_joltages[idx]:
            return True
        
    return False

def any_joltages_match(joltage_values, wanted_joltages):
    for joltages in joltage_values:
        if joltages == wanted_joltages:
            return True
        
    return False

def apply_button(joltages, buttons_indices):
    next_joltages = list(joltages)
    for idx in buttons_indices:
        next_joltages[idx] +=1
    return tuple(next_joltages)

def apply_buttons(val, buttons, next_joltage_values, check_for_bigness):
    for buttons_indices in buttons:
        next_joltages = apply_button(val, buttons_indices)
        # we can discard anything that has gone too high 
        if check_for_bigness and joltage_too_big(next_joltages, wanted_joltages):
            continue
        next_joltage_values.add(next_joltages)

total_presses = 0
for line in input.split('\n'):
    indicators_re = re.search(r"^\[[.#]*\]", line)
    indicators = []
    wanted_indicators = []
    for i in range(indicators_re.start()+1, indicators_re.end()-1):
        indicators.append(False)
        if(line[i] == '.'):
            wanted_indicators.append(False)
        elif(line[i] == '#'):
            wanted_indicators.append(True)
    wanted_indicators = tuple(wanted_indicators)
    indicators = tuple(indicators)

    buttons_matches = re.findall(r"\([\d,]+\)", line)
    buttons = []
    for match in buttons_matches:
        buttons_indices = []
        match = match.strip("()")
        buttons_indices_strings = match.split(",")
        for button_idx in buttons_indices_strings:
            buttons_indices.append(int(button_idx))
        buttons_indices=tuple(buttons_indices)
        buttons.append(buttons_indices)

    joltage_re = re.search(r"{([\d,]+)}$", line)
    joltages_str = joltage_re[1].split(",")
    wanted_joltages = []
    joltages = []
    for jolt in joltages_str:
        wanted_joltages.append(int(jolt))
        joltages.append(0)
    wanted_joltages = tuple(wanted_joltages)
    joltages = tuple(joltages)

    presses = 0
    # take everything in this array, try each button in turn, see if we end up matching
    # if we don;t match then we can compress any matching values in this array and carry on
    joltage_values = [joltages]
    while(not any_joltages_match(joltage_values, wanted_joltages)):
        presses += 1
        next_joltage_values = set()
        check_for_bigness = (presses % 50 == 0) # optimisation - only strip out the big values periodically
        for val in joltage_values:
            apply_buttons(val, buttons, next_joltage_values, check_for_bigness)
            
        joltage_values = next_joltage_values

    print(presses)
    total_presses+=presses

print(total_presses)
