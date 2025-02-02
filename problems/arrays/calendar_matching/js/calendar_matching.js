export const calendarMatching = (() => {
  const timeToMinutes = (time) => {
    const [hours, minutes] = time.split(":").map(Number);
    return hours * 60 + minutes;
  };

  const minutesToTime = (minutes) => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours}:${mins < 10 ? "0" : ""}${mins}`;
  };

  const updateCalendar = (calendar, dailyBounds) => {
    const start = timeToMinutes(dailyBounds[0]);
    const end = timeToMinutes(dailyBounds[1]);
    const END_OF_DAY = 1440;

    const filteredCalendar = calendar
      .map(([startTime, endTime]) => [
        timeToMinutes(startTime),
        timeToMinutes(endTime),
      ])
      .filter(([startTime, endTime]) => endTime > start && startTime < end);

    return [[0, start], ...filteredCalendar, [end, END_OF_DAY]];
  };

  const mergeCalendars = (calendar1, calendar2) => {
    const merged = [];
    let i = 0,
      j = 0;
    let last = [-1, -1];
    while (i < calendar1.length || j < calendar2.length) {
      let meeting;
      if (
        j >= calendar2.length ||
        (i < calendar1.length && calendar1[i][0] < calendar2[j][0])
      ) {
        meeting = calendar1[i++];
      } else {
        meeting = calendar2[j++];
      }
      if (last[1] >= meeting[0]) {
        last[1] = Math.max(last[1], meeting[1]);
      } else {
        if (last[0] !== -1) merged.push(last);
        last = meeting;
      }
    }
    if (last[0] !== -1) merged.push(last);
    return merged;
  };

  const findAvailableTimes = (calendar, meetingDuration) => {
    const available = [];
    for (let i = 1; i < calendar.length; i++) {
      const previousEnd = calendar[i - 1][1];
      const currentStart = calendar[i][0];
      if (currentStart - previousEnd >= meetingDuration) {
        available.push([
          minutesToTime(previousEnd),
          minutesToTime(currentStart),
        ]);
      }
    }
    return available;
  };

  return (
    calendar1,
    dailyBounds1,
    calendar2,
    dailyBounds2,
    meetingDuration,
  ) => {
    const updatedCalendar1 = updateCalendar(calendar1, dailyBounds1);
    const updatedCalendar2 = updateCalendar(calendar2, dailyBounds2);
    const mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2);
    return findAvailableTimes(mergedCalendar, meetingDuration);
  };
})();
