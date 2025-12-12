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

def parse_input(data):
    lines = data.splitlines()
    shapes = [[] for _ in range(6)]
    index = 0
    trees = []
    for line in lines:
        line = line.strip() # to be safe
        if line == "":
            index += 1
            continue
        if index < 6 and ":" in line:
            continue
        if index < 6:
            shapes[index].append([int(x) for x in line.replace(".","0").replace("#","1")])
        else:
            splited = line.split(": ")
            trees.append( [tuple(int(x) for x in splited[0].split("x")), [int(x) for x in splited[1].split(" ")]])
    return shapes, trees

def fits_without_fanagling(size, shape_indices):
    # all shapes are considered to be 3x3
    width, height = size
    amount_of_shapes = len(shape_indices)
    max_x = width // 3
    max_y = height // 3
    return amount_of_shapes <= max_x * max_y

@timer
def solve(shapes, trees):
    total = 0

    shape_sizes = [0 for _ in range(6)]
    for i, shape in enumerate(shapes):
        shape_sizes[i] = sum(row.count(1) for row in shape)

    for tree in trees:
        size, shape_indices = tree
        if size[0] * size[1] < sum(shape_sizes[i] * j for i, j in enumerate(shape_indices)):
            continue # not enough area
        if fits_without_fanagling(size, shape_indices):
            total += 1
        else:
            print("Skipping complex case for size", size, "and shapes", shape_indices)

    return total

if __name__ == "__main__":
    data = read_input('input.txt')
    shapes, trees = parse_input(data)
    result = solve(shapes, trees)
    assert(result == 583)