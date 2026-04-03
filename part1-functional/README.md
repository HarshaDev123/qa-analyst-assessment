# Part 1: Functional Programming — Remove Duplicates

## Approach

The solution uses Python's built-in `filter()` to iterate through the input list and keep only the first occurrence of each element. A `set` tracks which values have already been seen, ensuring **O(n)** time complexity.

### Functional Programming Principles Applied

- **Pure Function** — `remove_duplicates` always returns the same output for the same input and produces no side effects.
- **Immutability** — The original input list is never modified; a new list is returned.
- **Higher-Order Functions** — Uses `filter()` to declaratively select elements.

## How to Run

No external dependencies required — uses only the Python standard library.

python remove_duplicates.py

## Expected Output

Running tests...

  Test 1 [PASS]: Mixed duplicates
  Test 2 [PASS]: All identical elements
  Test 3 [PASS]: Empty list
  Test 4 [PASS]: No duplicates
  Test 5 [PASS]: Single element
  Test 6 [PASS]: String elements
  Test 7 [PASS]: Mixed types

All tests passed!
