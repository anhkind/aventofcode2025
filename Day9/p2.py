from collections import defaultdict

def area(i, j, P):
    x1, y1 = P[i]
    x2, y2 = P[j]
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def adjacent(i, j, adj):
    if i not in adj: adj[i] = list()
    if j not in adj: adj[j] = list()
    adj[i].append(j)
    adj[j].append(i)

def find_adj(P):
    adj = {}
    X, Y = {}, {}
    for i, [x, y] in enumerate(P):
        if x in Y:
            adjacent(i, Y[x], adj)
        if y in X:
            adjacent(i, X[y], adj)
        Y[x] = i
        X[y] = i
    return adj

def find_polygon(i, i0, adj, polygon, visited, P):
    if i == i0 and len(polygon) > 2: return True
    for j in adj[i]:
        if j not in visited:
            visited.add(j)
            polygon.append(P[j])
            found = find_polygon(j, i0, adj, polygon, visited, P)
            if found: return found
            polygon.pop()
            visited.remove(j)
    return False

def is_inside(x, y, polygon):
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
    P = sorted([list(map(int, line.split(','))) for line in lines])
    adj = find_adj(P)

    V = set()
    res = 0
    for i in adj:
        if i in V: continue
        visited = set()
        polygon = []
        found = find_polygon(i, i, adj, polygon, visited, P)
        if not found: continue
        # print(polygon)

        inside = {}
        for i in range(1, len(P)):
            x1, y1 = P[i]
            if (x1, y1) not in inside: inside[(x1, y1)] = is_inside(x1, y1, polygon)
            if not inside[(x1, y1)]:
                print(x1, y1)
                continue

            for j in range(i):
                x2, y2 = P[j]
                if (x2, y2) not in inside: inside[(x2, y2)] = is_inside(x2, y2, polygon)
                if not inside[(x2, y2)]:
                    print(x2, y2)
                    continue

                if  is_inside(x1, y2, polygon) and is_inside(x2, y1, polygon):
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
