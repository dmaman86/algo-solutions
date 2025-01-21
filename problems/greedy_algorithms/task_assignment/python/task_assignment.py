def task_assignment(k: int, tasks: list[int]) -> list[list[int]]:
    # pair each task value with its original index
    task_pairs: list[tuple[int, int]] = [
        (task, index) for index, task in enumerate(tasks)
    ]
    # sort the tasks by their values
    task_pairs.sort(key=lambda x: x[0])

    # pair the smallest and largest tasks
    result: list[list[int]] = []
    for i in range(k):
        result.append([task_pairs[i][1], task_pairs[-(i + 1)][1]])

    return result
