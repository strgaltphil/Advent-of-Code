with open('input.txt', 'r') as file:
    data = [int(value) for value in file.read().split(',')]

used_fuel_all = []
for i in range(min(data), max(data) + 1):
    used_fuel = 0
    for d in data:
        used_fuel += abs(d-i)
    used_fuel_all.append(used_fuel)
print(f"Used fuel: {min(used_fuel_all)}")
    