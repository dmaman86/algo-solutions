export const minimumWaitingTime = (queries) => {
  queries.sort((a, b) => a - b);

  let total = 0,
    query = 0;

  for (let i = 0; i < queries.length; i++) {
    total += query * (queries.length - i);
    query = queries[i];
  }
  return total;
};
