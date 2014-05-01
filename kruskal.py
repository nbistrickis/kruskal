def make_set(vertice):
    pass

def find_set(vertice):
    pass

def union(vertice1, vertice2):
    pass

def kruskal(graph):
    mst = set()
    for vertice in graph['vertices']:
        make_set(vertice)

    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v)

    return mst
