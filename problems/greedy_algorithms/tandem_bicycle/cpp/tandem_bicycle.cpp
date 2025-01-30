#include "tandem_bicycle.h"
#include <algorithm>

int tandemBicycle(std::vector<int> redShirtSpeeds,
                  std::vector<int> blueShirtSpeeds, bool fastest) {
  int totalSpeed = 0;
  std::sort(redShirtSpeeds.begin(), redShirtSpeeds.end());
  std::sort(blueShirtSpeeds.begin(), blueShirtSpeeds.end());

  if (fastest)
    std::reverse(blueShirtSpeeds.begin(), blueShirtSpeeds.end());

  for (int i = 0; i < redShirtSpeeds.size(); i++)
    totalSpeed += std::max(redShirtSpeeds[i], blueShirtSpeeds[i]);

  return totalSpeed;
}
