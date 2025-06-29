# Conditional Statements in Python
# Making decisions in your code

# ==========================================
# 1. Basic if Statement
# ==========================================

print("=== Basic if Statement ===")
age = 18

if age >= 18:
    print("You are an adult!")
    print("You can vote and drive.")

# ==========================================
# 2. if-else Statement
# ==========================================

print("\n=== if-else Statement ===")
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# ==========================================
# 3. if-elif-else Statement
# ==========================================

print("\n=== if-elif-else Statement ===")
score = 85

if score >= 90:
    grade = "A"
    print(f"Excellent! Your grade is {grade}")
elif score >= 80:
    grade = "B"
    print(f"Good job! Your grade is {grade}")
elif score >= 70:
    grade = "C"
    print(f"Not bad! Your grade is {grade}")
elif score >= 60:
    grade = "D"
    print(f"You passed with a {grade}")
else:
    grade = "F"
    print(f"You failed with a {grade}")

# ==========================================
# 4. Nested if Statements
# ==========================================

print("\n=== Nested if Statements ===")
is_weekend = True
is_sunny = True

if is_weekend:
    if is_sunny:
        print("Perfect! Let's go to the beach!")
    else:
        print("It's weekend but not sunny. Let's watch a movie.")
else:
    if is_sunny:
        print("It's a sunny weekday. Work time!")
    else:
        print("It's a cloudy weekday. Focus on work.")

# ==========================================
# 5. Multiple Conditions
# ==========================================

print("\n=== Multiple Conditions ===")
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid username or password.")

# ==========================================
# 6. Using 'in' Operator
# ==========================================

print("\n=== Using 'in' Operator ===")
favorite_colors = ["blue", "green", "red"]
user_color = "blue"

if user_color in favorite_colors:
    print(f"{user_color} is one of my favorite colors!")
else:
    print(f"{user_color} is not in my favorite colors.")

# ==========================================
# 7. Conditional Expressions (Ternary Operator)
# ==========================================

print("\n=== Conditional Expressions ===")
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Another example
number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}")

# ==========================================
# 8. Checking for None
# ==========================================

print("\n=== Checking for None ===")
user_input = None

if user_input is None:
    print("No input provided")
else:
    print(f"Input received: {user_input}")

# ==========================================
# 9. Practical Example: Grade Calculator
# ==========================================

print("\n=== Grade Calculator Example ===")
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
test_scores = [95, 87, 73, 55, 105, -5]

for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score: {score} → Grade: {grade}")

# ==========================================
# 10. Interactive Example
# ==========================================

print("\n=== Interactive Example ===")
print("Let's play a simple game!")

# You can uncomment this section to make it interactive
# user_age = int(input("Enter your age: "))
# 
# if user_age < 13:
#     print("You're a child!")
# elif user_age < 20:
#     print("You're a teenager!")
# elif user_age < 65:
#     print("You're an adult!")
# else:
#     print("You're a senior!")

print("Game completed!")

# ==========================================
# 11. Common Mistakes to Avoid
# ==========================================

print("\n=== Common Mistakes ===")

# ❌ Wrong: Using = instead of ==
# if x = 5:  # This will cause an error

# ✅ Correct: Using == for comparison
x = 5
if x == 5:
    print("x equals 5")

# ❌ Wrong: Forgetting colon
# if x > 0
#     print("Positive")  # This will cause an error

# ✅ Correct: Including colon
if x > 0:
    print("x is positive")

# ==========================================
# 12. Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Use meaningful variable names
user_is_logged_in = True
user_has_permission = True

if user_is_logged_in and user_has_permission:
    print("Access granted")

# ✅ Keep conditions simple
# Instead of complex nested conditions, use early returns
def check_access(user):
    if not user.is_logged_in:
        return False
    if not user.has_permission:
        return False
    if user.is_blocked:
        return False
    return True

# ✅ Use parentheses for complex conditions
a, b, c = 1, 2, 3
if (a > 0 and b > 0) or c > 0:
    print("At least one condition is true")

print("\n=== End of Conditional Statements ===")
print("You've learned the basics of making decisions in Python!") 