def solve(ranges, ids):
    R = sorted(map(lambda range: tuple(map(int, range.split('-'))) , ranges))
    I = sorted(map(int, ids))

    j = 0
    res = 0
    for i, id in enumerate(I):
        while j < len(R) and R[j][1] < id: j += 1
        if j == len(R): break
        l, _ = R[j]
        if l <= id: res += 1
    return res

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    ranges = read_lines('input.txt')
    ids    = read_lines('input2.txt')
    result = solve(ranges, ids)
    print(result)
    assert(result == 694)

