# Lists in Python
# Ordered, mutable collections of items

# ==========================================
# 1. Creating Lists
# ==========================================

print("=== Creating Lists ===")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")

# List with mixed data types
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed list: {mixed_list}")

# List using list() constructor
numbers = list(range(1, 6))
print(f"Numbers: {numbers}")

# ==========================================
# 2. Accessing List Elements
# ==========================================

print("\n=== Accessing List Elements ===")

colors = ["red", "green", "blue", "yellow", "purple"]

# Access by index (0-based)
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Last color: {colors[-1]}")
print(f"Second to last: {colors[-2]}")

# Slicing
print(f"First 3 colors: {colors[0:3]}")
print(f"Colors from index 1 to end: {colors[1:]}")
print(f"Colors from start to index 3: {colors[:3]}")
print(f"Every other color: {colors[::2]}")
print(f"Reverse the list: {colors[::-1]}")

# ==========================================
# 3. Modifying Lists
# ==========================================

print("\n=== Modifying Lists ===")

# Lists are mutable - you can change them
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Change an element
numbers[2] = 10
print(f"After changing index 2: {numbers}")

# Change a slice
numbers[1:3] = [20, 30]
print(f"After changing slice: {numbers}")

# ==========================================
# 4. Adding Elements
# ==========================================

print("\n=== Adding Elements ===")

animals = ["dog", "cat"]
print(f"Original: {animals}")

# append() - add to the end
animals.append("bird")
print(f"After append: {animals}")

# insert() - add at specific position
animals.insert(1, "fish")
print(f"After insert: {animals}")

# extend() - add multiple items
animals.extend(["hamster", "rabbit"])
print(f"After extend: {animals}")

# + operator - concatenate lists
more_animals = ["elephant", "giraffe"]
all_animals = animals + more_animals
print(f"After concatenation: {all_animals}")

# ==========================================
# 5. Removing Elements
# ==========================================

print("\n=== Removing Elements ===")

items = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"Original: {items}")

# remove() - remove by value
items.remove("banana")
print(f"After remove('banana'): {items}")

# pop() - remove by index and return value
removed_item = items.pop(1)
print(f"Removed item: {removed_item}")
print(f"After pop(1): {items}")

# pop() without index - removes last item
last_item = items.pop()
print(f"Removed last item: {last_item}")
print(f"After pop(): {items}")

# del statement
del items[0]
print(f"After del items[0]: {items}")

# Clear all items
items.clear()
print(f"After clear(): {items}")

# ==========================================
# 6. List Methods
# ==========================================

print("\n=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# sort() - sort in place
numbers.sort()
print(f"After sort(): {numbers}")

# reverse() - reverse in place
numbers.reverse()
print(f"After reverse(): {numbers}")

# count() - count occurrences
count_1 = numbers.count(1)
print(f"Count of 1: {count_1}")

# index() - find index of value
try:
    index_5 = numbers.index(5)
    print(f"Index of 5: {index_5}")
except ValueError:
    print("5 not found in list")

# ==========================================
# 7. List Operations
# ==========================================

print("\n=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Combined: {combined}")

# Repetition
repeated = list1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"Is 2 in list1? {2 in list1}")
print(f"Is 7 in list1? {7 in list1}")

# Length
print(f"Length of list1: {len(list1)}")

# ==========================================
# 8. List Comprehensions
# ==========================================

print("\n=== List Comprehensions ===")

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comp}")

# With condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension
matrix = [[i + j for j in range(3)] for i in range(0, 9, 3)]
print(f"Matrix: {matrix}")

# ==========================================
# 9. Copying Lists
# ==========================================

print("\n=== Copying Lists ===")

original = [1, 2, [3, 4]]
print(f"Original: {original}")

# Shallow copy
shallow_copy = original.copy()
print(f"Shallow copy: {shallow_copy}")

# Deep copy (for nested structures)
import copy
deep_copy = copy.deepcopy(original)
print(f"Deep copy: {deep_copy}")

# Modify nested list to see difference
original[2][0] = 99
print(f"After modifying nested list:")
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")

# ==========================================
# 10. Practical Examples
# ==========================================

print("\n=== Practical Examples ===")

# Example 1: Student grades
grades = [85, 92, 78, 96, 88, 91, 75]
print(f"Grades: {grades}")
print(f"Average: {sum(grades) / len(grades):.2f}")
print(f"Highest: {max(grades)}")
print(f"Lowest: {min(grades)}")

# Example 2: Shopping list
shopping_list = ["milk", "bread", "eggs", "butter"]
print(f"Shopping list: {shopping_list}")

# Add items
shopping_list.append("cheese")
shopping_list.insert(1, "yogurt")
print(f"Updated list: {shopping_list}")

# Remove purchased items
shopping_list.remove("milk")
shopping_list.remove("bread")
print(f"After shopping: {shopping_list}")

# Example 3: Temperature tracking
temperatures = [22, 24, 19, 25, 23, 21, 26]
print(f"Temperatures: {temperatures}")

# Find days above average
avg_temp = sum(temperatures) / len(temperatures)
hot_days = [temp for temp in temperatures if temp > avg_temp]
print(f"Days above average ({avg_temp:.1f}°C): {hot_days}")

# ==========================================
# 11. Common List Patterns
# ==========================================

print("\n=== Common List Patterns ===")

# Pattern 1: Building a list incrementally
fibonacci = [0, 1]
for i in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(f"Fibonacci: {fibonacci}")

# Pattern 2: Filtering a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Pattern 3: Transforming a list
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(f"Capitalized: {capitalized}")

# Pattern 4: Zipping lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(f"People: {people}")

# ==========================================
# 12. List Performance Tips
# ==========================================

print("\n=== Performance Tips ===")

# ✅ Use append() for adding single items
# ✅ Use extend() for adding multiple items
# ✅ Use list comprehensions for transformations
# ✅ Avoid modifying list while iterating
# ✅ Use in operator for membership testing

# Example of efficient list building
efficient_list = []
for i in range(1000):
    efficient_list.append(i)

# Less efficient (creates new list each time)
# inefficient_list = []
# for i in range(1000):
#     inefficient_list = inefficient_list + [i]

print(f"Efficient list length: {len(efficient_list)}")

# ==========================================
# 13. Common Mistakes to Avoid
# ==========================================

print("\n=== Common Mistakes ===")

# ❌ Mistake 1: Modifying list while iterating
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # This can cause issues

# ✅ Solution: Create a copy or use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(f"After removing evens: {numbers}")

# ❌ Mistake 2: Using = for copying
list1 = [1, 2, 3]
list2 = list1  # This creates a reference, not a copy
list2[0] = 99
print(f"list1: {list1}")  # list1 is also changed!

# ✅ Solution: Use .copy() or list()
list1 = [1, 2, 3]
list2 = list1.copy()  # This creates a copy
list2[0] = 99
print(f"list1: {list1}")  # list1 is unchanged
print(f"list2: {list2}")

# ==========================================
# 14. Advanced List Features
# ==========================================

print("\n=== Advanced Features ===")

# Unpacking lists
first, second, *rest = [1, 2, 3, 4, 5]
print(f"First: {first}, Second: {second}, Rest: {rest}")

# List as stack (LIFO)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")
popped = stack.pop()  # pop
print(f"Popped: {popped}, Stack: {stack}")

# List as queue (FIFO)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)  # enqueue
print(f"Queue: {queue}")
first_item = queue.popleft()  # dequeue
print(f"Dequeued: {first_item}, Queue: {queue}")

print("\n=== End of Lists ===")
print("You've mastered the most versatile data structure in Python! 📋") 