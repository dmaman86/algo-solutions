export const tandemBicycle = (redShirtSpeeds, blueShirtSpeeds, fastest) => {
  redShirtSpeeds.sort((a, b) => a - b);
  blueShirtSpeeds.sort((a, b) => a - b);

  if (fastest) {
    redShirtSpeeds.reverse();
  }

  let totalSpeed = 0;
  for (let i = 0; i < redShirtSpeeds.length; i++) {
    totalSpeed += Math.max(redShirtSpeeds[i], blueShirtSpeeds[i]);
  }

  return totalSpeed;
};
