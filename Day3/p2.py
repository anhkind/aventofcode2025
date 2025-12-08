def solve(lines):
    res = 0
    for line in lines:
        dp = [0]*13
        for i in range(len(line)):
            for j in range(len(dp) - 1, 0, -1):
                dp[j] = max(dp[j], dp[j - 1]*10 + int(line[i]))
        res += dp[-1]
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
    assert(result == 170997883706617)

