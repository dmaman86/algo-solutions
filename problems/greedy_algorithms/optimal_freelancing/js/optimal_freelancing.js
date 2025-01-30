export const optimalFreelancing = (jobs) => {
  jobs.sort((a, b) => b.payment - a.payment);
  const days = new Array(7).fill(false);
  let totalProfit = 0;

  for (const job of jobs) {
    const { deadline, payment } = job;
    let found = false;
    for (let day = Math.min(deadline, 7) - 1; day >= 0 && !found; day--) {
      if (!days[day]) {
        days[day] = found = true;
        totalProfit += payment;
      }
    }
  }
  return totalProfit;
};
