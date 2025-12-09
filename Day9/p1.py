def area(i, j, P):
    x1, y1 = P[i]
    x2, y2 = P[j]
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def solve(lines):
    P = [list(map(int, line.split(','))) for line in lines]
    res = 0
    for i in range(1, len(P)):
        for j in range(i):
            res = max(res, area(i, j, P))
    return res

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    filename = 'input.txt'  # Change this to your actual filename
    lines = read_lines(filename)
    result = solve(lines)
    print(result)
    assert(result == 4760959496)

