import heapq

AdjacencyList = list[list[list[int]]]


def primsAlgorithm(edges: AdjacencyList) -> AdjacencyList:
    num_vertex = len(edges)
    in_mst = [False] * num_vertex
    mst_edges = [[] for _ in range(num_vertex)]
    min_heap = [(0, 0, -1)]

    while min_heap:
        weight, current_vertex, parent_vertex = heapq.heappop(min_heap)
        if in_mst[current_vertex]:
            continue

        in_mst[current_vertex] = True
        if parent_vertex != -1:
            mst_edges[parent_vertex].append([current_vertex, weight])
            mst_edges[current_vertex].append([parent_vertex, weight])

        for neighbor, edge_weight in edges[current_vertex]:
            if not in_mst[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return mst_edges
