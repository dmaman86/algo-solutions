from bisect import bisect_left


def longestIncreasingSubsequence(array: list[int]) -> list[int]:
    def build_lis(array: list[int]) -> tuple[int, list[int]]:
        lis_values = []  # tracks active LIS values
        indices = []  # tracks indices of LIS elements
        predecessors = [-1] * len(array)  # tracks LIS predecessor

        for i, num in enumerate(array):
            # find position to insert/replace using binary search
            pos = bisect_left(lis_values, num)
            if pos == len(lis_values):
                # extend LIS
                if indices:
                    predecessors[i] = indices[-1]
                indices.append(i)
                lis_values.append(num)
            else:
                # replace element in LIS
                if pos:
                    predecessors[i] = indices[pos - 1]
                indices[pos] = i
                lis_values[pos] = num

        return indices[-1], predecessors

    if not array:
        return []

    last_index, predecessors = build_lis(array)
    result = []
    current = last_index
    while current != -1:
        result.append(array[current])
        current = predecessors[current]

    return result[::-1]  # reverse to get the correct order
