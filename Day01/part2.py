with open('input.txt', 'r') as file:
	data = [int(line) for line in file.read().split('\n')]
    
solution = 0
i = 0

previous_sum = None

while i < len(data):
	if len(data[i:i+3]) == 3:
		if previous_sum != None:
			if sum(data[i:i+3]) > previous_sum:
				solution += 1
	previous_sum = sum(data[i:i+3])
	i += 1

print(solution)
