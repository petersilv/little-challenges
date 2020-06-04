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
    position = (0,0)

    for move in moves:
        direction = move[0]
        distance = int(move[1:])

        i = 0

        while i < distance:
            if direction == 'R':
                position = (position[0]+1, position[1])
            elif direction == 'L':
                position = (position[0]-1, position[1])
            elif direction == 'U':
                position = (position[0], position[1]+1)
            elif direction == 'D':
                position = (position[0], position[1]-1)

            i += 1

            position_lst.append(position[:])

    line_position_lst.append({'line': index, 'position': position_lst})


# ---------------------------------------------------------------------------------------------------------------------
# Create a list per line 
positions_1 = line_position_lst[0]['position']
positions_2 = line_position_lst[1]['position']

# Find the intersecting points that appear in both lists
cross_positions = list(set(positions_1).intersection(positions_2))

# Find the Manhatten distance between the origin and points where lines cross
cross_positions_with_distance = [{'position': c, 'distance': abs(c[0])+abs(c[1])} for c in cross_positions]

# Sort the list of points by Manhatten distance 
cross_positions_sorted = sorted(cross_positions_with_distance, key=lambda k: k['distance'])


# ---------------------------------------------------------------------------------------------------------------------
# Return smallest distance
if __name__ == "__main__":
    print(cross_positions_sorted[0])

