def solve(ranges):
    R = map(lambda range: range.split('-'), ranges)
    R = map(lambda arr: tuple(map(int, arr)), R)
    R = sorted(R, reverse=True)
    res = 0
    for x in range(1, 10**6):
        y = int(f"{x}{x}")

        while R and R[-1][1] < y: R.pop()
        if not R: break

        l, _ = R[-1]
        if l <= y: res += y
    return res

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

def read_items_single(filename, separator=','):
    lines = read_lines(filename)
    return lines[0].split(separator)

if __name__ == "__main__":
    filename = 'input.txt'  # Change this to your actual filename
    ranges = read_items_single(filename)
    result = solve(ranges)
    print(result)
    assert(result == 12850231731)

