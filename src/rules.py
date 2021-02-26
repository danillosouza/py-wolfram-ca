
DOWN, UP = 0, 1

def get_possible_neighborhoods():
    """
    one-dimensional neighborhoods
    """
    return [
        '111',
        '110',
        '101',
        '100',
        '011',
        '010',
        '001',
        '000'
    ]

def get_neighborhood(row: list, col: int) -> str:
    n = []
    n.append(row[col-1] and row[col-1] or 0)
    n.append(row[col])
    n.append(col+1 < len(row) and row[col+1] or 0)

    return ''.join(map(str, n))

def apply(row: list, ruleset: callable) -> list:
    new_row = []
    states = get_possible_neighborhoods()

    for index in range(len(row)):
        neighborhood = get_neighborhood(row, index)
        new_row.append(ruleset[states.index(neighborhood)])
    
    return new_row

def advance_grid(grid: list, ruleset: list, direction=UP) -> list:
    if direction == DOWN:
        # shift the grid down
        new_row = apply(grid[0], ruleset)
        grid.pop()
        grid.insert(0, new_row)
    else:
        # shift the grid up
        new_row = apply(grid[-1], ruleset)
        grid.pop(0)
        grid.append(new_row)

    return grid

##
## RULES
## Ex.: 90, 150, 169, 182
##

def get_rule(number: int) -> list:
    binary = bin(number)[2:]
    b_size = len(binary)

    if b_size < 8:
        binary = ('0' * (8-b_size)) + binary
    elif b_size > 8:
        binary = binary[-8:]
    
    return list(map(int, binary))