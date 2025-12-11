from collections import defaultdict, deque
from functools import cache


input_file = 'day11.txt'

with open(input_file, 'r') as f:
    lines = f.readlines()

graph = defaultdict(list)
for line in lines:
    source, dests = line.split(':')
    graph[source] = dests.strip().split()


def bfs(graph, start, goal):
    q = deque([start])
    cnt = 0
    while q:
        node = q.popleft()
        if node == goal:
            cnt += 1
            continue
        for nei in graph[node]:
            q.append(nei)
        print(len(q))
    return cnt


def find_path(start, goal):
    @cache
    def rec(state):
        if state == goal:
            return 1
        cnt = 0
        for nei in graph[state]:
            cnt += rec(nei)
        return cnt
    v = rec(start)
    return v


v = find_path('svr', 'fft') * find_path('fft', 'dac') * find_path('dac', 'out')
v += find_path('svr', 'dac') * find_path('dac', 'fft') * find_path('fft', 'out')
print(v)
# v = find_path('svr', 'out')
