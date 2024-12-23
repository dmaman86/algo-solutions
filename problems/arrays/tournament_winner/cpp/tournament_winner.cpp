#include "tournament_winner.h"

std::string tournamentWinner(std::vector<std::vector<std::string>> competitions,
                             std::vector<int> results) {
  std::string winner = "";
  std::map<std::string, int> scores;

  for (auto i = 0; i < results.size(); i++) {
    auto current = competitions[i][!(results[i])];
    scores[current] += 3;
    if (scores[current] > scores[winner])
      winner = current;
  }

  return winner;
}
