import math


def detectArbitrage(exchangeRates: list[list[float]]) -> bool:
    logExchangeRates: list[list[float]] = [
        [-math.log(rate) for rate in row] for row in exchangeRates
    ]
    n: int = len(logExchangeRates)

    def hasNegativeCycle() -> bool:
        distances: list[int] = [float("inf")] * n
        distances[0] = 0

        for _ in range(n - 1):
            for u in range(n):
                for v in range(n):
                    if distances[u] + logExchangeRates[u][v] < distances[v]:
                        distances[v] = distances[u] + logExchangeRates[u][v]

        for u in range(n):
            for v in range(n):
                if distances[u] + logExchangeRates[u][v] < distances[v]:
                    return True

        return False

    return hasNegativeCycle()
