def optimalFreelancing(jobs: list[dict]) -> int:
    # sort jobs by start time
    jobs.sort(key=lambda x: x["payment"], reverse=True)

    days = [False] * 7
    total = 0

    for job in jobs:
        deadline = job["deadline"]
        payment = job["payment"]

        for day in range(min(deadline, 7) - 1, -1, -1):
            if not days[day]:
                days[day] = True
                total += payment
                break

    return total
