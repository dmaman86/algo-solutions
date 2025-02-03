export const detectArbitrage = (() => {
  const hasNegativeCycle = (exchangeRates) => {
    const distances = Array(exchangeRates.length).fill(Infinity);
    distances[0] = 0;
    const logExchangesRates = exchangeRates.map((row) =>
      row.map((rate) => -Math.log(rate)),
    );

    for (let i = 0; i < exchangeRates.length - 1; i++) {
      for (let u = 0; u < exchangeRates.length; u++) {
        for (let v = 0; v < exchangeRates.length; v++) {
          if (distances[u] + logExchangesRates[u][v] < distances[v]) {
            distances[v] = distances[u] + logExchangesRates[u][v];
          }
        }
      }
    }

    for (let u = 0; u < exchangeRates.length; u++) {
      for (let v = 0; v < exchangeRates.length; v++) {
        if (distances[u] + logExchangesRates[u][v] < distances[v]) {
          return true;
        }
      }
    }
    return false;
  };

  return (exchangeRates) => hasNegativeCycle(exchangeRates);
})();
