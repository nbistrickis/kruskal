def make_set(vertice, parent):
    parent[vertice] = vertice

# returns first element of set, which includes 'vertice'
def find_set(vertice):
    pass

# joins two sets: set, which includes 'vertice1' and set, which
# includes 'vertice2'
def union(vertice1, vertice2):
    pass

def kruskal(graph):
    mst = set()
    parent = dict()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice, parent)

    print(parent)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v)

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

kruskal(graph)
