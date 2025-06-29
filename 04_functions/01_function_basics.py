# Function Basics in Python
# Defining and calling functions

# ==========================================
# 1. Basic Function Definition
# ==========================================

print("=== Basic Function Definition ===")

def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")

# Calling the function
greet()

# ==========================================
# 2. Function with Parameters
# ==========================================

print("\n=== Function with Parameters ===")

def greet_person(name):
    """Function that greets a specific person"""
    print(f"Hello, {name}!")

# Calling with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# ==========================================
# 3. Function with Multiple Parameters
# ==========================================

print("\n=== Function with Multiple Parameters ===")

def introduce(name, age, city):
    """Function that introduces a person"""
    print(f"Hi, I'm {name}. I'm {age} years old and I live in {city}.")

# Calling with positional arguments
introduce("Alice", 25, "New York")

# Calling with keyword arguments
introduce(age=30, city="Los Angeles", name="Bob")

# ==========================================
# 4. Function with Return Value
# ==========================================

print("\n=== Function with Return Value ===")

def add_numbers(a, b):
    """Function that adds two numbers and returns the result"""
    result = a + b
    return result

# Using the return value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Direct use in expressions
print(f"10 + 20 = {add_numbers(10, 20)}")

# ==========================================
# 5. Function with Multiple Return Values
# ==========================================

print("\n=== Function with Multiple Return Values ===")

def get_name_and_age():
    """Function that returns multiple values"""
    name = "Alice"
    age = 25
    return name, age

# Unpacking multiple return values
person_name, person_age = get_name_and_age()
print(f"Name: {person_name}, Age: {person_age}")

# Another example
def calculate_stats(numbers):
    """Calculate sum and average of a list of numbers"""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

numbers_list = [1, 2, 3, 4, 5]
total_sum, avg = calculate_stats(numbers_list)
print(f"Numbers: {numbers_list}")
print(f"Sum: {total_sum}, Average: {avg:.2f}")

# ==========================================
# 6. Function with Default Parameters
# ==========================================

print("\n=== Function with Default Parameters ===")

def greet_with_title(name, title="Mr."):
    """Function with a default parameter"""
    print(f"Hello, {title} {name}!")

# Using default parameter
greet_with_title("Smith")

# Overriding default parameter
greet_with_title("Johnson", "Dr.")

# ==========================================
# 7. Function with Variable Number of Arguments
# ==========================================

print("\n=== Function with Variable Arguments ===")

def sum_all(*args):
    """Function that can take any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

# Calling with different numbers of arguments
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")
print(f"Sum of 5: {sum_all(5)}")

# ==========================================
# 8. Function with Keyword Arguments
# ==========================================

print("\n=== Function with Keyword Arguments ===")

def create_profile(**kwargs):
    """Function that accepts keyword arguments"""
    print("Profile created with the following information:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Using keyword arguments
create_profile(name="Alice", age=25, city="NYC", occupation="Developer")

# ==========================================
# 9. Function with Mixed Parameter Types
# ==========================================

print("\n=== Function with Mixed Parameters ===")

def complex_function(name, age, *args, city="Unknown", **kwargs):
    """Function with positional, variable, default, and keyword arguments"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
    if args:
        print(f"Additional info: {args}")
    
    if kwargs:
        print("Extra details:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

# Calling the complex function
complex_function("Bob", 30, "Engineer", "Tech enthusiast", city="San Francisco", hobby="coding", pet="cat")

# ==========================================
# 10. Function Documentation (Docstrings)
# ==========================================

print("\n=== Function Documentation ===")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle
    
    Returns:
    float: The area of the rectangle
    """
    return length * width

# Accessing the docstring
print("Function documentation:")
print(calculate_area.__doc__)

# Using the function
area = calculate_area(5.5, 3.2)
print(f"Area of rectangle: {area}")

# ==========================================
# 11. Function as Variables
# ==========================================

print("\n=== Function as Variables ===")

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Functions can be assigned to variables
my_function = square
result = my_function(4)
print(f"Using function variable: {result}")

# Functions can be stored in lists
functions = [square, cube]
for func in functions:
    print(f"{func.__name__}(3) = {func(3)}")

# ==========================================
# 12. Nested Functions
# ==========================================

print("\n=== Nested Functions ===")

def outer_function(x):
    """Function containing another function"""
    def inner_function(y):
        return x + y  # inner_function can access x from outer_function
    
    return inner_function

# Creating a function that adds 5 to any number
add_five = outer_function(5)
result = add_five(3)
print(f"add_five(3) = {result}")

# ==========================================
# 13. Practical Examples
# ==========================================

print("\n=== Practical Examples ===")

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Test temperature conversions
c_temp = 25
f_temp = celsius_to_fahrenheit(c_temp)
print(f"{c_temp}°C = {f_temp}°F")

f_temp = 77
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp}°C")

# Example 2: String utilities
def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test string functions
test_string = "Hello, World!"
print(f"Original: {test_string}")
print(f"Reversed: {reverse_string(test_string)}")
print(f"Vowel count: {count_vowels(test_string)}")

# Example 3: List utilities
def find_max(numbers):
    """Find the maximum number in a list"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    """Find the minimum number in a list"""
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Test list functions
test_numbers = [23, 45, 12, 67, 34, 89, 56]
print(f"Numbers: {test_numbers}")
print(f"Maximum: {find_max(test_numbers)}")
print(f"Minimum: {find_min(test_numbers)}")

# ==========================================
# 14. Common Mistakes to Avoid
# ==========================================

print("\n=== Common Mistakes ===")

# ❌ Mistake 1: Forgetting to call the function
def say_hello():
    print("Hello!")

# say_hello  # This doesn't call the function, just references it
say_hello()  # ✅ This calls the function

# ❌ Mistake 2: Not using return value
def get_square(x):
    return x ** 2

# get_square(5)  # Return value is ignored
result = get_square(5)  # ✅ Using the return value
print(f"Square of 5: {result}")

# ❌ Mistake 3: Modifying global variables without global keyword
global_var = 10

def modify_global():
    # global_var = 20  # This creates a local variable, doesn't modify global
    global global_var  # ✅ Use global keyword to modify global variable
    global_var = 20

print(f"Before: {global_var}")
modify_global()
print(f"After: {global_var}")

# ==========================================
# 15. Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Use descriptive function names
def calculate_monthly_payment(principal, rate, years):
    """Calculate monthly mortgage payment"""
    monthly_rate = rate / 12 / 100
    num_payments = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return payment

# ✅ Keep functions small and focused
def validate_email(email):
    """Validate email format"""
    return '@' in email and '.' in email

def send_email(email, message):
    """Send email (simplified)"""
    if validate_email(email):
        print(f"Email sent to {email}: {message}")
        return True
    else:
        print(f"Invalid email: {email}")
        return False

# Test the functions
send_email("user@example.com", "Hello!")
send_email("invalid-email", "This won't be sent")

print("\n=== End of Function Basics ===")
print("You've learned the fundamentals of functions in Python! 🎯") 