import functools
import os
import time
from typing import List, Tuple

inf = float('inf')

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
    switches = [list(map(int, part[1:-1].split(','))) for part in parts[1:-1]]
    counters = list(map(int, parts[-1][1:-1].split(',')))
    return switches, counters

def gaussian_elimination(matrix: List[List[int]]) -> Tuple[List[int], List[List[int]]]:
    if not matrix:
        return [], []

    m = len(matrix)
    n = len(matrix[0]) - 1

    pivot_cols = []
    current_row = 0

    mat = [row[:] for row in matrix]

    for col in range(n):
        if current_row >= m:
            break

        pivot_row = -1
        for row in range(current_row, m):
            if mat[row][col] != 0:
                pivot_row = row
                break

        if pivot_row == -1:
            continue

        mat[current_row], mat[pivot_row] = mat[pivot_row], mat[current_row]
        pivot_cols.append(col)

        for row in range(current_row + 1, m):
            if mat[row][col] != 0:
                factor = mat[row][col]
                pivot_val = mat[current_row][col]

                for j in range(col, n + 1):
                    mat[row][j] = mat[row][j] * pivot_val - mat[current_row][j] * factor

        current_row += 1

    return pivot_cols, mat

def solve_system_exact(switches: List[List[int]], counters: List[int]) -> int:
    n = len(switches)
    m = len(counters)

    matrix = [[0] * (n + 1) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            affects = False
            for pos in switches[j]:
                if pos == i:
                    affects = True
                    break
            if affects:
                matrix[i][j] = 1
        matrix[i][n] = counters[i]

    pivot_cols, reduced_matrix = gaussian_elimination(matrix)

    pivot_set = set(pivot_cols)
    free_vars = [i for i in range(n) if i not in pivot_set]

    best_solution = [0] * n
    best_sum = -1

    def try_solution(free_values: List[int]) -> None:
        nonlocal best_solution, best_sum

        solution = [0] * n
        for i, var_idx in enumerate(free_vars):
            solution[var_idx] = free_values[i] if i < len(free_values) else 0

        for idx in range(len(pivot_cols) - 1, -1, -1):
            row = idx
            col = pivot_cols[idx]
            total = reduced_matrix[row][n]

            for j in range(col + 1, n):
                total -= reduced_matrix[row][j] * solution[j]

            if reduced_matrix[row][col] == 0:
                return

            if total % reduced_matrix[row][col] != 0:
                return

            val = total // reduced_matrix[row][col]
            if val < 0:
                return

            solution[col] = val

        for i in range(m):
            total = 0
            for j in range(n):
                if solution[j] > 0:
                    for pos in switches[j]:
                        if pos == i:
                            total += solution[j]
                            break
            if total != counters[i]:
                return

        total_presses = sum(solution)

        if best_sum == -1 or total_presses < best_sum:
            best_solution = solution[:]
            best_sum = total_presses

    if len(free_vars) == 0:
        try_solution([])
    elif len(free_vars) == 1:
        max_val = 0
        for j in counters:
            if j > max_val:
                max_val = j
        max_val *= 3
        for val in range(max_val + 1):
            if best_sum != -1 and val > best_sum:
                break
            try_solution([val])
    elif len(free_vars) == 2:
        max_val = 0
        for j in counters:
            if j > max_val:
                max_val = j
        if max_val < 200:
            max_val = 200
        for v1 in range(max_val + 1):
            for v2 in range(max_val + 1):
                if best_sum != -1 and v1 + v2 > best_sum:
                    continue
                try_solution([v1, v2])
    elif len(free_vars) == 3:
        for v1 in range(250):
            for v2 in range(250):
                for v3 in range(250):
                    if best_sum != -1 and v1 + v2 + v3 > best_sum:
                        continue
                    try_solution([v1, v2, v3])
    elif len(free_vars) == 4:
        for v1 in range(30):
            for v2 in range(30):
                for v3 in range(30):
                    for v4 in range(30):
                        if best_sum != -1 and v1 + v2 + v3 + v4 > best_sum:
                            continue
                        try_solution([v1, v2, v3, v4])
    else:
        try_solution([0] * len(free_vars))

    return 0 if best_sum == -1 else best_sum

@timer
def solve(data: str):
    res = 0
    for line in data.splitlines():
        switches, counters = parse_line(line)
        res += solve_system_exact(switches, counters)
    return res

if __name__ == "__main__":
    input_data = read_input("input.txt")
    result = solve(input_data)
    assert(result == 17848)