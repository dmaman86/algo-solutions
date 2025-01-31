export const countSquares = (points) => {
  const pointMap = new Map();
  for (const [x, y] of points) pointMap.set([x, y].toString(), true);

  let count = 0;
  const rotationClockwise = [0, 1, -1, 0];
  const rotationCounterClockwise = [0, -1, 1, 0];

  const rotate = (point, matrix) => {
    return {
      x: matrix[0] * point.x + matrix[1] * point.y,
      y: matrix[2] * point.x + matrix[3] * point.y,
    };
  };

  const hasPoint = (point) => pointMap.has(point.toString());

  const checkSquare = (p1, p2, vector, matrix) => {
    const rotatedVector = rotate(vector, matrix);
    const p3 = [p1.x + rotatedVector.x, p1.y + rotatedVector.y];
    const p4 = [p2.x + rotatedVector.x, p2.y + rotatedVector.y];

    return hasPoint(p3) && hasPoint(p4) ? 1 : 0;
  };

  for (let i = 0; i < points.length; i++) {
    const p1 = { x: points[i][0], y: points[i][1] };
    for (let j = i + 1; j < points.length; j++) {
      const p2 = { x: points[j][0], y: points[j][1] };

      const dx = p2.x - p1.x;
      const dy = p2.y - p1.y;

      count += checkSquare(p1, p2, { x: dx, y: dy }, rotationClockwise);
      count += checkSquare(p1, p2, { x: dx, y: dy }, rotationCounterClockwise);
    }
  }
  return count / 4;
};
