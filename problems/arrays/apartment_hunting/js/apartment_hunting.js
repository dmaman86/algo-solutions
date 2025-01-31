export const apartmentHunting = (blocks, reqs) => {
  const n = blocks.length;

  const getMinDistances = () => {
    const minDistances = Object.fromEntries(
      reqs.map((req) => [req, new Array(n).fill(Infinity)]),
    );

    const calculateDistances = (startIdx, endIdx, step) => {
      for (const req of reqs) {
        let closest = -1;
        for (let i = startIdx; i !== endIdx; i += step) {
          if (blocks[i][req]) closest = i;
          if (closest !== -1)
            minDistances[req][i] = Math.min(
              minDistances[req][i],
              Math.abs(i - closest),
            );
        }
      }
    };

    calculateDistances(0, n, 1);
    calculateDistances(n - 1, -1, -1);

    return minDistances;
  };

  const minDistances = getMinDistances();

  const maxDistancesAtBlocks = new Array(n)
    .fill(0)
    .map((_, i) => Math.max(...reqs.map((req) => minDistances[req][i])));

  return maxDistancesAtBlocks.indexOf(Math.min(...maxDistancesAtBlocks));
};
