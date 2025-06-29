# For Loops in Python
# Iterating over sequences and collections

# ==========================================
# 1. Basic For Loop with Range
# ==========================================

print("=== Basic For Loop with Range ===")
for i in range(5):
    print(f"Count: {i}")

# ==========================================
# 2. For Loop with Start, Stop, Step
# ==========================================

print("\n=== For Loop with Range Parameters ===")
# range(start, stop, step)
for i in range(1, 11, 2):  # Start at 1, stop before 11, step by 2
    print(f"Odd number: {i}")

# Countdown
print("\nCountdown:")
for i in range(10, 0, -1):
    print(f"{i}...")
print("Blast off!")

# ==========================================
# 3. For Loop with Lists
# ==========================================

print("\n=== For Loop with Lists ===")
fruits = ["apple", "banana", "orange", "grape"]

# Iterate over list items
for fruit in fruits:
    print(f"I like {fruit}")

# Iterate with index
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# ==========================================
# 4. For Loop with Strings
# ==========================================

print("\n=== For Loop with Strings ===")
word = "Python"

# Iterate over characters
for char in word:
    print(f"Character: {char}")

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in '{word}': {vowel_count}")

# ==========================================
# 5. For Loop with Dictionaries
# ==========================================

print("\n=== For Loop with Dictionaries ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Developer"
}

# Iterate over keys
print("Keys:")
for key in person:
    print(f"Key: {key}")

# Iterate over keys and values
print("\nKeys and Values:")
for key, value in person.items():
    print(f"{key}: {value}")

# Iterate over values only
print("\nValues:")
for value in person.values():
    print(f"Value: {value}")

# ==========================================
# 6. For Loop with Tuples
# ==========================================

print("\n=== For Loop with Tuples ===")
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]

for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# ==========================================
# 7. Nested For Loops
# ==========================================

print("\n=== Nested For Loops ===")
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row

# ==========================================
# 8. List Comprehensions (Advanced)
# ==========================================

print("=== List Comprehensions ===")
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

# ==========================================
# 9. Practical Examples
# ==========================================

print("\n=== Practical Examples ===")

# Example 1: Calculate average
grades = [85, 92, 78, 96, 88]
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print(f"Grades: {grades}")
print(f"Average: {average:.2f}")

# Example 2: Find maximum value
numbers = [23, 45, 12, 67, 34, 89, 56]
max_num = numbers[0]  # Start with first number
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Numbers: {numbers}")
print(f"Maximum: {max_num}")

# Example 3: Filter even numbers
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in all_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"All numbers: {all_numbers}")
print(f"Even numbers: {even_numbers}")

# ==========================================
# 10. For Loop with Sets
# ==========================================

print("\n=== For Loop with Sets ===")
colors = {"red", "green", "blue", "yellow", "red"}  # Note: duplicates are removed
print(f"Colors set: {colors}")

for color in colors:
    print(f"Color: {color}")

# ==========================================
# 11. For Loop with enumerate()
# ==========================================

print("\n=== For Loop with enumerate() ===")
students = ["Alice", "Bob", "Charlie", "Diana"]

# enumerate() provides both index and value
for index, student in enumerate(students):
    print(f"Student {index + 1}: {student}")

# Start enumeration from a different number
for index, student in enumerate(students, start=1001):
    print(f"ID {index}: {student}")

# ==========================================
# 12. For Loop with zip()
# ==========================================

print("\n=== For Loop with zip() ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# zip() combines multiple lists
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# ==========================================
# 13. Break and Continue in For Loops
# ==========================================

print("\n=== Break and Continue ===")

# Using break
print("Using break:")
for i in range(1, 11):
    if i == 6:
        break  # Exit the loop when i equals 6
    print(f"Number: {i}")

# Using continue
print("\nUsing continue:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# ==========================================
# 14. For Loop Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Use descriptive variable names
for student_name in students:
    print(f"Hello, {student_name}!")

# ✅ Use _ for unused variables
for _ in range(3):
    print("Processing...")

# ✅ Use list comprehensions for simple operations
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"Doubled numbers: {doubled}")

# ✅ Avoid modifying the list while iterating
# ❌ Don't do this:
# for item in my_list:
#     my_list.remove(item)

# ✅ Instead, create a copy or use a different approach
my_list = [1, 2, 3, 4, 5]
for item in my_list[:]:  # Create a slice copy
    if item % 2 == 0:
        my_list.remove(item)
print(f"List after removing evens: {my_list}")

# ==========================================
# 15. Interactive Example
# ==========================================

print("\n=== Interactive Example ===")
print("Let's create a simple shopping list!")

# You can uncomment this to make it interactive
# shopping_list = []
# print("Enter items for your shopping list (type 'done' when finished):")
# 
# while True:
#     item = input("Add item: ")
#     if item.lower() == 'done':
#         break
#     shopping_list.append(item)
# 
# print("\nYour shopping list:")
# for i, item in enumerate(shopping_list, 1):
#     print(f"{i}. {item}")

print("Shopping list example completed!")

print("\n=== End of For Loops ===")
print("You've mastered the art of iteration in Python! 🔄") 