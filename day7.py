input_file = 'day7.txt'


def part1():
    with open(input_file, 'r') as f:
        lines = f.readlines()
        grid = [list(line.rstrip('\n')) for line in lines]
        s = set()
        m, n = len(grid), len(grid[0])
        for i in range(n):
            if grid[0][i] == 'S':
                s.add((0, i))

        count = 0
        while s:
            next_s = set()
            for r, c in s:
                if r == m-1 or c == -1 or c == n:
                    continue
                r += 1
                if grid[r][c] == '^':
                    count += 1
                    next_s.add((r, c-1))
                    next_s.add((r, c+1))
                else:
                    next_s.add((r, c))
            s = next_s

        print(count)


def part2():
    with open(input_file, 'r') as f:
        lines = f.readlines()

    grid = [list(line.rstrip('\n')) for line in lines]
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    # dp[i][j] = number of ways to reach cell (i, j)

    for i in range(n):
        if grid[0][i] == 'S':
            dp[0][i] = 1

    for r in range(1, m):
        for c in range(n):
            if grid[r-1][c] == '.' or grid[r-1][c] == 'S':
                dp[r][c] += dp[r-1][c]
            if c > 0 and grid[r-1][c-1] == '^':
                dp[r][c] += dp[r-1][c-1]
            if c < n-1 and grid[r-1][c+1] == '^':
                dp[r][c] += dp[r-1][c+1]
    print(sum(dp[-1]))


if __name__ == '__main__':
    part1()
    part2()
