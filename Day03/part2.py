with open('input.txt', 'r') as file:
    data = [int(line, 2) for line in file.read().split('\n')]

bits = 12

def calculate_oxygen_generator_rating(list: list):
    filtered_list = list

    for i in reversed(range(bits)):
        filtered_list_ones = []
        filtered_list_zeros = []

        for fl in filtered_list:
            if (fl & (1 << i)) == (1 << i):
                filtered_list_ones.append(fl)
            else:
                filtered_list_zeros.append(fl)

        if (len(filtered_list_ones) >= len(filtered_list_zeros)):
            filtered_list = filtered_list_ones
        else:
            filtered_list = filtered_list_zeros

        if len(filtered_list) == 1:
            return filtered_list[0]

def calculate_co2_scrubber_rating(list: list):
    filtered_list = list

    for i in reversed(range(bits)):
        filtered_list_ones = []
        filtered_list_zeros = []

        for fl in filtered_list:
            if (fl & (1 << i)) == (1 << i):
                filtered_list_ones.append(fl)
            else:
                filtered_list_zeros.append(fl)

        if (len(filtered_list_ones) < len(filtered_list_zeros)):
            filtered_list = filtered_list_ones
        else:
            filtered_list = filtered_list_zeros

        if len(filtered_list) == 1:
            return filtered_list[0]

print(f"Life support rating: {calculate_oxygen_generator_rating(data) * calculate_co2_scrubber_rating(data)}")
