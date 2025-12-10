import heapq
from math import sqrt


input_file = 'day8.txt'


def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.count = {i: 1 for i in range(n)}

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def merge(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.ranks[px] == self.ranks[py]:
                self.parents[py] = px
                self.ranks[px] += 1
                self.count[px] += self.count[py]
                # self.count.pop(py, 0)
            elif self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
                self.count[py] += self.count[px]
                # self.count.pop(px, 0)
            else:
                self.parents[py] = px
                self.count[px] += self.count[py]
                # self.count.pop(py, 0)


points = []
with open(input_file, 'r') as f:
    points = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

q = []
n = len(points)
for i in range(n):
    for j in range(i+1, n):
        d = dist(points[i], points[j])
        q.append((d, i, j))

heapq.heapify(q)
dsu = DSU(n)

connections = 1000
last2 = None
while q:
    # if connections == 0:
    #     break
    d, i, j = heapq.heappop(q)
    if dsu.find(i) == dsu.find(j):
        continue
    connections -= 1
    dsu.merge(i, j)
    last2 = (i, j)

# cnts = sorted(dsu.count.values())

# tmp = set(dsu.find(x) for x in range(n))
# cnts = sorted(dsu.count[x] for x in tmp)
# print(cnts)
# ans = cnts[-1] * cnts[-2] * cnts[-3]


# print(ans)

i, j = last2
print(points[i])
print(points[j])
print(points[i][0] * points[j][0])
