def solve(ranges):
    R = sorted(map(lambda range: tuple(map(int, range.split('-'))) , ranges))
    last = [R[0][0], R[0][0]]

    res = 0
    for l, r in R:
        if l <= last[1]:
            last[1] = max(last[1], r)
        else:
            res += last[1] - last[0] + 1
            last = [l, r]
    return res + last[1] - last[0] + 1

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    ranges = read_lines('input.txt')
    result = solve(ranges)
    print(result)
    assert(result == 352716206375547)

