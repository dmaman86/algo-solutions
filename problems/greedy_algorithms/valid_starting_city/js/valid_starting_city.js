export const validStartingCity = (distances, fuel, mpg) => {
  const n = distances.length;
  let remainingFuel = 0;
  let startCity = 0;

  for (let i = 0; i < n; i++) {
    remainingFuel += fuel[i] * mpg - distances[i];
    if (remainingFuel < 0) {
      remainingFuel = 0;
      startCity = i + 1;
    }
  }
  return startCity % n;
};
