def countSquares(points: list[list[int]]) -> int:
    point_map = {tuple(point): True for point in points}
    count = 0
    rotation_clockwise = [0, 1, -1, 0]
    rotation_counter_clockwise = [0, -1, 1, 0]

    def rotate(point: dict, matrix: list[int]) -> dict:
        return {
            "x": matrix[0] * point["x"] + matrix[1] * point["y"],
            "y": matrix[2] * point["x"] + matrix[3] * point["y"],
        }

    def has_point(point: dict) -> bool:
        return tuple([point["x"], point["y"]]) in point_map

    def check_square(p1: dict, p2: dict, vector: dict, matrix: list[int]) -> int:
        rotated_vector = rotate(vector, matrix)
        p3 = {"x": p1["x"] + rotated_vector["x"], "y": p1["y"] + rotated_vector["y"]}
        p4 = {"x": p2["x"] + rotated_vector["x"], "y": p2["y"] + rotated_vector["y"]}
        return 1 if has_point(p3) and has_point(p4) else 0

    for i in range(len(points)):
        p1 = {"x": points[i][0], "y": points[i][1]}
        for j in range(i + 1, len(points)):
            p2 = {"x": points[j][0], "y": points[j][1]}

            dx = p2["x"] - p1["x"]
            dy = p2["y"] - p1["y"]

            count += check_square(p1, p2, {"x": dx, "y": dy}, rotation_clockwise)
            count += check_square(
                p1, p2, {"x": dx, "y": dy}, rotation_counter_clockwise
            )

    return count // 4
