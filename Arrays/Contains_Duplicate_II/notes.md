# Notes

## Brute Force

Time Complexity: O(n²)

Used nested loops to compare every pair.

---

## Optimized

Time Complexity: O(n)

Used a dictionary called last_seen.

Dictionary stores:

number -> latest index

Example:

1 -> 0

2 -> 1

3 -> 2

Whenever a duplicate is found, calculate

current index - previous index

If it is <= k

Return True.

Otherwise update the index.

---

## Concepts Learned

- HashMap
- Dictionary
- Last Seen Pattern
- Time Complexity Optimization
