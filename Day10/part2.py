import functools

with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

def is_corrupted(line):
    stack = []

    for l in list(line):
        if l in ["<","(","[","{"]:
            stack.append(l)
        else:
            if l == ">" and stack[-1] != "<":
                return True
            if l == ")" and stack[-1] != "(":
                return True
            if l == "]" and stack[-1] != "[":
                return True
            if l == "}" and stack[-1] != "{":
                return True
            else:
                stack.pop()
    return False

def completion_score(line):
    stack = []

    for l in list(line):
        if l in ["<","(","[","{"]:
            stack.append(l)
        else:
            stack.pop()

    stack = list(reversed(stack))
    solution = []

    for s in stack:
        if s == "<":
            solution.append(4)
        if s == "(":
            solution.append(1)
        if s == "[":
            solution.append(2)
        if s == "{":
            solution.append(3)

    return functools.reduce(lambda a, b: a * 5 + b, solution)

incomplete = [d for d in data if not is_corrupted(d)]

scores = [completion_score(i) for i in incomplete]

scores.sort()

print(f"Solution: {scores[len(scores) // 2]}")