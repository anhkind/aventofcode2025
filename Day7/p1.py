def solve(lines):
    pos = lines[0].index('S')
    S = set([pos])
    res = 0
    for line in lines[1:]:
        SS = set()
        for i, c in enumerate(line):
            if c == '.': continue
            if i in S:
                res += 1
                S.discard(i)
                SS.add(i - 1)
                SS.add(i + 1)
        S = S.union(SS)
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
    lines = read_lines(filename)
    result = solve(lines)
    print(result)
    assert(result == 1622)

