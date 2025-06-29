# Simple Calculator
# A command-line calculator that performs basic arithmetic operations

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_menu():
    """Display the calculator menu"""
    print("\n=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("========================")

def main():
    """Main calculator function"""
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        
        # Get user choice
        try:
            choice = input("Enter your choice (1-5): ")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        
        # Exit condition
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1-5.")
            continue
        
        # Get numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        
        # Display result
        if isinstance(result, str):
            print(f"Result: {result}")
        else:
            print(f"{num1} {operation} {num2} = {result}")
        
        # Ask if user wants to continue
        continue_calc = input("\nDo another calculation? (y/n): ").lower()
        if continue_calc not in ['y', 'yes']:
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main() 