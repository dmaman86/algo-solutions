export const aStarAlgorithm = (() => {
  const heuristic = (a, b) => Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);

  const getNeighbors = (node, rows, cols) => {
    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];
    const neighbors = [];
    for (const [dr, dc] of directions) {
      const neighbor = [node[0] + dr, node[1] + dc];
      if (
        neighbor[0] >= 0 &&
        neighbor[0] < rows &&
        neighbor[1] >= 0 &&
        neighbor[1] < cols
      ) {
        neighbors.push(neighbor);
      }
    }
    return neighbors;
  };

  const reconstructPath = (cameFrom, start, end) => {
    const path = [];
    let current = end;
    while (current in cameFrom) {
      path.push(current);
      current = cameFrom[current];
    }
    path.push(start);
    return path.reverse();
  };

  return (startRow, startCol, endRow, endCol, graph) => {
    const rows = graph.length;
    const cols = graph[0].length;

    const startNode = [startRow, startCol];
    const endNode = [endRow, endCol];

    const openSet = [];
    openSet.push({ node: startNode, fScore: 0 });

    const cameFrom = {};

    const gScore = Array(rows)
      .fill(null)
      .map(() => Array(cols).fill(Infinity));
    gScore[startRow][startCol] = 0;

    const fScore = Array(rows)
      .fill(null)
      .map(() => Array(cols).fill(Infinity));
    fScore[startRow][startCol] = heuristic(startNode, endNode);

    while (openSet.length) {
      openSet.sort((a, b) => a.fScore - b.fScore);
      const { node: current } = openSet.shift();

      if (current[0] === endRow && current[1] === endCol) {
        return reconstructPath(cameFrom, startNode, endNode);
      }

      for (const neighbor of getNeighbors(current, rows, cols)) {
        const [row, col] = neighbor;
        if (graph[row][col] === 0) {
          const tentativeGScore = gScore[current[0]][current[1]] + 1;

          if (tentativeGScore < gScore[row][col]) {
            cameFrom[neighbor] = current;
            gScore[row][col] = tentativeGScore;
            fScore[row][col] = gScore[row][col] + heuristic(neighbor, endNode);

            if (
              !openSet.some(
                (item) => item.node[0] === row && item.node[1] === col,
              )
            ) {
              openSet.push({ node: neighbor, fScore: fScore[row][col] });
            }
          }
        }
      }
    }
    return [];
  };
})();
