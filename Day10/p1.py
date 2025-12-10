import functools
import os
import time
from collections import deque

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

def parse_line(line):
    parts = line.split(" ")

    light    = parts[0][-2:0:-1].replace('.', '0').replace('#', '1')
    switches = []
    for part in parts[1:-1]:
        switch = 0
        for pos in part[1:-1].split(','):
            switch |= 1 << int(pos)
        switches.append(switch)

    return int(light, 2), switches

def toggle(light, switches):
    q = deque([0])
    visited = set([0])
    c = 0
    while q:
        for _ in range(len(q)):
            status = q.popleft()
            if status == light: return c
            for switch in switches:
                status_new = status ^ switch
                if status_new not in visited:
                    visited.add(status_new)
                    q.append(status_new)
        c += 1
    return c

@timer
def solve(data: str):
    res = 0
    for line in data.splitlines():
        light, switches = parse_line(line)
        res += toggle(light, switches)
    return res

if __name__ == "__main__":
    input_data = read_input("input.txt")
    result = solve(input_data)
    assert(result == 449)