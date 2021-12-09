from functools import reduce

with open('input.txt', 'r') as file:
    data = [[x for x in line] for line in file.read().split('\n')]

def get_adjacents(x: int, y: int) -> list:
    max_x, max_y = len(data[0])-1, len(data)-1

    adjacents = [index for index in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)] if index[0] >= 0 and index[0] <= max_x and index[1] >= 0 and index[1] <= max_y]

    return adjacents

visited = []

def get_basins(x: int, y: int) -> list:
    adjacents = [a for a in get_adjacents(x, y) if int(data[a[1]][a[0]]) < 9 and int(data[a[1]][a[0]]) > int(data[y][x])]
    global visited
    visited.extend(adjacents)
    visited.append((x, y))

    if len(adjacents) > 0:
        return [get_basins(a[0], a[1]) for a in adjacents]
    else:
        return

basin_sizes = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if min([data[ad[1]][ad[0]] for ad in get_adjacents(x, y)]) > data[y][x]:
            visited = []
            get_basins(x, y)
            basin_sizes.append(len(set(visited)))
basin_sizes.sort()

print(f"Solution: {reduce((lambda a, b: a * b), basin_sizes[-3:])}")