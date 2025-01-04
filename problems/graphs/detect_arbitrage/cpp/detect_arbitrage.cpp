#include "detect_arbitrage.h"

#include <cmath>
#include <limits>

bool detectArbitrage(const std::vector<std::vector<double>> &exchangeRates) {
  int n = exchangeRates.size();

  std::vector<std::vector<double>> logExchangeRates(n, std::vector<double>(n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      logExchangeRates[i][j] = -std::log(exchangeRates[i][j]);
    }
  }

  auto hasNegativeCycle = [&]() -> bool {
    std::vector<double> distances(n, std::numeric_limits<double>::infinity());
    distances[0] = 0;

    for (int i = 0; i < n - 1; ++i) {
      for (int u = 0; u < n; ++u) {
        for (int v = 0; v < n; ++v) {
          if (distances[u] + logExchangeRates[u][v] < distances[v]) {
            distances[v] = distances[u] + logExchangeRates[u][v];
          }
        }
      }
    }

    for (int u = 0; u < n; ++u) {
      for (int v = 0; v < n; ++v) {
        if (distances[u] + logExchangeRates[u][v] < distances[v]) {
          return true;
        }
      }
    }
    return false;
  };

  return hasNegativeCycle();
}
