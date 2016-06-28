# Enter your code here. Read input from STDIN. Print output to STDOUT

def column(matrix, col, start_idx_row, height):
    return [row[col] for row in matrix[start_idx_row:start_idx_row + height]]


def set_column(matrix, col, start_idx_row, height, values):
    i = 0
    for cur_row in range(start_idx_row, start_idx_row + height):
        matrix[cur_row][col] = values[i]
        i += 1


# Initialise parameters
M, N, R = map(int, raw_input().strip().split())

# Build matrix
matrix = []
for i in range(M):
    matrix.append(raw_input().strip().split())

height = M
width = N
start_idx_row = 0
start_idx_col = 0

while height > 0 and width > 0:
    oneline = []
    # Add top to oneline
    oneline.extend(matrix[start_idx_row][start_idx_col:start_idx_col + width])
    # Add right
    if height > 2:
        right_col = start_idx_col + width - 1
        right_row = start_idx_row + 1
        right_height = height - 2
        oneline.extend(column(matrix, right_col, right_row, right_height))
    # Add bottom
    bottom_row = start_idx_row + height - 1
    oneline.extend(reversed(matrix[bottom_row][start_idx_col:start_idx_col + width]))
    # Add left
    if height > 2:
        left_row = start_idx_row + 1
        left_height = height - 2
        oneline.extend(reversed(column(matrix, start_idx_col, left_row, left_height)))

    # Real Rotation number
    rotations = R % (height * 2 + width * 2 - 4)
    # Rotate oneline
    oneline = oneline[rotations:] + oneline[:rotations]

    # Put rotation back to top
    cur_idx = 0
    matrix[start_idx_row][start_idx_col:start_idx_col + width] = oneline[cur_idx:cur_idx + width]
    cur_idx += width
    # Put back to right
    if height > 2:
        right_col = start_idx_col + width - 1
        right_row = start_idx_row + 1
        right_height = height - 2
        set_column(matrix, right_col, right_row, right_height, oneline[cur_idx:cur_idx + right_height])
        cur_idx += right_height
    # Put back to bottom
    bottom_row = start_idx_row + height - 1
    matrix[bottom_row][start_idx_col:start_idx_col + width] = reversed(oneline[cur_idx:cur_idx + width])
    cur_idx += width
    # Put back to left
    if height > 2:
        left_row = start_idx_row + 1
        left_height = height - 2
        set_column(matrix, start_idx_col, left_row, left_height, list(reversed(oneline[cur_idx:cur_idx + left_height])))

    start_idx_row += 1
    start_idx_col += 1
    height -= 2
    width -= 2

for line in matrix:
    print ' '.join(line)