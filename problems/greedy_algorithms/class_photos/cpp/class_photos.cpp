#include "class_photos.h"
#include <algorithm>

bool classPhotos(std::vector<int> redShirtHeights,
                 std::vector<int> blueShirtHeights) {
  std::sort(redShirtHeights.begin(), redShirtHeights.end());
  std::sort(blueShirtHeights.begin(), blueShirtHeights.end());

  int diff = redShirtHeights[0] - blueShirtHeights[0];

  for (size_t i = 0; i < redShirtHeights.size(); i++) {
    if ((redShirtHeights[i] - blueShirtHeights[i]) * diff <= 0)
      return false;
  }
  return true;
}
