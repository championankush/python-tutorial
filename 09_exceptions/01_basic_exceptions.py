# Basic Exception Handling in Python
# Using try-except blocks to handle errors gracefully

# ==========================================
# 1. Basic Try-Except Block
# ==========================================

print("=== Basic Try-Except Block ===")

# Without exception handling (this would crash)
# result = 10 / 0  # This would raise a ZeroDivisionError

# With exception handling
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program continues after handling the exception")

# ==========================================
# 2. Catching Different Exception Types
# ==========================================

print("\n=== Catching Different Exception Types ===")

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# Example 2: Invalid type conversion
try:
    number = int("abc")
except ValueError:
    print("Error: Cannot convert 'abc' to an integer")

# Example 3: Index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Error: Index out of range")

# Example 4: Key error in dictionary
try:
    person = {"name": "Alice", "age": 25}
    print(person["city"])
except KeyError:
    print("Error: Key 'city' not found in dictionary")

# ==========================================
# 3. Catching All Exceptions (Not Recommended)
# ==========================================

print("\n=== Catching All Exceptions ===")

# Catching all exceptions (use sparingly)
try:
    result = 10 / 0
except Exception as e:
    print(f"Caught an exception: {e}")

# Better approach: catch specific exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Division error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

# ==========================================
# 4. Getting Exception Information
# ==========================================

print("\n=== Getting Exception Information ===")

import traceback

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print(f"Exception details: {str(e)}")

# Getting the full traceback
try:
    def divide_numbers(a, b):
        return a / b
    
    result = divide_numbers(10, 0)
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
    print("Full traceback:")
    traceback.print_exc()

# ==========================================
# 5. Exception Handling with Functions
# ==========================================

print("\n=== Exception Handling with Functions ===")

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None

# Test the function
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'abc' = {safe_divide(10, 'abc')}")

# ==========================================
# 6. File Operations with Exception Handling
# ==========================================

print("\n=== File Operations with Exception Handling ===")

def read_file_safely(filename):
    """Safely read a file with error handling"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None

# Test file reading
content = read_file_safely("nonexistent_file.txt")
if content is None:
    print("Could not read the file")

# ==========================================
# 7. Input Validation with Exceptions
# ==========================================

print("\n=== Input Validation with Exceptions ===")

def get_valid_age():
    """Get a valid age from user input"""
    while True:
        try:
            age_input = input("Enter your age: ")
            age = int(age_input)
            
            if age < 0:
                print("Error: Age cannot be negative")
                continue
            elif age > 150:
                print("Error: Age seems unrealistic")
                continue
            
            return age
        except ValueError:
            print("Error: Please enter a valid number")
        except KeyboardInterrupt:
            print("\nInput cancelled by user")
            return None

# Uncomment to test interactive input
# age = get_valid_age()
# if age is not None:
#     print(f"Your age is: {age}")

# ==========================================
# 8. Database Operations (Simulated)
# ==========================================

print("\n=== Database Operations (Simulated) ===")

class DatabaseConnection:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        """Simulate database connection"""
        import random
        if random.random() < 0.3:  # 30% chance of failure
            raise ConnectionError("Database server is down")
        self.connected = True
        print("Connected to database")
    
    def execute_query(self, query):
        """Simulate executing a database query"""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        
        if "SELECT" in query.upper():
            return ["row1", "row2", "row3"]
        elif "INSERT" in query.upper():
            return "1 row affected"
        else:
            raise ValueError("Invalid query")

def safe_database_operation():
    """Perform database operations with error handling"""
    db = DatabaseConnection()
    
    try:
        # Try to connect
        db.connect()
        
        # Try to execute queries
        result1 = db.execute_query("SELECT * FROM users")
        print(f"Query result: {result1}")
        
        result2 = db.execute_query("INSERT INTO users VALUES (1, 'Alice')")
        print(f"Insert result: {result2}")
        
    except ConnectionError as e:
        print(f"Database connection failed: {e}")
    except RuntimeError as e:
        print(f"Database operation failed: {e}")
    except ValueError as e:
        print(f"Invalid query: {e}")
    except Exception as e:
        print(f"Unexpected database error: {e}")
    finally:
        print("Database operation completed")

# Test database operations
safe_database_operation()

# ==========================================
# 9. Network Operations (Simulated)
# ==========================================

print("\n=== Network Operations (Simulated) ===")

import time
import random

def fetch_data_from_api(url):
    """Simulate fetching data from an API"""
    # Simulate network delay
    time.sleep(0.1)
    
    # Simulate different types of errors
    error_chance = random.random()
    
    if error_chance < 0.2:
        raise ConnectionError("Network connection failed")
    elif error_chance < 0.4:
        raise TimeoutError("Request timed out")
    elif error_chance < 0.6:
        raise ValueError("Invalid URL format")
    else:
        # Success
        return {"status": "success", "data": "Sample data"}

def safe_api_call(url):
    """Safely call an API with error handling"""
    try:
        response = fetch_data_from_api(url)
        return response
    except ConnectionError:
        print("Network error: Please check your internet connection")
        return None
    except TimeoutError:
        print("Timeout error: The request took too long")
        return None
    except ValueError as e:
        print(f"Invalid URL: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test API calls
urls = ["https://api.example.com/data", "invalid-url", "https://slow-api.com"]
for url in urls:
    print(f"\nFetching data from: {url}")
    result = safe_api_call(url)
    if result:
        print(f"Success: {result}")

# ==========================================
# 10. Custom Error Messages
# ==========================================

print("\n=== Custom Error Messages ===")

def calculate_square_root(number):
    """Calculate square root with custom error handling"""
    try:
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        
        import math
        result = math.sqrt(number)
        return result
    except ValueError as e:
        print(f"Value Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test square root calculation
test_numbers = [4, -1, 16, "abc"]
for num in test_numbers:
    try:
        result = calculate_square_root(num)
        if result is not None:
            print(f"Square root of {num} = {result}")
    except Exception as e:
        print(f"Error calculating square root of {num}: {e}")

# ==========================================
# 11. Exception Handling in Loops
# ==========================================

print("\n=== Exception Handling in Loops ===")

def process_numbers(numbers):
    """Process a list of numbers with error handling"""
    results = []
    
    for i, num in enumerate(numbers):
        try:
            # Simulate processing that might fail
            if num == 0:
                raise ValueError("Cannot process zero")
            elif num < 0:
                raise ValueError("Cannot process negative numbers")
            
            result = 100 / num
            results.append(result)
            print(f"Processed {num}: {result}")
            
        except ValueError as e:
            print(f"Error processing {num} at index {i}: {e}")
            results.append(None)
        except Exception as e:
            print(f"Unexpected error processing {num} at index {i}: {e}")
            results.append(None)
    
    return results

# Test processing
test_numbers = [1, 0, 5, -2, 10, "abc"]
results = process_numbers(test_numbers)
print(f"Final results: {results}")

# ==========================================
# 12. Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Good: Catch specific exceptions
def good_example():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Specific error handling")
    except Exception as e:
        print(f"General error handling: {e}")

# ✅ Good: Use meaningful error messages
def validate_age(age):
    try:
        age_int = int(age)
        if age_int < 0:
            raise ValueError("Age cannot be negative")
        if age_int > 150:
            raise ValueError("Age seems unrealistic")
        return age_int
    except ValueError as e:
        print(f"Invalid age: {e}")
        return None

# ✅ Good: Clean up resources in finally
def file_operation():
    file = None
    try:
        file = open('test.txt', 'w')
        file.write("Test data")
    except IOError as e:
        print(f"File error: {e}")
    finally:
        if file:
            file.close()
            print("File closed")

# ❌ Bad: Catching all exceptions without handling
def bad_example():
    try:
        result = 10 / 0
    except:  # Too broad
        pass  # Silent failure

# ❌ Bad: Ignoring exceptions
def another_bad_example():
    try:
        result = 10 / 0
    except Exception:
        pass  # This hides the error

print("\n=== End of Basic Exception Handling ===")
print("You've learned how to handle exceptions gracefully! 🛡️") 