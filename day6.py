from collections import deque


input_file = 'day6.txt'


def perform_op(op, values):
    if op == '+':
        return sum(values)
    result = 1
    for v in values:
        result *= v
    return result


def part1():
    with open(input_file, 'r') as f:
        symbols = [line.strip().split(' ') for line in f.readlines()]
        ops = deque(symbols[-1])
        symbols = [deque(line) for line in symbols[:-1]]
        m = len(symbols)
        total = 0
        while symbols[0]:
            vals = []
            for i in range(m):
                while symbols[i] and symbols[i][0].strip() == '':
                    symbols[i].popleft()
                if not symbols[i]:
                    break
                vals.append(int(symbols[i].popleft().strip()))
            while ops and ops[0].strip() == '':
                ops.popleft()
            if not ops:
                break
            op = ops.popleft().strip()
            total += perform_op(op, vals)
        print(total)


def part2():
    with open(input_file, 'r') as f:
        lines = f.readlines()
        ops = lines[-1].strip().split(' ')
        lines = lines[:-1]
        m, n = len(lines), len(lines[0])
        vals = []
        total = 0
        for col in range(n-1, -1, -1):
            num = 0
            for row in range(m):
                if lines[row][col].strip():
                    num = num * 10 + int(lines[row][col].strip())
            if num == 0:
                if vals:
                    while ops and ops[-1].strip() == '':
                        ops.pop()
                    if not ops:
                        break
                    op = ops.pop().strip()
                    total += perform_op(op, vals)
                    vals = []
                continue
            vals.append(num)
        while ops and ops[-1].strip() == '':
            ops.pop()
        if not ops:
            return
        op = ops.pop().strip()
        total += perform_op(op, vals)
        print(total)


if __name__ == '__main__':
    part1()
    part2()
