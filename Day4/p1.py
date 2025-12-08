def solve(lines):
    def count(i, j, lines):
        if i < 0 or i >= m or j < 0 or j >= n or lines[i][j] != '@': return float('inf')
        c = 0
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                if ii < 0 or ii >= m or jj < 0 or jj >= n: continue
                c += lines[ii][jj] == '@'
        return c

    m, n = len(lines), len(lines[0])
    res = 0
    for i in range(m):
        for j in range(n):
            cnt = count(i, j, lines)
            if cnt < 5: res += 1
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
    assert(result == 1419)