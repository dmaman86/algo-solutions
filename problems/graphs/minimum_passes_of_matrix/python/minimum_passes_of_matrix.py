from collections import deque
from copy import deepcopy


def is_valid(point: tuple[int, int], matrix: list[list[int]]) -> bool:
    x, y = point
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def init_queue(matrix: list[list[int]]) -> tuple[deque[tuple[int, int]], int]:
    queue: deque[tuple[int, int]] = deque()
    negatives = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                negatives += 1
            elif matrix[i][j] > 0:
                queue.append((i, j))

    return queue, negatives


def bfs(
    matrix: list[list[int]], q: deque[tuple[int, int]], negatives: int
) -> dict[int, list[list[int]]]:
    passes: int = 0
    history: dict[int, list[list[int]]] = {0: deepcopy(matrix)}

    while q and negatives > 0:
        size = len(q)
        converted = False

        for _ in range(size):
            x, y = q.popleft()

            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy

                if is_valid((nx, ny), matrix) and matrix[nx][ny] < 0:
                    matrix[nx][ny] = abs(matrix[nx][ny])
                    q.append((nx, ny))
                    negatives -= 1
                    converted = True

        if converted:
            passes += 1
            history[passes] = deepcopy(matrix)

    return history


def minimum_passes_of_matrix(
    matrix: list[list[int]],
) -> tuple[int, dict[int, list[list[int]]]]:

    q, negatives = init_queue(matrix)

    if negatives == 0:
        return 0, {0: matrix}

    history = bfs(matrix, q, negatives)
    negatives = sum(row.count(-1) for row in matrix)
    passes = max(history.keys(), default=0)

    return (passes if negatives == 0 else -1), history
