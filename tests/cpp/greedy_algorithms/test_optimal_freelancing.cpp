#include "../../../problems/greedy_algorithms/optimal_freelancing/cpp/optimal_freelancing.h"
#include "../jsontestbase.h"

#include <nlohmann/json.hpp>
#include <unordered_map>
#include <vector>

using json = nlohmann::json;

class OptimalFreelancingTest : public JsonTestBase {
public:
  OptimalFreelancingTest() {
    json_file_path = std::string(TEST_CASES_DIR) +
                     "/greedy_algorithms/optimal_freelancing.json";
  }
};

std::vector<std::unordered_map<std::string, int>>
buildList(const json &jsonJobs) {
  std::vector<std::unordered_map<std::string, int>> jobs;
  for (const auto &job : jsonJobs) {
    std::unordered_map<std::string, int> jobMap;
    jobMap["deadline"] = job["deadline"];
    jobMap["payment"] = job["payment"];
    jobs.push_back(jobMap);
  }
  return jobs;
}

TEST_F(OptimalFreelancingTest, TestCases) {
  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty or not loaded";

  for (const auto &test : test_cases) {
    auto jobs = buildList(test["jobs"]);
    int expected = test["expected"];

    auto result = optimalFreelancing(jobs);

    EXPECT_EQ(result, expected) << "Failed for test: " << test.dump(2);
  }
}
