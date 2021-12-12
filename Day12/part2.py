with open('input.txt', 'r') as file:
    data = [tuple(line.split("-")) for line in file.read().split('\n')]

caves = dict()

for d in data:
    caves[d[0]] = set([d[1]]) | caves.get(d[0], set())
    caves[d[1]] = set([d[0]]) | caves.get(d[1], set())

def cave_traversal(current_cave = "start", visited = {"start"}, allow_small_caves_twice = False):
    if current_cave == "end":
        return 1

    distinct_paths = 0

    for cave in caves[current_cave]:
        if cave.isupper():
            distinct_paths += cave_traversal(cave, visited, allow_small_caves_twice)

        elif cave not in visited:
            distinct_paths += cave_traversal(cave, visited | {cave}, allow_small_caves_twice)

        elif allow_small_caves_twice and cave != "start":
             distinct_paths += cave_traversal(cave, visited, False)

    return distinct_paths

print(f"Distinct paths: {cave_traversal(allow_small_caves_twice = True)}")