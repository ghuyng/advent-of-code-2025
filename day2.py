import math

# input_file = 'id-ranges-tmp.txt'
input_file = 'id-ranges.txt'


def sum_invalid_ids(id_range: str):
    start_id, end_id = id_range.split('-')
    start_int, end_int = int(start_id), int(end_id)
    ans = 0
    seen = set()
    for repeated_time in range(2, len(end_id)+1):
        left = 0 if len(start_id) < repeated_time else int(start_id[:len(start_id)//repeated_time])
        right = int(end_id[:math.ceil(len(end_id)/repeated_time)])
        for i in range(left, right+1):
            id = int(f'{i}'*repeated_time)
            if id < start_int or id in seen:
                continue
            if id > end_int:
                break
            seen.add(id)
            ans += id
    return ans


with open(input_file, 'r') as f:
    id_ranges = f.readline().strip().split(',')
    total_invalid_ids = sum(sum_invalid_ids(id_range) for id_range in id_ranges)
    print(total_invalid_ids)
