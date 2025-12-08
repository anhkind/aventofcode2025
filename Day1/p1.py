def solve(rotations):
    pos, res = 50, 0
    for rot in rotations:
        sign = 1 if rot[0] == 'R' else -1
        val  = sign * int(rot[1:])
        pos  = (pos + val) % 100
        res  += pos == 0
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
    assert(result == 1129)


