with open("input.txt") as file:
    data = [line for line in file.read().split('\n') if line != ""]

dots = tuple(tuple((int(d.split(",")[0]), int(d.split(",")[1]))) for d in data if not d.startswith("fold along"))
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

print(f"Visible dots: {len(fold(dots, folds[:1]))}")
