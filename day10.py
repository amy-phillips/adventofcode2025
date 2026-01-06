import re
from copy import deepcopy

with open("day10input.txt","r") as f:
    input = f.read()

def indicators_match(indicators, wanted_indicators):
    for idx, iv in enumerate(indicators):
        if iv != wanted_indicators[idx]:
            return False
        
    return True

def any_indicators_match(indicator_values, wanted_indicators):
    for indicators in indicator_values:
        if indicators_match(indicators, wanted_indicators):
            return True
        
    return False

def append_unique(next_indicators, next_indicator_values):
    # is this value already in?
    for existing in next_indicator_values:
        if indicators_match(existing, next_indicators):
            return
        
    next_indicator_values.append(next_indicators)

def apply_button(indicators, buttons_indices):
    next_indicators = deepcopy(indicators)
    for idx in buttons_indices:
        next_indicators[idx] = not next_indicators[idx]
    return next_indicators

total_presses = 0
for line in input.split('\n'):
    indicators_re = re.search("^[[.#]*]", line)
    indicators = []
    wanted_indicators = []
    for i in range(indicators_re.start()+1, indicators_re.end()-1):
        indicators.append(False)
        if(line[i] == '.'):
            wanted_indicators.append(False)
        elif(line[i] == '#'):
            wanted_indicators.append(True)

    buttons_matches = re.findall("\([\d,]+\)", line)
    buttons = []
    for match in buttons_matches:
        buttons_indices = []
        match = match.strip("()")
        buttons_indices_strings = match.split(",")
        for button_idx in buttons_indices_strings:
            buttons_indices.append(int(button_idx))
        buttons.append(buttons_indices)

    presses = 0
    # take everything in this array, try each button in turn, see if we end up matching
    # if we don;t match then we can compress any matching values in this array and carry on
    indicator_values = [indicators]
    while(not any_indicators_match(indicator_values, wanted_indicators)):
        presses += 1
        next_indicator_values = []
        for val in indicator_values:
            for buttons_indices in buttons:
                next_indicators = apply_button(val, buttons_indices)
                append_unique(next_indicators, next_indicator_values)
        indicator_values = next_indicator_values

    total_presses+=presses

print(total_presses)
