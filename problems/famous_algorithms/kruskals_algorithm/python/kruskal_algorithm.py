# from typing import List, Tuple
#
# Edge = Tuple[int, int, int]
# AdjacencyList = List[List[Tuple[int, int]]]
# MSTResult = Tuple[List[Edge], AdjacencyList]

Edge = tuple[int, int, int]
AdjacencyList = list[list[tuple[int, int]]]
MSTResult = tuple[list[Edge], AdjacencyList]


class UnionFind:
    def __init__(self, size: int):
        self.p = list(range(size))
        self.rank = [0] * size
        self.setSize = [1] * size
        self.numSets = size

    def findSet(self, i: int) -> int:
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]

    def isSameSet(self, i: int, j: int) -> bool:
        return self.findSet(i) == self.findSet(j)

    def unionSet(self, i: int, j: int):
        if not self.isSameSet(i, j):
            self.numSets -= 1
            x = self.findSet(i)
            y = self.findSet(j)
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
                self.setSize[x] += self.setSize[y]
            else:
                self.p[x] = y
                self.setSize[y] += self.setSize[x]
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

    def numDisjointSets(self):
        return self.numSets

    def sizeOfSet(self, i: int) -> int:
        return self.setSize[self.findSet(i)]


def kruskalsAlgorithm(edges: AdjacencyList) -> MSTResult:
    all_edges: list[Edge] = []

    for u in range(len(edges)):
        for v, w in edges[u]:
            if u < v:
                all_edges.append((w, u, v))

    all_edges.sort()

    mst_cost = 0
    num_taken = 0
    uf = UnionFind(len(edges))
    mst_edges: list[Edge] = []
    mst: AdjacencyList = [[] for _ in range(len(edges))]

    for w, u, v in all_edges:
        if num_taken == len(edges) - 1:
            break
        if not uf.isSameSet(u, v):
            num_taken += 1
            mst_cost += w
            uf.unionSet(u, v)
            mst_edges.append((u, v, w))
            mst[u].append((v, w))
            mst[v].append((u, w))

    return mst_edges, mst
