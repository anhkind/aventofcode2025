import functools
import os
import time
from collections import Counter

def timer(func):
    """Decorator to measure the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function to execute the decorated function and print its runtime."""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] Result: {result}")
        duration = end - start
        time_units = {
            "ns": (1e-6, 1e9),
            "us": (1e-3, 1e6),
            "ms": (1, 1e3),
            "s": (float("inf"), 1),
        }
        for unit, (threshold, multiplier) in time_units.items():
            if duration < threshold:
                print(f"[{func.__name__}] Time: {duration * multiplier:.4f} {unit}")
                break
        return result

    return wrapper

def read_input(file_name) -> str:
    """Read and parse the input file."""
    input_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(input_path, "r", encoding="utf-8") as f:
        return f.read().strip()

def parse_presents(data):
    lines = data.splitlines()
    presents = []
    for i in range(0, len(lines), 5):
        id = int(lines[i][:-1])
        M  = lines[i+1:i+4]
        presents.append((id, M))
    return presents

def parse_regions(data):
    lines = data.splitlines()
    regions = []
    for line in lines:
        parts = line.split(' ')
        nxm = parts[0][:-1]
        n, m = map(int, nxm.split('x'))
        counter = Counter()
        for i, cnt in enumerate(parts[1:]): counter[i] = int(cnt)
        regions.append((m, n, counter))
    return regions

def build_pshapes(present):
    M = present[1]
    shapes = []
    m, n = len(M), len(M[0])
    print(m, n)

    shape = []
    for i in range(m):
        bit = 0
        for j in range(n):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for i in range(m - 1, -1, -1):
        bit = 0
        for j in range(n):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for i in range(m):
        bit = 0
        for j in range(n - 1, -1, -1):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for i in range(m - 1, -1, -1):
        bit = 0
        for j in range(n - 1, -1, -1):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for j in range(n):
        bit = 0
        for i in range(m):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for j in range(n - 1, -1, -1):
        bit = 0
        for i in range(m):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for j in range(n):
        bit = 0
        for i in range(m - 1, -1, -1):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    shape = []
    for j in range(n - 1, -1, -1):
        bit = 0
        for i in range(m - 1, -1, -1):
            bit = bit*2 + (M[i][j] == '#')
        shape.append(bit)
    shapes.append(shape)

    return shapes

def build_rshape(region):
    return [0]*region[0]

def get_rshape_rc(rshape, r, c):
    shape = []
    for i in range(3):
        shape.append((rshape[r + i] >> c) & 7)
    return shape

def can_fit(pshape, rshape_rc):
    for pbit, rbit in zip(pshape, rshape_rc):
        if (rbit ^ pbit) & pbit != pbit: return False
    return True

@timer
def solve(presents, regions):
    pshapes = build_pshapes(presents[0])
    rshape  = build_rshape(regions[0])
    for pshape in pshapes:
        rshape_rc = get_rshape_rc(rshape, 0, 0)
        print(rshape_rc)
        print(can_fit(pshape, rshape_rc))

    res = 0
    return res

if __name__ == "__main__":
    present_data = read_input("test1.txt")
    presents = parse_presents(present_data)

    region_data = read_input("test2.txt")
    regions = parse_regions(region_data)

    result = solve(presents, regions)
    assert(result == 477)