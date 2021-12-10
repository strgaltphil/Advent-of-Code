with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

def get_error_points(line):
    stack = []

    for l in list(line):
        if l in ["<","(","[","{"]:
            stack.append(l)
        else:
            if l == ">" and stack[-1] != "<":
                return 25137
            if l == ")" and stack[-1] != "(":
                return 3
            if l == "]" and stack[-1] != "[":
                return 57
            if l == "}" and stack[-1] != "{":
                return 1197
            else:
                stack.pop()
    return 0

errors = [get_error_points(d) for d in data]

print(f"Points: {sum(errors)}")