with open('input.txt', 'r') as file:
    data = [tuple(line.split("-")) for line in file.read().split('\n')]

caves = dict()

for d in data:
    caves[d[0]] = set([d[1]]) | caves.get(d[0], set())
    caves[d[1]] = set([d[0]]) | caves.get(d[1], set())

def cave_traversal(current_cave = "start", visited = {"start"}):
    if current_cave == "end":
        return 1

    distinct_paths = 0

    for cave in caves[current_cave]:
        if cave.isupper():
            distinct_paths += cave_traversal(cave, visited)

        elif cave not in visited:
            distinct_paths += cave_traversal(cave, visited | {cave})

    return distinct_paths

print(f"Distinct paths: {cave_traversal()}")