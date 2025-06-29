# Variables and Data Types in Python
# Variables are containers that store data

# ==========================================
# 1. Creating Variables
# ==========================================

# String variable (text)
name = "Alice"
age = 25
height = 5.6
is_student = True

print("=== Variable Examples ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# ==========================================
# 2. Variable Naming Rules
# ==========================================

# ✅ Good variable names
first_name = "John"
last_name = "Doe"
user_age = 30
is_active = True

# ❌ Bad variable names (don't do this)
# 1name = "John"  # Can't start with number
# my-name = "John"  # Can't use hyphens
# class = "Python"  # Can't use reserved words

print("\n=== Variable Naming ===")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"User Age: {user_age}")
print(f"Is Active: {is_active}")

# ==========================================
# 3. Multiple Assignment
# ==========================================

# Assign multiple variables at once
x, y, z = 1, 2, 3
print(f"\n=== Multiple Assignment ===")
print(f"x = {x}, y = {y}, z = {z}")

# Assign same value to multiple variables
a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

# ==========================================
# 4. Checking Data Types
# ==========================================

print(f"\n=== Data Types ===")
print(f"name ({name}) is type: {type(name)}")
print(f"age ({age}) is type: {type(age)}")
print(f"height ({height}) is type: {type(height)}")
print(f"is_student ({is_student}) is type: {type(is_student)}")

# ==========================================
# 5. Variable Reassignment
# ==========================================

print(f"\n=== Variable Reassignment ===")
score = 85
print(f"Original score: {score}")

score = 92  # Reassigning the variable
print(f"Updated score: {score}")

# ==========================================
# 6. Constants (by convention)
# ==========================================

# In Python, we use UPPERCASE for constants
PI = 3.14159
MAX_CONNECTIONS = 100
API_KEY = "abc123"

print(f"\n=== Constants ===")
print(f"PI: {PI}")
print(f"Max Connections: {MAX_CONNECTIONS}")
print(f"API Key: {API_KEY}")

# ==========================================
# 7. Deleting Variables
# ==========================================

temp_variable = "I'm temporary"
print(f"\n=== Before deletion: {temp_variable}")

del temp_variable
# print(temp_variable)  # This would cause an error

print("Variable deleted successfully!")

# ==========================================
# 8. Interactive Example
# ==========================================

print(f"\n=== Interactive Example ===")
print("Let's create some variables together!")

# You can modify these values
favorite_color = "blue"
favorite_number = 7
favorite_food = "pizza"

print(f"My favorite color is {favorite_color}")
print(f"My favorite number is {favorite_number}")
print(f"My favorite food is {favorite_food}")

# Try changing the values above and run the program again! 