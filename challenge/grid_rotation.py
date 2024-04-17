grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate_grid(grid: list) -> None:
    rows = len(grid)
    columns = len(grid[0])
    for col in range(columns):
        for row in range(rows):
            print(grid[row][col], end='')
        print()
    return None

if __name__ == "__main__":
    rotate_grid(grid)        