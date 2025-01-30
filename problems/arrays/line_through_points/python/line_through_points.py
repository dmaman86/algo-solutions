from collections import defaultdict
from math import gcd


def normalize(dx: int, dy: int) -> tuple[int, int]:
    def compute_gcd(a: int, b: int) -> int:
        return gcd(a, b) if b != 0 else a

    gcd_val = compute_gcd(dx, dy)
    dx //= gcd_val
    dy //= gcd_val
    if dx < 0:
        dx, dy = -dx, -dy

    return dx, dy


def get_max_points(index: int, points: list[list[int]], p1: tuple[int, int]) -> int:
    slopes = defaultdict(int)
    duplicate = 1
    x1, y1 = p1

    for j in range(index + 1, len(points)):
        x2, y2 = points[j]
        if x1 == x2 and y1 == y2:
            duplicate += 1
            continue

        dx, dy = normalize(x2 - x1, y2 - y1)
        slopes[(dx, dy)] += 1

    return max(slopes.values(), default=0) + duplicate


def lineThroughPoints(points: list[list[int]]) -> int:
    if len(points) < 3:
        return len(points)

    max_points = 0
    for i in range(len(points)):
        max_points = max(
            max_points, get_max_points(i, points, [points[i][0], points[i][1]])
        )

    return max_points
