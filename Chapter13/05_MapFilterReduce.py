# `map()`, `filter()` and `reduce()` in Python
# These are built-in functional programming tools used to work with lists and iterables.

# 1. `map()` Function
## Theory
# `map()` is used to apply a function to every element of an iterable (like a list).
# It transforms the data.

## Syntax
# map(function, iterable)
# * `function` → operation to apply
# * `iterable` → list/tuple etc.

## Example
numbers = [1, 2, 3, 4]
square = list(map(lambda x: x*x, numbers))
print(square)

# [1, 4, 9, 16]
# Explanation:
# * Each number is squared
# * `map()` applies lambda function to every element

# 2. `filter()` Function
## Theory
# `filter()` is used to select elements from an iterable based on a condition.
# It keeps only `True` values.
## Syntax
# filter(function, iterable)
# * Function must return `True` or `False`
## Example
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# [2, 4, 6]

# Explanation:
# * Keeps only even numbers
# * Removes odd numbers

# 3. `reduce()` Function

## Theory
# `reduce()` is used to reduce all elements of an iterable into a single value.
# It performs cumulative operations.
# `reduce()` is present in the `functools` module.
## Syntax
# reduce(function, iterable)
## Example
from functools import reduce
numbers = [1, 2, 3, 4]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

# 10
# Explanation:
# Process:
# * `1 + 2 = 3`
# * `3 + 3 = 6`
# * `6 + 4 = 10`
# Final result = `10`

# Difference Between `map()`, `filter()`, and `reduce()`
# | Function   | Purpose                             | Returns           |
# | ---------- | ----------------------------------- | ----------------- |
# | `map()`    | Transform elements                  | Modified iterable |
# | `filter()` | Select elements based on condition  | Filtered iterable |
# | `reduce()` | Combine all elements into one value | Single value      |

# * `map()` → Modify every item
# * `filter()` → Keep selected items
# * `reduce()` → Combine everything into one result
