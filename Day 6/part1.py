with open('input.txt', 'r') as file:
    data = [int(value) for value in file.read().split(',')]

days = 80

for i in range(days):
    start_len = len(data)
    for d in range(start_len):
        if data[d] == 0:
            data[d] = 6
            data.append(8)
        else:
            data[d] -= 1

print(f"Total number of fish: {len(data)}")