import bisect

input_file = 'day5.txt'

with open(input_file, 'r') as f:
    ingredient_ranges = []
    while True:
        r = f.readline().strip()
        if r == '':
            break
        start, end = r.split('-')
        ingredient_ranges.append((int(start), int(end)))

    ingredient_ranges.sort()
    merged_ranges = []
    curr = ingredient_ranges[0]
    valid_ids = 0
    for i in range(1, len(ingredient_ranges)):
        start, end = ingredient_ranges[i]
        if start > curr[1]:
            merged_ranges.append(curr)
            valid_ids += curr[1] - curr[0] + 1
            curr = (start, end)
        else:
            curr = (curr[0], max(curr[1], end))
    merged_ranges.append(curr)
    valid_ids += curr[1] - curr[0] + 1
    print(valid_ids)

    n = len(merged_ranges)
    cnt = 0
    while True:
        id = f.readline().strip()
        if id == '':
            break
        id = int(id)
        i = bisect.bisect_left(merged_ranges, id, key=lambda x: x[1])
        if 0 <= i < n and merged_ranges[i][0] <= id:
            cnt += 1
    print(cnt)
