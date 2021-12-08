import string

# complement of set
def comp(i: set):
    return set(list(string.ascii_lowercase[:7])) - i

# complement of a list of sets
def comp_all(input: list):
    l = []
    for i in input:
        l.append(comp(i))
    return l

# union of a list of sets
def union_all(sets: list):
    tmp = sets[0]
    for s in sets[1:]:
        tmp = tmp | s
    return tmp

def calculate_mapping(input):
    mapping = {}

    for c in list(string.ascii_lowercase[:7]):
        mapping[c] = set()

    one = set([s for s in input if len(s) == 2][0])
    four = set([s for s in input if len(s) == 4][0])
    seven = set([s for s in input if len(s) == 3][0])

    # solve for segments with the knowledge of the easy numbers over here
    f = four - union_all(comp_all([set(s) for s in input if len(s) == 5]))
    b = one - union_all(comp_all([set(s) for s in input if len(s) == 6]))
    a = one - b
    d = seven - a - b
    e = four - a - b - f
    g = union_all(comp_all([set(s) for s in input if len(s) == 6])) - a - f
    c = comp(four) - d - g

    mapping[list(f)[0]] = "d"
    mapping[list(b)[0]] = "f"
    mapping[list(a)[0]] = "c"
    mapping[list(d)[0]] = "a"
    mapping[list(e)[0]] = "b"
    mapping[list(g)[0]] = "e"
    mapping[list(c)[0]] = "g"

    return mapping

def calculate_number_from_segments(segments: list, mapping: set):
    num = ""
    for seg in segments:
        tmp = ""
        for s in list(seg):
            tmp += mapping[s]

        tmp = "".join(sorted(list(tmp)))

        number = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
        num += str(number.index(tmp))

    return num

with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

splitted_data = [(d.split(" | ")[0].split(), d.split(" | ")[1].split()) for d in data]

input_data, output_data = [], []

for s in splitted_data:
    input_data.append(["".join(sorted(o)) for o in s[0]])
    output_data.append(["".join(sorted(o)) for o in s[1]])


output_values = []
for sd in splitted_data:
    mapping = calculate_mapping(sd[0])
    output_values.append(calculate_number_from_segments(sd[1], mapping))

print(f"Sum of all numbers: {sum([int(o) for o in output_values])}")