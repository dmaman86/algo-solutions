def apartmentHunting(blocks: list[dict[str, bool]], reqs: list[str]) -> int:
    n = len(blocks)

    def get_min_distances() -> dict:
        min_distances = {req: [float("inf")] * n for req in reqs}

        def calculate_distances(start_idx: int, end_idx: int, step: int) -> None:
            for req in reqs:
                closest = -1
                for i in range(start_idx, end_idx, step):
                    if blocks[i].get(req, False):
                        closest = i
                    if closest != -1:
                        min_distances[req][i] = min(
                            min_distances[req][i], abs(i - closest)
                        )

        calculate_distances(0, n, 1)
        calculate_distances(n - 1, -1, -1)

        return min_distances

    min_distances = get_min_distances()
    max_distances_at_blocks = [
        max(min_distances[req][i] for req in reqs) for i in range(n)
    ]

    return min(range(n), key=lambda i: max_distances_at_blocks[i])
