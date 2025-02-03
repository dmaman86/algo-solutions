export const minimumPassesOfMatrix = (() => {
  const movements = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
  ];

  const isValid = (point, matrix) => {
    const [row, col] = point;
    return (
      row >= 0 && row < matrix.length && col >= 0 && col < matrix[0].length
    );
  };

  const initQueue = (matrix) => {
    const queue = [];
    let negatives = 0;

    for (let i = 0; i < matrix.length; i++) {
      for (let j = 0; j < matrix[0].length; j++) {
        if (matrix[i][j] < 0) negatives++;
        else if (matrix[i][j] > 0) queue.push([i, j]);
      }
    }

    return { queue, negatives };
  };

  const bfs = (matrix, queue, negatives) => {
    let passes = 0;

    while (queue.length && negatives) {
      let size = queue.length;
      let converted = false;

      for (let i = 0; i < size; i++) {
        const [row, col] = queue.shift();

        for (const [rowMove, colMove] of movements) {
          const nx = row + rowMove;
          const ny = col + colMove;

          if (isValid([nx, ny], matrix) && matrix[nx][ny] < 0) {
            matrix[nx][ny] *= -1;
            negatives--;
            converted = true;
            queue.push([nx, ny]);
          }
        }
      }
      if (converted) passes++;
    }
    return { passes, negatives };
  };

  return (matrix) => {
    if (!matrix || !matrix.length || !matrix[0].length) return -1;

    const { queue, negatives: initialNegatives } = initQueue(matrix);

    if (initialNegatives === 0) return 0;

    const { passes, negatives } = bfs(matrix, queue, initialNegatives);

    return negatives === 0 ? passes : -1;
  };
})();
