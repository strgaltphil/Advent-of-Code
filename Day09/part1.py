with open('input.txt', 'r') as file:
    data = [[x for x in line] for line in file.read().split('\n')]

def get_adjacents(x: int, y: int) -> list:
    max_x, max_y = len(data[0])-1, len(data)-1

    adjacents = [index for index in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)] if index[0] >= 0 and index[0] <= max_x and index[1] >= 0 and index[1] <= max_y]

    return [data[coord[1]][coord[0]] for coord in adjacents]


low_point_risk_values = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if min(get_adjacents(x, y)) > data[y][x]:
            low_point_risk_values.append(int(data[y][x])+1)

print(sum(low_point_risk_values))