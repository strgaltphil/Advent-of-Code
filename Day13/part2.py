with open("input.txt") as file:
    data = [line for line in file.read().split('\n') if line != ""]

dots = set(tuple((int(d.split(",")[0]), int(d.split(",")[1]))) for d in data if not d.startswith("fold along"))
folds = tuple(tuple((d.split()[-1].split("=")[0], int(d.split()[-1].split("=")[1]))) for d in data if d.startswith("fold along"))

def fold(d, f):
    for axis, index in f:
        folded = set()
        for x, y in d:
            if axis == "x":
                folded.add((x if x < index else 2 * index - x, y))
            else:
                folded.add((x, y if y < index else 2 * index - y))
        d = folded
    return folded

folded = fold(dots, folds)

len_x = max(x for x, _ in folded) + 1
len_y = max(y for _, y in folded) + 1

paper = [[' '] * (len_x) for _ in range(len_y)]

for x, y in folded:
    paper[y][x] = "#"

print("\n".join("".join(row) for row in paper))