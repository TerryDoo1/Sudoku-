
def get_row(grid, r):
    """returns the row of a grid at index row r"""
    return grid[r]
    
def get_column(grid, r):
    """returns the column of a row at index column r"""
    column = [x[r] for x in grid]
    return column
    
def get_num_rows(grid):
    """returns the number of rows in a grid"""
    return len(grid)
    
def get_num_columns(grid):
    """returns the number of columns in a grid"""
    return len(grid[0])
    
def count_value(grid, n):
    """returns the number of cells that contain target n"""
    count = 0
    for i in range(get_num_rows(grid)):
        for j in range(get_num_columns(grid)):
            if grid[i][j] == n:
                count += 1
    return count


def get_coordinates(grid, n):
    """returns the coordinates of cells that contain target n"""
    return [(i, j) for i in range(get_num_rows(grid))
        for j in range(get_num_columns(grid)) if grid[i][j] == n
        ]
                
