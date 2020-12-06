# ---------------------------------------------------------------------------------------------------------------------
# Read input file
with open('../data/input_03.txt') as f:
    line_lst = f.read().split('\n')


# ---------------------------------------------------------------------------------------------------------------------
# Loop through all positions for each line, create list of all positions that the lines travelled
line_position_lst = []

for index, line in enumerate(line_lst):
    moves = line.split(',')

    position_lst = []
    position = (0,0,0)

    for move in moves:
        direction = move[0]
        distance = int(move[1:])

        i = 0

        while i < distance:
            if direction == 'R':
                position = (position[0]+1, position[1], position[2]+1)
            elif direction == 'L':
                position = (position[0]-1, position[1], position[2]+1)
            elif direction == 'U':
                position = (position[0], position[1]+1, position[2]+1)
            elif direction == 'D':
                position = (position[0], position[1]-1, position[2]+1)

            i += 1

            position_lst.append(position[:])

    line_position_lst.append({'line': index, 'position': position_lst})


# ---------------------------------------------------------------------------------------------------------------------
# Create a list per line 
line_1 = line_position_lst[0]['position']
line_2 = line_position_lst[1]['position']

positions_1 = [(p[0], p[1]) for p in line_1]
positions_2 = [(p[0], p[1]) for p in line_2]


# Find the intersecting points that appear in both lists
cross_positions = list(set(positions_1).intersection(positions_2))

# Merge intersecting points back to steps taken to reach the position
cross_positions_with_steps = []

for cp in cross_positions:
    for p1 in line_1:
        if cp[0] == p1[0] and cp[1] == p1[1]:
            steps_1 = p1[2]

    for p2 in line_2:
        if cp[0] == p2[0] and cp[1] == p2[1]:
            steps_2 = p2[2]

    cross_positions_with_steps.append({'position': cp, 'steps': steps_1+steps_2})

# Sort the list of points by number of steps
cross_positions_sorted = sorted(cross_positions_with_steps, key=lambda k: k['steps'])


# ---------------------------------------------------------------------------------------------------------------------
# Return smallest distance
if __name__ == "__main__":
    print(cross_positions_sorted[0])

