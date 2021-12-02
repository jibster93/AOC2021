def create_data_array(path):
    file = open(path, 'r')
    Lines = file.readlines()
    return Lines


def pilot_submarine():

    dive_instructions = create_data_array('DataFiles/DiveInstructions.txt')

    position = 0
    depth = 0

    for instruction in dive_instructions:
        direction, value = instruction.split()
        if direction == 'forward':
            position += int(value)
        elif direction == 'up':
            depth -= int(value)
        elif direction == 'down':
            depth += int(value)

    return(position * depth)


def advanced_pilot_submarine():

    dive_instructions = create_data_array('DataFiles/DiveInstructions.txt')

    position = 0
    depth = 0
    aim = 0

    for instruction in dive_instructions:
        direction, value = instruction.split()

        if direction == 'forward':
            position += int(value)
            depth += (int(value) * aim)
        elif direction == 'up':
            aim -= int(value)
        elif direction == 'down':
            aim += int(value)

    return(position * depth)


print(f'Part 1 - Calculated rudementry position: {pilot_submarine()}\nPart 2 - Calculated advanced positionn: {advanced_pilot_submarine()}')