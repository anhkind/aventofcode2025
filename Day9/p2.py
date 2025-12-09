from collections import defaultdict

def area(i, j, P):
    x1, y1 = P[i]
    x2, y2 = P[j]
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def find_lines(P):
    X, Y = {}, {}
    for i, [x, y] in enumerate(P):
        if x in X:
            lo, hi = X[x]
            X[x] = [min(y, lo), max(y, hi)]
        else: X[x] = [y, y]

        if y in Y:
            lo, hi = Y[y]
            Y[y] = [min(x, lo), max(x, hi)]
        else: Y[y] = [x, x]
    return (X, Y)

def adjacent(p1, p2, adj):
    if p1 not in adj: adj[p1] = list()
    if p2 not in adj: adj[p2] = list()
    adj[p1].append(p2)
    adj[p2].append(p1)

def find_adj(P):
    adj = {}
    X, Y = {}, {}
    for i, [x, y] in enumerate(P):
        if x in Y:
            adjacent(P[i], P[Y[x]], adj)
        if y in X:
            adjacent(P[i], P[X[y]], adj)
        Y[x] = i
        X[y] = i
    return adj

def find_polygon(pi, p0, adj, polygon, visited):
    if pi == p0 and len(polygon) > 2: return True
    for pj in adj[pi]:
        if pj not in visited:
            visited.add(pj)
            polygon.append(pj)
            found = find_polygon(pj, p0, adj, polygon, visited)
            if found: return found
            polygon.pop()
            visited.remove(pj)
    return False

def is_inside(p, polygon):
    x, y = p
    size = len(polygon)
    inside = False
    x1, y1 = polygon[0]
    for i in range(1, size + 1):
        x2, y2 = polygon[i % size]

        # if on the edges -> True
        if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2): return True
        if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2): return True

        if min(y1, y2) < y <= max(y1, y2) and x <= max(x1, x2):
            x_intersection = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if x1 == x2 or x <= x_intersection: inside = not inside
        x1, y1 = x2, y2
    return inside

def solve(lines):
    P = sorted([tuple(map(int, line.split(','))) for line in lines])
    # X, Y = find_lines(P)
    # print(X, Y)

    adj = find_adj(P)

    V = set()
    res = 0
    for i in adj:
        if i in V: continue
        visited = set()
        polygon = []
        found = find_polygon(i, i, adj, polygon, visited)
        if not found: continue
        # print(polygon)

        inside = {}
        for i in range(1, len(P)):
            pi = P[i]
            if pi not in inside: inside[pi] = is_inside(pi, polygon)
            if not inside[pi]:
                print(pi)
                continue

            for j in range(i):
                pj = P[j]
                if pj not in inside: inside[pj] = is_inside(pj, polygon)
                if not inside[pj]:
                    print(pj)
                    continue

                if  is_inside((pi[0], pj[1]), polygon) and is_inside((pj[0], pi[1]), polygon):
                    res = max(res, area(i, j, P))

        V = V.union(visited)
    return res

def read_lines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    return lines

if __name__ == "__main__":
    filename = 'test.txt'  # Change this to your actual filename
    lines = read_lines(filename)
    result = solve(lines)
    print(result)
    assert(result == 24)
