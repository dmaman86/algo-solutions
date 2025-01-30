def validStartingCity(distances: list[int], fuel: list[int], mpg: int) -> int:
    remainingFuel = 0
    startCity = 0

    for i in range(len(distances)):
        remainingFuel += fuel[i] * mpg - distances[i]
        if remainingFuel < 0:
            remainingFuel = 0
            startCity = i + 1

    return startCity % len(distances)
