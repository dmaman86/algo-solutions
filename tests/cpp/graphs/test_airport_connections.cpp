#include "../../../problems/graphs/airport_connections/cpp/airport_connections.h"
#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

using Airports = std::vector<std::string>;
using Routes = std::vector<Airports>;

class TestAirportConnections : public ::testing::Test {
protected:
  void SetUp() override {
    std::string file_path =
        std::string(TEST_CASES_DIR) + "/graphs/airports_connections.json";
    std::ifstream f(file_path);

    if (!f.is_open())
      throw std::runtime_error("Could not open file");

    test_cases = json::parse(f);
  }
  json test_cases;
};

TEST_F(TestAirportConnections, TestCases) {
  for (const auto &test : test_cases) {
    auto airports = test["airports"].get<Airports>();
    auto routes = test["routes"].get<Routes>();
    auto starting_airport = test["startingAirport"].get<std::string>();
    auto expected = test["expected"].get<int>();

    auto result = airportConnections(airports, routes, starting_airport);

    EXPECT_EQ(result, expected)
        << "Test failed for test cases: " << test.dump(2);
  }
}
