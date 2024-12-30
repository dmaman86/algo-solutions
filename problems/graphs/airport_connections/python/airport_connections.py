from collections import defaultdict, deque


def topo_sort_util(
    adj: dict[str, list[str]], v: str, visited: set[str], stack: deque
) -> None:
    visited.add(v)

    for i in adj[v]:
        if i not in visited:
            topo_sort_util(adj, i, visited, stack)

    stack.append(v)


def topo_sort(adj: dict[str, list[str]], airports: list[str]) -> deque:
    visited: set[str] = set()
    stack = deque()

    for airport in airports:
        if airport not in visited:
            topo_sort_util(adj, airport, visited, stack)

    return stack


def dfs(adj: dict[str, list[str]], v: str, visited: set[str]) -> None:
    visited.add(v)

    for i in adj[v]:
        if i not in visited:
            dfs(adj, i, visited)


def airport_connections(
    airports: list[str], routes: list[list[str]], starting_airport: str
) -> list[tuple[str, str]]:
    # idmp = {airport: idx for idx, airport in enumerate(airports)}
    # adj = defaultdict(list)
    adj: dict[str, list[str]] = defaultdict(list)

    for route in routes:
        u, v = route
        adj[u].append(v)

    stack: deque[str] = topo_sort(adj, airports)
    visited: set[str] = set()
    dfs(adj, starting_airport, visited)

    new_connections: list[tuple[str, str]] = []

    while stack:
        u = stack.pop()
        if u not in visited:
            new_connections.append((starting_airport, u))
            dfs(adj, u, visited)

    return new_connections
