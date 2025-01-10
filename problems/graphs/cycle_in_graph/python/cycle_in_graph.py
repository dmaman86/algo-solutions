from enum import Enum


class VisitState(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class State:
    def __init__(self):
        self.hasCycle = False


def dfs(
    node: int, visited: dict[int, VisitState], edges: list[list[int]], state: State
) -> None:
    if state.hasCycle:
        return

    if visited.get(node) == VisitState.VISITING:
        state.hasCycle = True
        return

    visited[node] = VisitState.VISITING
    for neighbor in edges[node]:
        dfs(neighbor, visited, edges, state)

    visited[node] = VisitState.VISITED


def cycleInGraph(edges: list[list[int]]) -> bool:
    visited: dict[int, VisitState] = {}
    state = State()

    for i in range(len(edges)):
        if not state.hasCycle:
            dfs(i, visited, edges, state)

    return state.hasCycle
