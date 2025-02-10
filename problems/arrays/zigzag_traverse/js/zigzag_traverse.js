class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  add(move) {
    this.x += move.x;
    this.y += move.y;
  }

  isLessThan(other) {
    return this.x < other.x && this.y < other.y;
  }
}

export const zigzagTraverse = (() => {
  const checkBoundary = (point, dim, direction) => {
    const atBottomLeft =
      direction.goingDown && (point.y === 0 || point.x === dim.x - 1);
    const atTopRight =
      !direction.goingDown && (point.x === 0 || point.y === dim.y - 1);

    if (atBottomLeft || atTopRight) direction.goingDown = !direction.goingDown;

    return { atBottomLeft, atTopRight };
  };

  const nextPosition = (point, dim, atTopRight) => {
    let position = atTopRight ? new Point(point.y, point.x) : point;
    const limit = atTopRight ? dim.y : dim.x;

    if (position.x === limit - 1) position.y++;
    else position.x++;

    return atTopRight ? new Point(position.y, position.x) : position;
  };

  return (array) => {
    if (!array || !array.length) return [];

    let point = new Point(0, 0);
    const dim = new Point(array.length, array[0].length);
    const result = [];
    const direction = { goingDown: true };

    const moveDown = new Point(1, -1);
    const moveUp = new Point(-1, 1);

    while (result.length < dim.x * dim.y) {
      if (point.isLessThan(dim)) result.push(array[point.x][point.y]);

      const { atBottomLeft, atTopRight } = checkBoundary(point, dim, direction);
      if (!atBottomLeft && !atTopRight)
        point.add(direction.goingDown ? moveDown : moveUp);
      else point = nextPosition(point, dim, atTopRight);
    }

    return result;
  };
})();
