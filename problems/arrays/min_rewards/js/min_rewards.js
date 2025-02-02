export const minRewards = (scores) => {
  const n = scores.length;
  const rewards = new Array(n).fill(1);

  const traverse = (startIdx, endIdx, step) => {
    for (let i = startIdx; i !== endIdx; i += step) {
      if (scores[i] > scores[i - step]) {
        rewards[i] =
          step == 1
            ? rewards[i - step] + 1
            : Math.max(rewards[i], rewards[i - step] + 1);
      }
    }
  };

  traverse(1, n, 1);
  traverse(n - 2, -1, -1);

  return rewards.reduce((sum, reward) => sum + reward, 0);
};
