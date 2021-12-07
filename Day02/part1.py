with open('input.txt', 'r') as file:
    data = [tuple((str(line.split(' ')[0]), int(line.split(' ')[1]))) for line in file.read().split('\n') if len(line.split(' ')) == 2]

horizontal_position = 0
depth = 0

for d in data:
    if d[0] == 'up':
        depth -= d[1]
    elif d[0] == 'down':
        depth += d[1]
    else:
        horizontal_position += d[1]

print(horizontal_position*depth)