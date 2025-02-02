export const zigzagTraverse = (() => {
  const updatePosition = (position, limit) => {
    if (position.x === limit - 1) position.y++;
    else position.x++;
  };

  const updateDirection = (position, dimension, direction) => {
    const atBottomLeft =
      direction.goingDown &&
      (position.y === 0 || position.x === dimension.rows - 1);
    const atTopRight =
      !direction.goingDown &&
      (position.x === 0 || position.y === dimension.cols - 1);

    if (atBottomLeft || atTopRight) direction.goingDown = !direction.goingDown;

    if (atTopRight) [position.x, position.y] = [position.y, position.x];

    return { atBottomLeft, atTopRight };
  };

  const moveInZigzag = (position, dimension, direction, move) => {
    const { atBottomLeft, atTopRight } = updateDirection(
      position,
      dimension,
      direction,
    );

    if (atBottomLeft) updatePosition(position, dimension.rows);
    else if (atTopRight) {
      updatePosition(position, dimension.cols);
      [position.x, position.y] = [position.y, position.x];
    } else {
      position.x += move[0];
      position.y += move[1];
    }
  };

  return (array) => {
    if (!array || !array.length) return [];

    const dimension = { rows: array.length, cols: array[0].length };
    const position = { x: 0, y: 0 };
    const direction = { goingDown: true };
    const moveDown = [1, -1];
    const moveUp = [-1, 1];
    let result = [];

    while (result.length < dimension.rows * dimension.cols) {
      result.push(array[position.x][position.y]);
      const move = direction.goingDown ? moveDown : moveUp;
      moveInZigzag(position, dimension, direction, move);
    }
    return result;
  };
})();
