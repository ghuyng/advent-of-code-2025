from collections import deque
import re


def bfs(start, goal, buttons):
    q = deque([(start, 0)])
    visited = set([start])
    while q:
        state, steps = q.popleft()
        if state == goal:
            return steps
        steps += 1
        for b in buttons:
            next_state = press_button(state, b)
            if next_state in visited:
                continue
            if next_state == goal:
                return steps
            visited.add(next_state)
            q.append((next_state, steps))
    return -1


def press_button(state, button):
    return state ^ button


def part1(b, goal):
    buttons = []
    for s in b.strip().split():
        button = 0
        for num in s[1:-1].split(','):
            if num:
                button |= 1 << int(num)
        buttons.append(button)

    # part1
    goal = int(''.join(['1' if x == '#' else '0' for x in goal[::-1]]), 2)
    return bfs(0, goal, buttons)


def press_button2(state, button, goal, time=1):
    state = state[:]
    for b in button:
        state[b] += time
        if state[b] > goal[b]:
            return None
    return state


def max_press(state, button, goal):
    ans = float('inf')
    for b in button:
        ans = min(ans, goal[b] - state[b])
    return ans


def dfs(start, goal, buttons):
    n = len(buttons)
    buttons.sort(key=lambda x: x[0])
    dp = {}
    def rec(state, i):
        # print(state, i)
        if state == goal:
            return 0
        if i == n:
            return float('inf')
        b_i = buttons[i][0]
        if b_i > 0 and state[b_i-1] < goal[b_i-1]:
            return float('inf')
        key = (tuple(state), i)
        if key in dp:
            return dp[key]
        ma = max_press(state, buttons[i], goal)
        cnt = float('inf')
        for time in range(ma+1):
            s = press_button2(state, buttons[i], goal, time)
            if s:
                cnt = min(cnt, time+rec(s, i+1))
        dp[key] = cnt
        return cnt

    return rec(start, 0)


def part2(b, goal):
    buttons = []
    for s in b.strip().split():
        button = []
        for num in s[1:-1].split(','):
            if num:
                button.append(int(num))
        buttons.append(button)

    goal = [int(s) for s in goal.strip().split(',')]
    # return bfs2([0]*len(goal), goal, buttons)
    return dfs([0] * len(goal), goal, buttons)


input_file = 'day10.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()


line_re = r'\[(.*)\](.*)\{(.*)\}'
ans = 0
for line in lines:
    match = re.search(line_re, line)
    if match:
        goal1, b, goal2 = match.groups()

        # part1
        # ans += part1(b, goal1)

        # part2
        v = part2(b, goal2)
        print(v)
        ans += v

print('final answer', ans)
