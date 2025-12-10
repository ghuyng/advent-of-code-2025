from collections import defaultdict


input_file = 'day9.txt'


def area(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


def is_valid(p1, p2, linex, liney):
    minx, maxx = min(p1[0], p2[0]), max(p1[0], p2[0])
    miny, maxy = min(p1[1], p2[1]), max(p1[1], p2[1])
    for y in range(miny, maxy+1):
        if not is_bound(minx, y, linex, liney):
            return False
        if not is_bound(maxx, y, linex, liney):
            return False
    for x in range(minx, maxx+1):
        if not is_bound(x, miny, linex, liney):
            return False
        if not is_bound(x, maxy, linex, liney):
            return False
    return True


def is_bound(x, y, linex, liney):
    left, right, upper, lower = False, False, False, False
    for boundx in linex:
        found = False
        for l, r in linex[boundx]:
            if l <= y <= r:
                found = True
                break
        if found:
            if boundx < x:
                left = True
            elif boundx > x:
                right = True
            else:
                left = right = True

    if not left or not right:
        return False

    for boundy in liney:
        found = False
        for l, r in liney[boundy]:
            if l <= x <= r:
                found = True
                break
        if found:
            if boundy < y:
                lower = True
            elif boundy > y:
                upper = True
            else:
                lower = upper = True
    if not lower or not upper:
        return False
    return True


with open(input_file, 'r') as f:
    points = [tuple(map(int, line.split(','))) for line in f.readlines()]


n = len(points)

minx, maxx = points[0][0], points[0][0]
miny, maxy = points[0][1], points[0][1]
for x, y in points:
    minx = min(minx, x)
    miny = min(miny, y)
    maxx = max(maxx, x)
    maxy = max(maxy, y)

linex, liney = defaultdict(list), defaultdict(list)
for i in range(n):
    p1x, p1y = points[i]
    p2x, p2y = points[(i+1)%n]
    if p1x == p2x:
        linex[p1x].append([min(p1y, p2y), max(p1y, p2y)])
    else:
        liney[p1y].append([min(p1x, p2x), max(p1x, p2x)])

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if is_valid(points[i], points[j], linex, liney):
            ans = max(ans, area(points[i], points[j]))

print(ans)

# (3, 5)

# y=1 and 7 <= x <= 11
# x=11 and 1 <= y <= 7 *
# y=7 and 9 <= x <= 11
# x=9 and 5 <= y <= 7 *
# y=5 and 2 <= x <= 9 *
# x=2 and 3 <= y <= 5 *
# y=3 and 2 <= x <= 7 *
# x=7 and 1 <= y <= 3
