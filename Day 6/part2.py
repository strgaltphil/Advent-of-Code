with open('input.txt', 'r') as file:
    data = [int(value) for value in file.read().split(',')]

days = 256

# create list for buckets
fish = [0] * 9

# initial population for buckets
for d in data:
    fish[d] += 1

# recalculate buckets for every new day
for i in range(days):
    fish = fish[1:] + fish[:1]
    fish[6] += fish[8]

print(f"Total number of fish: {sum(fish)}")