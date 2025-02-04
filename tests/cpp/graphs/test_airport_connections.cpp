#include "../../../problems/graphs/airport_connections/cpp/airport_connections.h"
#include "../jsontestbase.h"

#include <vector>

using Airports = std::vector<std::string>;
using Routes = std::vector<Airports>;

class TestAirportConnections : public JsonTestBase {
public:
  TestAirportConnections() {
    json_file_path =
        std::string(TEST_CASES_DIR) + "/graphs/airports_connections.json";
  }
};

TEST_F(TestAirportConnections, TestCases) {

  ASSERT_FALSE(test_cases.empty()) << "Test cases are empty";

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
