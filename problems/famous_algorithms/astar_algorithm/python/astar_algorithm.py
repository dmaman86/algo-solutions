import heapq
from typing import Generator


def heuristic(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(
    node: tuple[int, int], rows: int, cols: int
) -> Generator[tuple[int, int], None, None]:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        neighbor = (node[0] + dr, node[1] + dc)
        if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
            yield neighbor


def reconstruct_path(
    came_from: dict[tuple[int, int], tuple[int, int]],
    start: tuple[int, int],
    end: tuple[int, int],
) -> list[list[int]]:
    current = end
    path = []
    while current in came_from:
        path.append([current[0], current[1]])
        current = came_from[current]
    path.append([start[0], start[1]])
    return path[::-1]


def aStarAlgorithm(
    startRow: int, startCol: int, endRow: int, endCol: int, graph: list[list[int]]
) -> list[list[int]]:
    rows, cols = len(graph), len(graph[0])
    start_node: tuple[int, int] = (startRow, startCol)
    end_node: tuple[int, int] = (endRow, endCol)

    open_set: list[tuple[int, tuple[int, int]]] = []
    heapq.heappush(open_set, (0, start_node))

    came_from: dict[tuple[int, int], tuple[int, int]] = {}
    g_score: dict[tuple[int, int], float] = {
        node: float("inf")
        for row in range(rows)
        for node in [(row, col) for col in range(cols)]
    }
    g_score[start_node] = 0

    f_score: dict[tuple[int, int], float] = {
        node: float("inf")
        for row in range(rows)
        for node in [(row, col) for col in range(cols)]
    }
    f_score[start_node] = heuristic(start_node, end_node)

    while open_set:
        current: tuple[int, int] = heapq.heappop(open_set)[1]

        if current == end_node:
            return reconstruct_path(came_from, start_node, end_node)

        for neighbor in get_neighbors(current, rows, cols):
            row, col = neighbor
            if graph[row][col] == 0:
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(
                        neighbor, end_node
                    )
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []
