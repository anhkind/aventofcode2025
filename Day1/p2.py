def solve(rotations):
    pos, res = 50, 0
    for rot in rotations:
        sign = 1 if rot[0] == 'R' else -1
        q, r = divmod(int(rot[1:]), 100)
        res += q
        prev = pos
        pos += sign * r
        if prev != 0 and (pos <= 0 or pos >= 100): res += 1
        pos %= 100
    return res

def read_lines(filename):
    """Reads a file where each line is a string item into a list."""
    try:
        with open(filename, 'r') as file:
            # Remove empty lines if they exist
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []

if __name__ == "__main__":
    filename = 'input.txt'  # Change this to your actual filename
    lines = read_lines(filename)
    result = solve(lines)
    print(result)
    assert(result == 6638)
