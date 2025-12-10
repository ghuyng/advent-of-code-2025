input_file = 'day4.txt'


def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                count += 1
    return count


with open(input_file, 'r') as f:
    grid = [list(x) for x in f.readlines()]
    m, n = len(grid), len(grid[0])
    count = 0
    last_count = -1
    while count != last_count:
        last_count = count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@' and count_neighbors(grid, i, j) < 4:
                    count += 1
                    grid[i][j] = '.'
    print(count)
