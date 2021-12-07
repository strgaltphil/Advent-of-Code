with open('input.txt', 'r') as file:
    data = [int(line) for line in file.read().split('\n')]
    
i = 1
solution = 0

while i < len(data):
	if data[i] > data[i-1]:
		solution += 1
	i += 1

print(solution)
