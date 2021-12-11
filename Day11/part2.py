import itertools

class Octo:
    def __init__(self, energy: int) -> None:
        self.energy = int(energy)
        self.flashed = False
    
    def flash(self):
        self.flashed = True
        self.energy = 0

def is_in_bounds(x: int, y: int):
    return x in range(0, dim) and y in range(0, dim)

def get_adjacents(x: int, y: int):
    if not is_in_bounds(x, y):
        return []

    r = range(-1, 2)
    adjacent_formula = set(itertools.product(r,r)) - set([(0, 0)])
    return [(x + af[0], y + af[1]) for af in adjacent_formula if is_in_bounds(x + af[0], y + af[1])]

def get_flashable(coords: list):
    return [c for c in coords if not octos[c[1]][c[0]].flashed]

def get_all_flashable():
    coords = []
    for y in range(dim):
        for x in range(dim):
            if octos[y][x].energy > 9:
                coords.append((x, y))
    return coords

def flash_all_adjacents(x: int, y: int):
    for ad in get_adjacents(x, y):
        if not octos[ad[1]][ad[0]].flashed:
            octos[ad[1]][ad[0]].energy += 1

def increase_all():
    for y in range(dim):
        for x in range(dim):
            octos[y][x].energy += 1

def reset_flashed():
    for y in range(dim):
        for x in range(dim):
            octos[y][x].flashed = False

def sum_energies():
    l = []
    for y in range(dim):
        for x in range(dim):
            l.append(octos[y][x].energy)
    return sum(l)

with open('input.txt', 'r') as file:
    octos = [[Octo(l) for l in list(line)] for line in file.read().split('\n')]

dim = len(octos)
steps = 0

while sum_energies() > 0:
    steps += 1
    increase_all()

    while len(get_all_flashable()) > 0:
        flashable = get_all_flashable()
        for f in flashable:
            octos[f[1]][f[0]].flash()
            flash_all_adjacents(*f)
            
    reset_flashed()

    l = []
    for y in range(dim):
        for x in range(dim):
            l.append(octos[y][x].energy)

# print_octos()
print(f"Number of steps needed: {steps}")