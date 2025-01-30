def tandemBicycle(
    redShirtSpeeds: list[int], blueShirtSpeeds: list[int], fastest: bool
) -> int:
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        redShirtSpeeds.reverse()

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return totalSpeed
