#include "valid_starting_city.h"

int validStartingCity(std::vector<int> distances, std::vector<int> fuel,
                      int mpg) {

  int remainingFuel = 0;
  int startCity = 0;

  for (size_t i = 0; i < distances.size(); i++) {
    remainingFuel += fuel[i] * mpg - distances[i];
    if (remainingFuel < 0) {
      startCity = i + 1;
      remainingFuel = 0;
    }
  }
  return startCity % distances.size();
}
