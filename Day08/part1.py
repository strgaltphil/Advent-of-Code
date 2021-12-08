with open('input.txt', 'r') as file:
    data = [line for line in file.read().split('\n')]

splitted_data = [(d.split(" | ")[0].split(), d.split(" | ")[1].split()) for d in data]

easy_numbers = 0
for sd in splitted_data:
    for out in sd[1]:
        if len(out) in [2, 4, 3, 7]:
            easy_numbers += 1

print(f"Easy numbers: {easy_numbers}")

