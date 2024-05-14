adjacent_digits = {
    '0': ['0', '8'],
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9']
}

def get_pins(typed):
    if len(typed) == 1:
        return adjacent_digits[typed]
    
    rest_pins = get_pins(typed[1:])
    return [digit + pin for digit in adjacent_digits[typed[0]] for pin in rest_pins]

print(get_pins('369'))  
