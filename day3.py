input_file = 'day3.txt'


def process_bank(bank: str):
    if len(bank) < 2:
        return 0
    d1 = int(bank[0])
    val = 0
    for i in range(1, len(bank)):
        d = int(bank[i])
        val = max(val, d1*10 + d)
        if d > d1:
            d1 = d
    return val


def process_bank2(bank: str, k: int):
    n = len(bank)
    start = 0
    val = 0
    for l in range(k, 0, -1):
        max_idx = start
        for i in range(start+1, n-l+1):
            if bank[i] > bank[max_idx]:
                max_idx = i
        val = val * 10 + int(bank[max_idx])
        start = max_idx + 1
    return val


with open(input_file, 'r') as f:
    banks = f.readlines()
    total_value = sum(process_bank2(bank.strip(), 12) for bank in banks)
    print(total_value)
