from questions.minimum_sorted_subarray import length_smallest_subarray

def test_shortest_window_sort():
    assert length_smallest_subarray([1, 2, 5, 3, 7, 10, 9, 12]) == 5, "Test 1 failed"
    assert length_smallest_subarray([1, 3, 2, 0, -1, 7, 10]) == 5, "Test 2 failed"
    assert length_smallest_subarray([1, 2, 3]) == 0, "Test 3 failed"
    assert length_smallest_subarray([3, 2, 1]) == 3, "Test 4 failed"
