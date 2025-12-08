def solve(lines):
    res = 0
    for line in lines:
        one  = int(line[-1])
        maxx = 0
        for i in range(len(line) - 2, -1, -1):
            ten = int(line[i])
            maxx = max(maxx, ten*10 + one)
            one = max(ten, one)
        res += maxx
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
    assert(result == 17207)

