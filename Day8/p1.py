from heapq import heappush, heappop
def solve(lines, k):
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
        nonlocal k
        pu, pv = find(u), find(v)
        if pu == pv: return
        hi, lo = (pu, pv) if rank[pu] >= rank[pv] else (pv, pu)
        parent[lo] = hi
        rank[hi]  += rank[lo]

    parent = [i for i in range(n)]
    rank   = [1]*n
    while heap and k:
        d2, i, j = heappop(heap)
        union(i, j)
        k -= 1

    visited = set()
    sizes   = []
    for i in range(n):
        p = find(i)
        if p not in visited:
            visited.add(p)
            sizes.append(rank[p])

    sizes.sort(reverse=True)
    return sizes[0]*sizes[1]*sizes[2]

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    filename = 'input.txt'  # Change this to your actual filename
    lines = read_lines(filename)
    k = 1000
    result = solve(lines, k)
    print(result)
    assert(result == 117000)

