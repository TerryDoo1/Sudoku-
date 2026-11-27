def get_row(grid, r):
    """returns the row of a grid at index row r"""
    return grid[r]
    
def get_column(grid, r):
    """returns the column of a row at index column r"""
    column = [x[r] for x in grid]
    return(column)
