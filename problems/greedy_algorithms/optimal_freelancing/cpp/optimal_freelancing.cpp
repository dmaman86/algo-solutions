#include "optimal_freelancing.h"
#include <algorithm>

bool compareJobs(const std::unordered_map<std::string, int> &job1,
                 const std::unordered_map<std::string, int> &job2) {
  return job1.at("payment") > job2.at("payment");
}

int optimalFreelancing(std::vector<std::unordered_map<std::string, int>> jobs) {
  std::sort(jobs.begin(), jobs.end(), compareJobs);

  std::vector<bool> days(7, false);
  int totalProfit = 0;

  for (const auto &job : jobs) {
    int deadline = job.at("deadline");
    int payment = job.at("payment");
    bool done = false;

    for (int day = std::min(deadline, 7) - 1; day >= 0 && !done; day--) {
      if (!days[day]) {
        days[day] = true;
        totalProfit += payment;
        done = true;
      }
    }
  }
  return totalProfit;
}
