#include <fstream>
#include <gtest/gtest.h>
#include <nlohmann/json.hpp>
#include <stdexcept>
#include <string>

using json = nlohmann::json;

class JsonTestBase : public ::testing::Test {
protected:
  void SetUp() override {
    if (json_file_path.empty()) {
      throw std::runtime_error("json_file_path is empty");
    }
    std::ifstream ifs(json_file_path);
    if (!ifs.is_open()) {
      throw std::runtime_error("Failed to open file: " + json_file_path);
    }
    test_cases = json::parse(ifs);
  }

  std::string json_file_path;
  json test_cases;
};
