def minimumWaitingTime(queries: list[int]) -> int:
    queries.sort()
    total = 0
    query = 0

    for i in range(len(queries)):
        total += query * (len(queries) - i)
        query = queries[i]

    return total
