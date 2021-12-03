with open('input.txt', 'r') as file:
    data = [int(line, 2) for line in file.read().split('\n')]

bits = 12

def calculate():
    most_common_number = 0
    least_common_number = 0

    for i in range(bits):
        zeros = 0
        ones = 0
        for d in data:
            if 1 << i & d == 0:
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            most_common_number = most_common_number | 1 << i
        else:
            least_common_number = least_common_number | 1 << i

    return most_common_number * least_common_number

print(f"power consumption: {calculate()}")