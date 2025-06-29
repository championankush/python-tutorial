# Calculator Project

A simple command-line calculator that performs basic arithmetic operations.

## 🎯 Project Overview

Build a calculator that can:
- Add, subtract, multiply, and divide numbers
- Handle decimal numbers
- Display results clearly
- Continue calculations with previous results
- Handle division by zero errors

## 📋 Requirements

### Functional Requirements
- [ ] Accept two numbers as input
- [ ] Support four basic operations: +, -, *, /
- [ ] Display the result clearly
- [ ] Handle division by zero
- [ ] Allow continuous calculations
- [ ] Provide option to exit

### Technical Requirements
- [ ] Use functions to organize code
- [ ] Implement error handling
- [ ] Use proper variable naming
- [ ] Include comments explaining logic
- [ ] Handle invalid input gracefully

## 🚀 Getting Started

1. Create a new file called `calculator.py`
2. Implement the basic arithmetic functions
3. Create the main calculator loop
4. Add error handling
5. Test with various inputs

## 📝 Implementation Steps

### Step 1: Basic Functions
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

### Step 2: Main Calculator Loop
```python
def main():
    while True:
        # Get user input
        # Perform calculation
        # Display result
        # Ask to continue
```

### Step 3: Error Handling
- Check for valid numbers
- Handle division by zero
- Validate operation choice

## 🧪 Testing

Test your calculator with:
- Basic operations: 5 + 3, 10 - 4, 6 * 7, 15 / 3
- Decimal numbers: 3.5 + 2.1
- Division by zero: 10 / 0
- Invalid input: letters instead of numbers
- Continuous calculations

## 🎯 Bonus Features

Once the basic calculator works, try adding:
- [ ] More operations (power, square root, etc.)
- [ ] Memory functions (store/recall)
- [ ] History of calculations
- [ ] Scientific calculator functions
- [ ] GUI interface with Tkinter

## 📚 Learning Objectives

This project will help you practice:
- Function definition and calling
- User input handling
- Conditional statements
- Error handling
- Loop control
- String formatting

## 🔗 Related Concepts

Review these sections before starting:
- [02_data_types](../02_data_types/) - Numbers and strings
- [03_control_flow](../03_control_flow/) - Loops and conditionals
- [04_functions](../04_functions/) - Function definition
- [09_exceptions](../09_exceptions/) - Error handling

## 💡 Tips

- Start simple and add features gradually
- Test each function individually
- Use meaningful variable names
- Add comments to explain complex logic
- Handle edge cases (like division by zero)

---

**Ready to build your first calculator? Let's get coding! 🧮** 