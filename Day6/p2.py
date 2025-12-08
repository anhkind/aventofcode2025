import re
def solve(lines):
    OP = {
        '+': lambda x, y: x+y,
        '*': lambda x, y: x*y,
    }

    ops = re.split(r'\s+', lines.pop().strip())
    res = [0 if op == '+' else 1 for op in ops]

    m, n = len(lines), len(lines[0])
    idx = len(ops) - 1
    for j in range(n - 1, -1, -1):
        num = None
        for i in range(m):
            if lines[i][j] == ' ':
                if num == None: continue
                break
            if num == None: num = 0
            num = num*10 + int(lines[i][j])
        if num == None:
            idx -= 1
        else:
            res[idx] = OP[ops[idx]](res[idx], int(num))
    return sum(res)

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip("\n") for line in file if line]
    return lines

if __name__ == "__main__":
    lines = read_lines('input.txt')
    result = solve(lines)
    print(result)
    assert(result == 10389131401929)


