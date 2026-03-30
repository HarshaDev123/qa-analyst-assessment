"""
Part 1: Functional Programming - Remove Duplicates

Approach:
    Uses Python's functools.reduce to iterate through the list and accumulate
    unique elements while preserving the original order of first occurrences.
    This is a pure function — it does not modify the input and produces the
    same output for the same input every time, with no side effects.
"""

from functools import reduce


def remove_duplicates(items: list) -> list:
    """
    Remove duplicate values from a list while preserving the order of
    first occurrences.

    This is a pure function:
      - Same input always produces the same output.
      - The original list is never modified.
      - No external state is read or changed.

    Args:
        items: A list that may contain duplicate values.

    Returns:
        A new list with duplicates removed, preserving original order.
    """
    if not items:
        return []

    # Use filter with a closure to track seen elements immutably per call.
    seen = set()

    def is_first_occurrence(item):
        if item in seen:
            return False
        seen.add(item)
        return True

    return list(filter(is_first_occurrence, items))


# ---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

def run_tests():
    """Run all test cases and report results."""

    test_cases = [
        # (input, expected output, description)
        ([1, 2, 3, 2, 4, 1, 5], [1, 2, 3, 4, 5], "Mixed duplicates"),
        ([1, 1, 1],             [1],               "All identical elements"),
        ([],                    [],                 "Empty list"),
        ([5, 4, 3, 2, 1],      [5, 4, 3, 2, 1],   "No duplicates"),
        ([1],                   [1],                "Single element"),
        (["a", "b", "a", "c"], ["a", "b", "c"],    "String elements"),
        ([1, "1", 1, "1"],     [1, "1"],            "Mixed types"),
    ]

    print("Running tests...\n")
    all_passed = True

    for i, (input_data, expected, description) in enumerate(test_cases, 1):
        # Work on a copy so we can verify the original is unchanged
        original_copy = list(input_data)
        result = remove_duplicates(input_data)

        passed = result == expected and input_data == original_copy
        status = "PASS" if passed else "FAIL"

        if not passed:
            all_passed = False

        print(f"  Test {i} [{status}]: {description}")
        if not passed:
            print(f"           Input:    {input_data}")
            print(f"           Expected: {expected}")
            print(f"           Got:      {result}")

    print(f"\n{'All tests passed!' if all_passed else 'Some tests failed.'}")


if __name__ == "__main__":
    run_tests()
