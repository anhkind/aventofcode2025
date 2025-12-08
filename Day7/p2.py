from functools import cache
def solve(lines):
    @cache
    def count(pos, idx):
        if idx >= len(lines): return 1
        line = lines[idx]
        if line[pos] == '^':
            return count(pos - 1, idx + 1) + count(pos + 1, idx + 1)
        return count(pos, idx + 1)

    pos = lines[0].index('S')
    return count(pos, 1)

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
    assert(result == 10357305916520)

