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
    parent1 = find_set(u)
    parent2 = find_set(v)
    # if u and v are not connected by a path
    if parent1 != parent2:
        

def kruskal(graph):
    mst = set()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice)

    print("Starting sets:")
    print(parent)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)
            print(parent)
    print("final sets")
    print(parent)

    return mst

graph = {
        'V': ['A','B', 'C', 'D'],
        'E': set([
            (1, 'A', 'B'),
            (1, 'A', 'C'),
            (2, 'A', 'D'),
            (3, 'B', 'D'),
            (2, 'C', 'D'),
             ])
        }

print(kruskal(graph))
