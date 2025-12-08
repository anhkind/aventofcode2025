from heapq import heappush, heappop
def solve(lines):
    P = [list(map(int, line.split(','))) for line in lines]
    n = len(P)
    heap = []
    for i in range(1, n):
        x1, y1, z1 = P[i]
        for j in range(i):
            x2, y2, z2 = P[j]
            d2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
            heappush(heap, (d2, i, j))

    def find(u):
        if u != parent[u]: parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        nonlocal remain
        pu, pv = find(u), find(v)
        if pu == pv: return
        hi, lo = (pu, pv) if rank[pu] >= rank[pv] else (pv, pu)
        parent[lo] = hi
        rank[hi]  += rank[lo]
        remain -= 1

    parent = [i for i in range(n)]
    rank   = [1]*n
    remain = n
    while heap and remain:
        d2, i, j = heappop(heap)
        union(i, j)
        if remain == 1:
            return P[i][0] * P[j][0]

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    filename = 'input.txt'  # Change this to your actual filename
    lines = read_lines(filename)
    result = solve(lines)
    print(result)
    assert(result == 8368033065)

