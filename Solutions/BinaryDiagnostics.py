def create_data_array(path):
    file = open(path, 'r')
    Lines = file.readlines()
    return Lines

def calculate_power_consumption():
    source_data = create_data_array('DataFiles/DiagnosticsReport.txt')

    bit_array = [0] * (len(source_data[0])  - 1)

    gamma_string = ''
    epsilon_string = ''

    for code in source_data:
        for bit_index in range(len(code) - 1):
            code = code.strip()
            if int(code[bit_index]) == 1:
                bit_array[bit_index] += 1
            elif int(code[bit_index]) == 0:
                bit_array[bit_index] -= 1

    for i in range(len(bit_array)):
        if bit_array[i] > 0:
            gamma_string = gamma_string + '1'
            epsilon_string = epsilon_string + '0'
        else:
            gamma_string = gamma_string + '0'
            epsilon_string = epsilon_string + '1'

    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)
    power_consumption = gamma * epsilon

    return (gamma, epsilon, power_consumption)


def calculate_additional_stat(stat):

    filtered_data = create_data_array('DataFiles/DiagnosticsReport.txt')
    checked_pos = 0

    while len(filtered_data) > 1:

        measure_value = 0

        for code in filtered_data:
            code = code.strip()
            if int(code[checked_pos]) == 1:
                measure_value += 1
            else: 
                measure_value -= 1

        if measure_value < 0:
            mcv = 0
        elif measure_value >= 0:
            mcv = 1

        if stat == "oxygen":
            filtered_data = [code for code in filtered_data if int(code[checked_pos]) == mcv]
        elif stat == "co2":
            filtered_data = [code for code in filtered_data if int(code[checked_pos]) != mcv]

        checked_pos += 1

    calculated_value = int(filtered_data[0], 2)
    return calculated_value
   
g, e, c = calculate_power_consumption()

print(f'Part 1.\nGamma value: {g}\nEpsilon value: {e}\nSubmarine power consuption {c} watts')


oxygen_generator = calculate_additional_stat('oxygen')
co2_scrubber = calculate_additional_stat('co2')

print(f'life support system at: {oxygen_generator * co2_scrubber}')