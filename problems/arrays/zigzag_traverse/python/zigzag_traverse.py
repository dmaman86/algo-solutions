def zigzagTraverse(array: list[list[int]]) -> list[int]:
    if not array or not array[0]:
        return []

    dimension: dict = {"rows": len(array), "cols": len(array[0])}
    position: dict = {"x": 0, "y": 0}
    direction: dict = {"going_down": True}
    move_down: tuple[int, int] = [1, -1]
    move_up: tuple[int, int] = [-1, 1]

    def update_position(position: dict, limit: int) -> None:
        if position["x"] == limit - 1:
            position["y"] += 1
        else:
            position["x"] += 1

    def update_direction() -> tuple[bool, bool]:
        at_bottom_left = direction["going_down"] and (
            position["y"] == 0 or position["x"] == dimension["rows"] - 1
        )
        at_top_right = not direction["going_down"] and (
            position["x"] == 0 or position["y"] == dimension["cols"] - 1
        )

        if at_bottom_left or at_top_right:
            direction["going_down"] = not direction["going_down"]

        # Swap position if atTopRight
        if at_top_right:
            position["x"], position["y"] = position["y"], position["x"]

        return at_bottom_left, at_top_right

    def move_in_zigzag(move: tuple[int, int]) -> None:
        at_bottom_left, at_top_right = update_direction()

        if at_bottom_left:
            update_position(position, dimension["rows"])
        elif at_top_right:
            update_position(position, dimension["cols"])
            position["x"], position["y"] = position["y"], position["x"]
        else:
            position["x"] += move[0]
            position["y"] += move[1]

    result: list[int] = []
    while len(result) < dimension["rows"] * dimension["cols"]:
        result.append(array[position["x"]][position["y"]])
        move = move_down if direction["going_down"] else move_up
        move_in_zigzag(move)

    return result
