# AlgoExpert Solutions

[![CI](https://github.com/dmaman86/algo-solutions/actions/workflows/ci.yml/badge.svg)](https://github.com/dmaman86/algo-solutions/actions/workflows/ci.yml)

This repository contains solutions to a wide range of algorithmic problems, categorized by topics such as Arrays, Binary Trees, Graphs, Dynamic Programming, and more.
Each problem is solved in multiple programming languages (JavaScript, Python, and C++) and includes unit tests for verification.

## 📖 Table of Contents

- [Summary of Problems](#summary-of-problems)
- [🚀 Quick Start](#quick-start)
- [🔧 How To Use This Project (Workflow)](#how-to-use-this-project-workflow)
  1. [Set Up the Environment](#1-set-up-the-environment)
  2. [Run Tests](#2-run-tests)
  3. [Run Tests with Visualizations (Python only)](#3-run-tests-with-visualizations-python-only)
  4. [Clean the Project](#4-clean-the-project)
  5. [Help](#5-help)
- [📂 Project Structure](#project-structure)
  - [🗂 Folder Breakdown](#folder-breakdown)
- [🔹 Notes](#notes)

<!-- START_TABLE -->
## Summary of Problems

| Topic               | Number of Problems |
|---------------------|--------------------|
| [Arrays](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays) | 12 |
| [Binary Search Trees](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees) | 4 |
| [Binary Trees](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees) | 6 |
| [Famous Algorithms](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms) | 6 |
| [Graphs](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs) | 6 |
| [Greedy Algorithms](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms) | 6 |
| [Dynamic Programming](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming) | 4 |
|---------------------|--------------------|
| **Total**          | **44**           |

### Difficulty Legend
| Emoji | Difficulty |
|--------|------------|
| 🟢 | Easy |
| 🟡 | Medium |
| 🔴 | Hard |
| ⚫ | Very hard |

### Arrays Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Sorted Squared Array](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/sorted_squared_array) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/sorted_squared_array/js) |
| 2   | [Tournament Winner](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner/js), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/tournament_winner/cpp) |
| 3   | [Two Number Sum](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/two_number_sum) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/two_number_sum/js) |
| 4   | [Validate Subsequence](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/validate_subsequence/python) |
| 5   | [Four Number Sum](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum) | <p align='center'>🔴</p> | [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum/cpp), [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/four_number_sum/js) |
| 6   | [Subarray Sort](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/subarray_sort) | <p align='center'>🔴</p> | [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/subarray_sort/cpp), [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/subarray_sort/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/subarray_sort/python) |
| 7   | [Count Squares](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/count_squares) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/count_squares/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/count_squares/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/count_squares/cpp) |
| 8   | [Zigzag Traverse](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/zigzag_traverse) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/zigzag_traverse/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/zigzag_traverse/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/zigzag_traverse/cpp) |
| 9   | [Min Rewards](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/min_rewards) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/min_rewards/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/min_rewards/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/min_rewards/cpp) |
| 10  | [Apartment Hunting](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/apartment_hunting) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/apartment_hunting/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/apartment_hunting/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/apartment_hunting/cpp) |
| 11  | [Line Through Points](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/line_through_points) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/line_through_points/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/line_through_points/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/line_through_points/cpp) |
| 12  | [Calendar Matching](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/calendar_matching) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/calendar_matching/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/calendar_matching/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/arrays/calendar_matching/cpp) |

### Binary search trees Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Repair Bst](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/repair_bst/cpp) |
| 2   | [Same Bsts](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/same_bsts) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/same_bsts/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/same_bsts/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/same_bsts/cpp) |
| 3   | [Validate Three Nodes](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/validate_three_nodes) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/validate_three_nodes/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/validate_three_nodes/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/validate_three_nodes/cpp) |
| 4   | [Right Smaller Than](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/right_smaller_than) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/right_smaller_than/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/right_smaller_than/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_search_trees/right_smaller_than/cpp) |

### Binary trees Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Find Nodes Distance K](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/find_nodes_distance_k) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/find_nodes_distance_k/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/find_nodes_distance_k/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/find_nodes_distance_k/cpp) |
| 2   | [Max Path Sum In Binary Tree](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/max_path_sum_in_binary_tree) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/max_path_sum_in_binary_tree/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/max_path_sum_in_binary_tree/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/max_path_sum_in_binary_tree/cpp) |
| 3   | [Compare Leaf Traversal](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/compare_leaf_traversal) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/compare_leaf_traversal/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/compare_leaf_traversal/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/compare_leaf_traversal/cpp) |
| 4   | [Right Sibling Tree](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/right_sibling_tree) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/right_sibling_tree/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/right_sibling_tree/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/right_sibling_tree/cpp) |
| 5   | [Flatten Binary Tree](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/flatten_binary_tree) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/flatten_binary_tree/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/flatten_binary_tree/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/flatten_binary_tree/cpp) |
| 6   | [All Kinds Of Node Depths](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/all_kinds_of_node_depths) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/all_kinds_of_node_depths/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/all_kinds_of_node_depths/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/binary_trees/all_kinds_of_node_depths/cpp) |

### Famous algorithms Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Kadanes Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm/js), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kadanes_algorithm/cpp) |
| 2   | [Dijkstras Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/dijkstras_algorithm/cpp) |
| 3   | [Kruskals Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/kruskals_algorithm/cpp) |
| 4   | [Prims Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/prims_algorithm/cpp) |
| 5   | [Topological Sort](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/topological_sort/cpp) |
| 6   | [Astar Algorithm](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/famous_algorithms/astar_algorithm/cpp) |

### Graphs Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Minimum Passes Of Matrix](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/minimum_passes_of_matrix) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/minimum_passes_of_matrix/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/minimum_passes_of_matrix/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/minimum_passes_of_matrix/cpp) |
| 2   | [Youngest Common Ancestor](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/youngest_common_ancestor) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/youngest_common_ancestor/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/youngest_common_ancestor/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/youngest_common_ancestor/cpp) |
| 3   | [Cycle In Graph](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/cycle_in_graph) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/cycle_in_graph/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/cycle_in_graph/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/cycle_in_graph/cpp) |
| 4   | [Boggle Board](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/boggle_board) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/boggle_board/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/boggle_board/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/boggle_board/cpp) |
| 5   | [Airport Connections](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/airport_connections/cpp) |
| 6   | [Detect Arbitrage](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/detect_arbitrage) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/detect_arbitrage/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/detect_arbitrage/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/graphs/detect_arbitrage/cpp) |

### Greedy algorithms Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Optimal Freelancing](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/optimal_freelancing) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/optimal_freelancing/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/optimal_freelancing/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/optimal_freelancing/cpp) |
| 2   | [Tandem Bicycle](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/tandem_bicycle) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/tandem_bicycle/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/tandem_bicycle/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/tandem_bicycle/cpp) |
| 3   | [Class Photos](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/class_photos) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/class_photos/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/class_photos/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/class_photos/cpp) |
| 4   | [Minimum Waiting Time](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/minimum_waiting_time) | <p align='center'>🟢</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/minimum_waiting_time/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/minimum_waiting_time/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/minimum_waiting_time/cpp) |
| 5   | [Task Assignment](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/task_assignment) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/task_assignment/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/task_assignment/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/task_assignment/cpp) |
| 6   | [Valid Starting City](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/valid_starting_city) | <p align='center'>🟡</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/valid_starting_city/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/valid_starting_city/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/greedy_algorithms/valid_starting_city/cpp) |

### Dynamic programming Problems
| #   | Problem               | Difficulty | Languages               |
|-----|-----------------------|------------|-------------------------|
| 1   | [Maximum Sum Submatrix](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/maximum_sum_submatrix) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/maximum_sum_submatrix/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/maximum_sum_submatrix/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/maximum_sum_submatrix/cpp) |
| 2   | [Knapsack Problem](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/knapsack_problem) | <p align='center'>🔴</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/knapsack_problem/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/knapsack_problem/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/knapsack_problem/cpp) |
| 3   | [Max Profit With K Transactions](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/max_profit_with_k_transactions) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/max_profit_with_k_transactions/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/max_profit_with_k_transactions/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/max_profit_with_k_transactions/cpp) |
| 4   | [Longest Increasing Subsequence](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/longest_increasing_subsequence) | <p align='center'>⚫</p> | [Js](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/longest_increasing_subsequence/js), [Python](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/longest_increasing_subsequence/python), [Cpp](https://github.com/dmaman86/algo-solutions/tree/main/problems/dynamic_programming/longest_increasing_subsequence/cpp) |


<!-- END_TABLE -->

## **Quick Start**

📌 **Clone the repository**:

```sh
git clone https://github.com/dmaman86/algo-solutions.git && cd algo-solutions
```

🔹 **Install dependencies**:

```sh
make setup
```

🧪 **Run all tests**:

```sh
make test
```

---

## **How To Use This Project (Workflow)**

### 1. **Set Up the Environment**:

Run the following command based on your operating system:

```sh
make setup
```

#### **What does `make setup` do?**:

- Installs **Python** dependencies from `requirements.txt` (`make install-python`) into:
  - the active virtualenv or Conda environment (e.g. `conda activate algo-solutions`), or
  - a local `./venv`, created with Python 3.12 (`python3.12` must be on `PATH`) when no environment is active.

  Active environments must use Python 3.11 or 3.12. The Conda `base` environment is refused on purpose.
- Installs **JavaScript** dependencies exactly as locked in `package-lock.json` (`make install-js`, which runs `npm ci`).
- Installs **Google Test (gtest)** and **nlohmann/json** depending your operating system:
  - **macOS**: Uses `brew`.
  - **Linux**: Uses `apt-get`.
  - **Windows**: Uses `vcpkg`.

`make test-python` and `make visualize` never install packages: run `make install-python` (or `make setup`) first, and again after `requirements.txt` changes (see [Manage Python dependencies](#6-manage-python-dependencies)). `make test-js` reinstalls npm dependencies only when `package.json` or `package-lock.json` change. To add or update a JavaScript dependency, use `npm install <package>` (which updates `package-lock.json`) and commit both files.

### 2. **Run Tests**:

You can run tests for each language individually or all at once.

- **Run all tests (JavaScript, Python and C++)**:

  ```sh
  make test
  ```

- **Run JavaScript tests only**:

  ```sh
  make test-js
  ```

- **Run Python tests only**:

  ```sh
  make test-python
  ```

- **Run C++ tests only**:

  ```sh
  make test-cpp
  ```

### 3. **Run Tests with Visualizations (Python only)**:

Some Python tests may generate **graphs** or **visual outputs**. To enable them, use:

```sh
make visualize
```

Visualizations require the **Graphviz** `dot` executable (regular test runs, including CI, do not):

```sh
brew install graphviz                                   # macOS
sudo apt-get install graphviz                           # Linux
conda install -n algo-solutions -c conda-forge graphviz # Conda
```

### 4. **Clean the project**:

To remove compiled files and Python cache (`__pycache__`), use:

```sh
make clean
```

This will delete:

- Build files (`build/`).
- Python cache files (`__pycache__`).

### 5. **Help**:

To view all available Makefile rules, use:

```sh
make help
```

This will display:

```sh
make setup          # Install all dependencies (Python, JavaScript, C++)
make install-python # Install Python dependencies from requirements.txt (creates ./venv with Python 3.12 if no env is active)
make install-js     # Clean install of npm dependencies from package-lock.json
make compile-requirements [P="pkg ..."] # Regenerate requirements.txt from requirements.in (P upgrades the listed packages)
make upgrade-requirements # Upgrade all pins within the ranges in requirements.in
make check-requirements   # Verify requirements.txt matches requirements.in (modifies nothing)
make test           # Run all tests, without visualizations
make test-js        # Run JavaScript tests with npm
make test-python    # Run Python tests with pytest
make test-cpp       # Run C++ tests with CMake
make visualize      # Run Python tests and generate visualizations (requires Graphviz)
make clean          # Clean temporary files
```

### 6. **Manage Python dependencies**:

- `requirements.in` lists the **direct** dependencies with compatible version ranges. This is the file you edit.
- `requirements.txt` is **generated** from it by [pip-tools](https://pip-tools.readthedocs.io/) (`pip-compile`) and pins every direct and transitive package. Commit it together with `requirements.in`; CI and `make install-python` install from it.

pip-tools is a maintenance tool, not a project dependency: the targets below install it into a separate `./.venv-tools` (Python 3.12, git-ignored) and never touch your project environment. Installing and running tests never regenerate or upgrade dependencies.

```sh
# Add or change a direct dependency: edit requirements.in, then
make compile-requirements             # existing pins are kept

# Upgrade specific packages (also list dependencies that must move with them)
make compile-requirements P="pytest pluggy"

# Upgrade everything within the ranges of requirements.in (review the diff: transitive majors can appear)
make upgrade-requirements

# Install the resolved versions into the selected environment
make install-python

# Verify requirements.txt is up to date with requirements.in
make check-requirements
```

Pins are resolved with Python 3.12 on macOS/Linux. Packages that are only needed on other platforms (e.g. `colorama` for pytest on Windows) are not pinned, and pip installs them when required.

---

## **Project Structure**

This repository is structured as follows:

- **problems/** → Algorithmic challenges, organized by category.
- **tests/** → Unit tests for JavaScript, C++, and Python solutions.
- **scripts/** → Utility scripts (e.g., updating the README).
- **test_cases/** → JSON-based test cases for automated validation.
- **makefile** → Automates testing, visualization, and cleanup tasks.

### **Folder Breakdown**:

```plaintext
.
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions: runs JS/Python/C++ tests on push and PR
├── CMakeLists.txt                  # Main configuration file for C++ tests
├── README.md                       # Project documentation and usage instructions
├── babel.config.json               # Babel configuration for JavaScript tests
├── jest.config.cjs                 # Jest configuration file for JavaScript tests
├── makefile                        # Automates common tasks (e.g., testing, visualization)
├── metadata.json                   # Metadata about problems and their solutions
├── package-lock.json               # Dependency lock file for npm
├── package.json                    # Node.js project configuration file
├── requirements.in                 # Direct Python dependencies (edit this file)
├── requirements.txt                # Pinned Python dependencies, generated by pip-compile
├── problems/                       # Solutions to problems, organized by topic
│   ├── arrays/                     # Array-related problems
│   ├── binary_search_trees/        # Binary search tree problems
|   ├── binary_trees/               # Binary tree problems
│   ├── famous_algorithms/          # Well-known algorithms
│   ├── greedy_algorithms/          # Greedy algorithm problems
│   ├── dynamic_programming/        # Dynamic programming problems
│   └── graphs/                     # Graph-related problems
├── scripts/                        # Utility scripts for project maintenance
│   └── update_readme.py            # Updates README with metadata or problem table
└── tests/                          # Contains all test-related files
    ├── __tests__/                  # JavaScript tests (run with Jest)
    │   ├── arrays/                 # Array-related JavaScript tests
    │   ├── binary_search_trees/    # Binary search tree JavaScript tests
    │   ├── binary_trees/           # Binary tree JavaScript tests
    │   ├── famous_algorithms/      # Well-known algorithm JavaScript tests
    |   ├── greedy_algorithms/      # Greedy algorithm JavaScript tests
    |   ├── dynamic_programming/    # Dynamic programming JavaScript tests
    │   └── graphs/                 # Graph-related JavaScript tests
    ├── cpp/                        # C++ tests (run with CMake and CTest)
    │   ├── CMakeLists.txt          # Main configuration for all C++ tests
    │   ├── arrays/                 # C++ tests for array problems
    │   │   ├── CMakeLists.txt      # Configuration for array-specific tests
    │   ├── binary_search_trees/    # C++ tests for binary search tree problems
    │   │   ├── CMakeLists.txt      # Configuration for binary search tree tests
    |   ├── binary_trees/           # C++ tests for binary tree problems
    │   │   ├── CMakeLists.txt      # Configuration for binary tree tests
    │   ├── famous_algorithms/      # C++ tests for well-known algorithms
    │   │   ├── CMakeLists.txt      # Configuration for famous algorithms tests
    │   ├── dynamic_programming/    # C++ tests for dynamic programming problems
    │   │   ├── CMakeLists.txt      # Configuration for dynamic programming tests
    |   ├── greedy_algorithms/      # C++ tests for greedy algorithm problems
    │   │   ├── CMakeLists.txt      # Configuration for greedy algorithm tests
    │   ├── graphs/                 # C++ tests for graph problems
    │   │   ├── CMakeLists.txt      # Configuration for graph-specific tests
    │   └── jsontestbase.h          # Header for handling JSON-based test cases in C++
    ├── python/                     # Python tests (run with pytest)
    │   ├── arrays/                 # Python tests for array problems
    │   ├── binary_search_trees/    # Python tests for binary search tree problems
    │   ├── binary_trees/           # Python tests for binary tree problems
    │   ├── conftest.py             # Configuration for pytest
    │   ├── famous_algorithms/      # Python tests for well-known algorithms
    │   ├── graphs/                 # Python tests for graph problems
    │   ├── greedy_algorithms/      # Python tests for greedy algorithm problems
    │   ├── dynamic_programming/    # Python tests for dynamic programming problems
    │   └── utility.py              # Helper functions for Python tests
    └── test_cases/                 # JSON test cases for all problems
        ├── arrays/                 # Test cases for array problems
        ├── binary_search_trees/    # Test cases for binary search tree problems
        ├── binary_trees/           # Test cases for binary tree problems
        ├── famous_algorithms/      # Test cases for well-known algorithms
        |── greedy_algorithms/      # Test cases for greedy algorithm problems
        ├── dynamic_programming/    # Test cases for dynamic programming problems
        └── graphs/                 # Test cases for graph problems
```

---

## **Notes**:

- If you're on **Windows**, ensure you have **vcpkg** installed.
- CI runs **Python 3.12**; locally use Python 3.12 (3.11 is also supported).
  ```bash
  python3 --version
  ```
- You can modify or add more tests in the following directories:
  - **JavaScript**: `tests/__tests__`
  - **Python**: `tests/python`
  - **C++**: `tests/cpp`
  - **Test Cases**: `tests/test_cases`
