import re
def solve(lines):
    OP = {
        '+': lambda x, y: x+y,
        '*': lambda x, y: x*y,
    }

    ops = re.split(r'\s+', lines.pop())
    res = [0 if op == '+' else 1 for op in ops]

    for line in lines:
        for i, num in enumerate(re.split(r'\s+', line)):
            res[i] = OP[ops[i]](res[i], int(num))
    return sum(res)

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    lines = read_lines('input.txt')
    result = solve(lines)
    print(result)
    assert(result == 5346286649122)

