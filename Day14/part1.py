with open("input.txt") as file:
    data = [line for line in file.read().split("\n") if line != ""]

template = [tuple(d) for d in data if " -> " not in d][0]
rules = dict()

for k, v in [d.split(" -> ") for d in data if " -> " in d]:
    rules[k] = v

polymer = template
for _ in range(10):
    polymer = list(" ".join(polymer))
    for i in range(1, len(polymer), 2):
        polymer[i] = rules["".join(polymer)[i - 1:i + 2:2]]

solution = dict()
for p in polymer:
    solution[p] = solution.get(p, 0) + 1

print(f"Solution: {solution[max(solution, key=solution.get)] - solution[min(solution, key=solution.get)]}")