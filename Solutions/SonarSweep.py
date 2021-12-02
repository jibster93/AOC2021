def create_data_array(path):
    file = open(path, 'r')
    Lines = file.readlines()
    return Lines

def depth_measure_increase():

    sweep_data = create_data_array('DataFiles/SonarSweep01.txt')
    increment_count = 0

    for i in range(len(sweep_data) - 1):
        if int(sweep_data[i]) < int(sweep_data[i+1]):
            increment_count += 1

    return increment_count

def sliding_window_increase():

    sweep_data = create_data_array('DataFiles/SonarSweep01.txt')
    increment_count = sum(int(second_set) > int(first_set) for first_set, second_set in zip(sweep_data, sweep_data[3:]))

    return increment_count
    

print(f'Part 1 - Depth measurments increased over previous: {depth_measure_increase()}\nPart 2 - Depth measurement windows increased over previous: {sliding_window_increase()}')