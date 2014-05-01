parent = dict()

def make_set(vertice):
    parent[vertice] = vertice

# returns first element of set, which includes 'vertice'
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]

# joins two sets: set, which includes 'vertice1' and set, which
# includes 'vertice2'
def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    # if u and v are not connected by a path
    if ancestor1 != ancestor2:
        for edge in edges:
            parent[ancestor1] = ancestor2

def kruskal(graph):
    mst = set()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)

    return mst

# input graph
graph = {
        'V': ['A', 'B', 'C', 'D', 'E', 'F'],
        'E': set([
            (1, 'A', 'B'),
            (5, 'A', 'C'),
            (3, 'A', 'D'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            (4, 'B', 'C'),
            (3, 'C', 'F'),
            (1, 'D', 'E'),
            (6, 'E', 'F'),
             ])
        }

print("Minimal Spanning Tree:")
print(kruskal(graph))
