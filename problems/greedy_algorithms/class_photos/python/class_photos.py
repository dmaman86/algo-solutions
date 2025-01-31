def classPhotos(redShirtHeights: list[int], blueShirtHeights: list[int]) -> bool:
    redShirtHeights.sort()
    blueShirtHeights.sort()

    diff = redShirtHeights[0] - blueShirtHeights[0]

    for i in range(len(redShirtHeights)):
        if (redShirtHeights[i] - blueShirtHeights[i]) * diff <= 0:
            return False
    return True
