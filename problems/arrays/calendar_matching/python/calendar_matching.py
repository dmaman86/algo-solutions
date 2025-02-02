def calendarMatching(
    calendar1: list[list[str]],
    dailyBounds1: list[str],
    calendar2: list[list[str]],
    dailyBounds2: list[str],
    meetingDuration: int,
) -> list[list[str]]:

    def time_to_minutes(time: str) -> int:
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    def minutes_to_time(minutes: int) -> str:
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours}:{mins:02d}"

    def update_calendar(
        calendar: list[list[str]], daily_bounds: list[str]
    ) -> list[list[int]]:
        start = time_to_minutes(daily_bounds[0])
        end = time_to_minutes(daily_bounds[1])
        END_OF_DAY = 1440

        filtered_calendar = [
            [time_to_minutes(start_time), time_to_minutes(end_time)]
            for start_time, end_time in calendar
            if time_to_minutes(end_time) > start and time_to_minutes(start_time) < end
        ]

        return [(0, start)] + filtered_calendar + [(end, END_OF_DAY)]

    def merge_calendars(
        calendar1: list[list[int]], calendar2: list[list[int]]
    ) -> list[list[int]]:
        merged: list[list[int]] = []
        i, j = 0, 0
        last: list[int] = [-1, -1]  # Tracks last merged interval

        while i < len(calendar1) or j < len(calendar2):
            if j >= len(calendar2) or (
                i < len(calendar1) and calendar1[i][0] < calendar2[j][0]
            ):
                meeting = list(calendar1[i])
                i += 1
            else:
                meeting = list(calendar2[j])
                j += 1

            if last[1] >= meeting[0]:
                last[1] = max(last[1], meeting[1])  # Merge overlapping intervals
            else:
                if last[0] != -1:
                    merged.append(last)
                last = meeting

        if last[0] != -1:
            merged.append(last)

        return merged

    def find_available_times(calendar: list[list[int]]) -> list[list[str]]:
        available: list[list[str]] = []
        for i in range(1, len(calendar)):
            previous_end = calendar[i - 1][1]
            current_start = calendar[i][0]
            if current_start - previous_end >= meetingDuration:
                available.append(
                    [minutes_to_time(previous_end), minutes_to_time(current_start)]
                )

        return available

    updated_calendar1: list[list[int]] = update_calendar(calendar1, dailyBounds1)
    updated_calendar2: list[list[int]] = update_calendar(calendar2, dailyBounds2)
    merged_calendar: list[list[int]] = merge_calendars(
        updated_calendar1, updated_calendar2
    )

    return find_available_times(merged_calendar)
