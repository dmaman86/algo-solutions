import heapq


def init_distance_and_queue(
    start: int, n: int
) -> tuple[list[float], list[tuple[float, int]]]:
    distances = [float("inf")] * n
    distances[start] = 0
    pq = [(0, start)]
    return distances, pq


def relax_edges(
    current_vertex: int,
    current_distance: float,
    edges: list[list[tuple[int, int]]],
    distances: list[float],
    pq: list[tuple[float, int]],
    previous: list[int],
) -> None:
    for edge in edges[current_vertex]:
        if len(edge) != 2:
            continue
        neighbor, weight = edge
        new_distance = current_distance + weight

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heapq.heappush(pq, (new_distance, neighbor))
            previous[neighbor] = current_vertex


def dijkstra(
    start: int, edges: list[list[tuple[int, int]]]
) -> tuple[list[float], list[int]]:
    distances, pq = init_distance_and_queue(start, len(edges))
    previous = [-1] * len(edges)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        relax_edges(current_vertex, current_distance, edges, distances, pq, previous)

    return distances, previous


def convert_unreachable_to_negative_one(distances: list[float]) -> list[int]:
    return [-1 if x == float("inf") else x for x in distances]


def dijkstra_algorithm(
    start: int, edges: list[list[tuple[int, int]]]
) -> tuple[list[int], list[int]]:
    distances, previous = dijkstra(start, edges)
    distances = convert_unreachable_to_negative_one(distances)
    return distances, previous
