import functools
import os
import time
from collections import defaultdict
from functools import cache

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

@timer
def solve(data: str):
    adj = defaultdict(set)
    for line in data.splitlines():
        parts = line.split(' ')
        u     = parts[0][:-1]
        for v in parts[1:]: adj[u].add(v)

    @cache
    def count(u, v, exclude = None):
        cnt = 0
        for nei in adj[u]:
            if nei == exclude: continue
            if nei == v:
                cnt += 1
                continue
            cnt += count(nei, v, exclude)
        return cnt

    svr_dac_fft_out = count('svr', 'dac', 'fft') * count('dac', 'fft') * count('fft', 'out')
    svr_fft_dac_out = count('svr', 'fft', 'dac') * count('fft', 'dac') * count('dac', 'out')
    return svr_dac_fft_out + svr_fft_dac_out

if __name__ == "__main__":
    input_data = read_input("input.txt")
    result = solve(input_data)
    assert(result == 383307150903216)