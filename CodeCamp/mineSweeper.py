'''
Write a function that will take 3 arguments:
bombs = list of bomb locations
rows of the matrix
columns of the matrix
e.g. mine_sweeper([[0,0], [1,2]], 3, 4)

output =
we should return an 3 X 4 array (-1) = bomb

'''

def mine_sweeper(bombs, num_rows, num_cols):
    # set all the fields to 0
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    #print(field)

    # Set the fields containing the bomb to -1 
    # Also for the proximity bomb logic this acts as the center point
    for bomb_locations in bombs:
        (bomb_row, bomb_col) = bomb_locations
        field[bomb_row][bomb_col] = -1

        # create 3 X 3 range for a given element in the matrix
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col -1, bomb_col + 2)

        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if (0 <= i < num_rows and 0<= j < num_cols and field[i][j] != -1):
                    field[i][j] += 1

    return field

print(mine_sweeper([[0,0], [1,2]], 3, 4))
