export const classPhotos = (redShirtHeights, blueShirtHeights) => {
  redShirtHeights.sort((a, b) => a - b);
  blueShirtHeights.sort((a, b) => a - b);

  const diff = redShirtHeights[0] - blueShirtHeights[0];

  for (let i = 0; i < redShirtHeights.length; i++) {
    if ((redShirtHeights[i] - blueShirtHeights[i]) * diff <= 0) return false;
  }
  return true;
};
