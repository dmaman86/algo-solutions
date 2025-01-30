export const lineThroughPoints = (() => {
  const gcd = (a, b) => {
    while (b !== 0) [a, b] = [b, a % b];

    return a;
  };

  const normalize = (dx, dy) => {
    const gcdVal = gcd(dx, dy);
    dx /= gcdVal;
    dy /= gcdVal;

    if (dx < 0) {
      dx = -dx;
      dy = -dy;
    }
    return [dx, dy];
  };

  const getMaxPoints = (index, points, p1) => {
    const slopes = new Map();
    let duplicate = 1;
    const [x1, y1] = p1;

    for (let j = index + 1; j < points.length; j++) {
      const [x2, y2] = points[j];

      if (x1 === x2 && y1 === y2) {
        duplicate++;
        continue;
      }
      let [dx, dy] = normalize(x2 - x1, y2 - y1);
      const slope = `${dy}/${dx}`;
      slopes.set(slope, (slopes.get(slope) || 0) + 1);
    }
    return (slopes.size ? Math.max(...slopes.values()) : 0) + duplicate;
  };

  return (points) => {
    if (points.length < 3) return points.length;

    let maxPoints = 0;

    for (let i = 0; i < points.length; i++) {
      maxPoints = Math.max(maxPoints, getMaxPoints(i, points, points[i]));
    }
    return maxPoints;
  };
})();
