from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iadd__(self, move: Point) -> Point:
        self.x += move.x
        self.y += move.y
        return self

    def __lt__(self, other: Point) -> bool:
        return self.x < other.x and self.y < other.y


def zigzagTraverse(array: list[list[int]]) -> list[int]:
    if not array or not array[0]:
        return []

    point = Point(0, 0)
    dimension = Point(len(array), len(array[0]))
    direction = {"going_down": True}

    def check_boundary() -> tuple[bool, bool]:
        at_bottom_left = direction["going_down"] and (
            point.y == 0 or point.x == dimension.x - 1
        )
        at_top_right = not direction["going_down"] and (
            point.x == 0 or point.y == dimension.y - 1
        )

        if at_bottom_left or at_top_right:
            direction["going_down"] = not direction["going_down"]

        return at_bottom_left, at_top_right

    def next_position(at_top_right: bool) -> Point:
        position = Point(point.y, point.x) if at_top_right else point
        limit = dimension.y if at_top_right else dimension.x

        if position.x == limit - 1:
            position.y += 1
        else:
            position.x += 1

        return Point(position.y, position.x) if at_top_right else position

    move_down = Point(1, -1)
    move_up = Point(-1, 1)

    result: list[int] = []
    while len(result) < dimension.x * dimension.y:
        if point < dimension:
            result.append(array[point.x][point.y])

        at_bottom_left, at_top_right = check_boundary()
        if not at_bottom_left and not at_top_right:
            point += move_down if direction["going_down"] else move_up
        else:
            point = next_position(at_top_right)

    return result
