from collections import defaultdict, deque
from enum import Enum


class State(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


def build_graph(jobs: list[int], deps: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph = defaultdict(list)
    for job in jobs:
        graph[job] = []
    for prereq, job in deps:
        graph[prereq].append(job)
    return graph


def topological_sort(
    jobs: list[int], deps: list[tuple[int, int]]
) -> tuple[list[int], dict[int, list[int]]]:

    graph = build_graph(jobs, deps)
    states = {job: State.UNVISITED for job in jobs}
    order = deque()

    def dfs(job: int) -> bool:
        if states[job] == State.VISITING:
            return False
        if states[job] == State.UNVISITED:
            states[job] = State.VISITING
            for neighbor in graph[job]:
                if not dfs(neighbor):
                    return False
            states[job] = State.VISITED
            order.appendleft(job)
        return True

    for job in jobs:
        if states[job] == State.UNVISITED and not dfs(job):
            return [], graph

    return list(order), graph
