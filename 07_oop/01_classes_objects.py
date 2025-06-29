# Classes and Objects in Python
# The foundation of Object-Oriented Programming

# ==========================================
# 1. Basic Class Definition
# ==========================================

print("=== Basic Class Definition ===")

class Dog:
    """A simple class to represent a dog"""
    
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says: Woof!"
    
    def describe(self):
        """Describe the dog"""
        return f"{self.name} is {self.age} years old"

# Creating objects (instances) of the Dog class
my_dog = Dog("Buddy", 3)
print(f"Dog object: {my_dog}")
print(f"Dog name: {my_dog.name}")
print(f"Dog age: {my_dog.age}")
print(my_dog.bark())
print(my_dog.describe())

# ==========================================
# 2. Multiple Objects
# ==========================================

print("\n=== Multiple Objects ===")

# Create multiple dog objects
dog1 = Dog("Max", 5)
dog2 = Dog("Luna", 2)
dog3 = Dog("Rocky", 7)

# Each object has its own data
print(f"{dog1.name} is {dog1.age} years old")
print(f"{dog2.name} is {dog2.age} years old")
print(f"{dog3.name} is {dog3.age} years old")

# ==========================================
# 3. Class Attributes vs Instance Attributes
# ==========================================

print("\n=== Class vs Instance Attributes ===")

class Car:
    """A class to represent a car"""
    
    # Class attribute (shared by all instances)
    wheels = 4
    engine_type = "Internal Combustion"
    
    def __init__(self, brand, model, year):
        """Initialize a new car"""
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, miles):
        """Drive the car and update mileage"""
        self.mileage += miles
        return f"Drove {miles} miles. Total mileage: {self.mileage}"
    
    def get_info(self):
        """Get car information"""
        return f"{self.year} {self.brand} {self.model}"

# Create car objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print(f"Car 1: {car1.get_info()}")
print(f"Car 2: {car2.get_info()}")

# Class attributes are shared
print(f"All cars have {Car.wheels} wheels")
print(f"Car 1 wheels: {car1.wheels}")
print(f"Car 2 wheels: {car2.wheels}")

# Instance attributes are unique
print(f"Car 1 mileage: {car1.mileage}")
print(f"Car 2 mileage: {car2.mileage}")

# ==========================================
# 4. Methods with Parameters
# ==========================================

print("\n=== Methods with Parameters ===")

class BankAccount:
    """A class to represent a bank account"""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize a new bank account"""
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return f"Balance: ${self.balance}"
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self.transactions

# Create and use a bank account
account = BankAccount("Alice Johnson", 1000)
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Should fail
print(f"Transaction history: {account.get_transaction_history()}")

# ==========================================
# 5. Constructor with Default Values
# ==========================================

print("\n=== Constructor with Default Values ===")

class Student:
    """A class to represent a student"""
    
    def __init__(self, name, age=18, major="Undecided"):
        """Initialize a new student with default values"""
        self.name = name
        self.age = age
        self.major = major
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"Added grade: {grade}"
        else:
            return "Invalid grade (must be 0-100)"
    
    def get_average(self):
        """Calculate and return the average grade"""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    
    def get_info(self):
        """Get student information"""
        return f"{self.name}, {self.age} years old, Major: {self.major}"

# Create students with different numbers of parameters
student1 = Student("Bob Smith")  # Uses defaults
student2 = Student("Carol Davis", 20)  # Uses some defaults
student3 = Student("David Wilson", 22, "Computer Science")  # All parameters

print(f"Student 1: {student1.get_info()}")
print(f"Student 2: {student2.get_info()}")
print(f"Student 3: {student3.get_info()}")

# Add grades and calculate averages
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)
print(f"{student1.name}'s average: {student1.get_average():.2f}")

# ==========================================
# 6. Object Identity and Comparison
# ==========================================

print("\n=== Object Identity and Comparison ===")

class Point:
    """A class to represent a 2D point"""
    
    def __init__(self, x, y):
        """Initialize a new point"""
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        """Calculate distance to origin"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        """String representation of the point"""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Check if two points are equal"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

# Create points
point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 12)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Point 3: {point3}")

# Object identity (different objects)
print(f"point1 is point2: {point1 is point2}")

# Object equality (same values)
print(f"point1 == point2: {point1 == point2}")
print(f"point1 == point3: {point1 == point3}")

# Calculate distances
print(f"Distance to origin for {point1}: {point1.distance_to_origin()}")
print(f"Distance to origin for {point3}: {point3.distance_to_origin()}")

# ==========================================
# 7. Class Methods and Static Methods
# ==========================================

print("\n=== Class Methods and Static Methods ===")

class Temperature:
    """A class to handle temperature conversions"""
    
    def __init__(self, celsius):
        """Initialize with temperature in Celsius"""
        self.celsius = celsius
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Create a Temperature object from Fahrenheit"""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @classmethod
    def from_kelvin(cls, kelvin):
        """Create a Temperature object from Kelvin"""
        celsius = kelvin - 273.15
        return cls(celsius)
    
    @staticmethod
    def is_valid_celsius(celsius):
        """Check if Celsius temperature is valid"""
        return -273.15 <= celsius <= 1000
    
    def to_fahrenheit(self):
        """Convert to Fahrenheit"""
        return self.celsius * 9/5 + 32
    
    def to_kelvin(self):
        """Convert to Kelvin"""
        return self.celsius + 273.15
    
    def __str__(self):
        """String representation"""
        return f"{self.celsius}°C ({self.to_fahrenheit():.1f}°F, {self.to_kelvin():.1f}K)"

# Create temperatures using different methods
temp1 = Temperature(25)  # From Celsius
temp2 = Temperature.from_fahrenheit(77)  # From Fahrenheit
temp3 = Temperature.from_kelvin(298.15)  # From Kelvin

print(f"Temp 1: {temp1}")
print(f"Temp 2: {temp2}")
print(f"Temp 3: {temp3}")

# Use static method
print(f"Is 100°C valid? {Temperature.is_valid_celsius(100)}")
print(f"Is -300°C valid? {Temperature.is_valid_celsius(-300)}")

# ==========================================
# 8. Object Lifecycle
# ==========================================

print("\n=== Object Lifecycle ===")

class Resource:
    """A class to demonstrate object lifecycle"""
    
    def __init__(self, name):
        """Initialize the resource"""
        self.name = name
        print(f"Resource '{self.name}' created")
    
    def use(self):
        """Use the resource"""
        print(f"Using resource '{self.name}'")
    
    def __del__(self):
        """Destructor - called when object is destroyed"""
        print(f"Resource '{self.name}' destroyed")

# Create and use resources
print("Creating resources...")
resource1 = Resource("File")
resource2 = Resource("Database")

print("Using resources...")
resource1.use()
resource2.use()

print("Resources will be destroyed when they go out of scope")

# ==========================================
# 9. Practical Example: Library Book
# ==========================================

print("\n=== Practical Example: Library Book ===")

class Book:
    """A class to represent a library book"""
    
    def __init__(self, title, author, isbn, year_published):
        """Initialize a new book"""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published
        self.is_checked_out = False
        self.checked_out_by = None
        self.checkout_date = None
    
    def checkout(self, borrower):
        """Check out the book to a borrower"""
        if not self.is_checked_out:
            self.is_checked_out = True
            self.checked_out_by = borrower
            from datetime import datetime
            self.checkout_date = datetime.now()
            return f"'{self.title}' checked out to {borrower}"
        else:
            return f"'{self.title}' is already checked out to {self.checked_out_by}"
    
    def return_book(self):
        """Return the book to the library"""
        if self.is_checked_out:
            self.is_checked_out = False
            borrower = self.checked_out_by
            self.checked_out_by = None
            self.checkout_date = None
            return f"'{self.title}' returned by {borrower}"
        else:
            return f"'{self.title}' is not checked out"
    
    def get_status(self):
        """Get the current status of the book"""
        if self.is_checked_out:
            return f"'{self.title}' is checked out to {self.checked_out_by}"
        else:
            return f"'{self.title}' is available"
    
    def __str__(self):
        """String representation of the book"""
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({status})"

# Create and use books
book1 = Book("Python Programming", "John Smith", "1234567890", 2023)
book2 = Book("Data Science", "Jane Doe", "0987654321", 2022)

print(f"Book 1: {book1}")
print(f"Book 2: {book2}")

# Check out books
print(book1.checkout("Alice"))
print(book2.checkout("Bob"))
print(book1.checkout("Charlie"))  # Should fail

# Check status
print(book1.get_status())
print(book2.get_status())

# Return books
print(book1.return_book())
print(book2.return_book())

# ==========================================
# 10. Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Good: Use descriptive class names
class CustomerAccount:
    pass

# ✅ Good: Use descriptive method names
class Calculator:
    def add_numbers(self, a, b):
        return a + b
    
    def calculate_area(self, length, width):
        return length * width

# ✅ Good: Use docstrings
class Product:
    """A class to represent a product in an e-commerce system"""
    
    def __init__(self, name, price, category):
        """
        Initialize a new product
        
        Args:
            name (str): Product name
            price (float): Product price
            category (str): Product category
        """
        self.name = name
        self.price = price
        self.category = category

# ✅ Good: Use type hints (Python 3.5+)
class Employee:
    def __init__(self, name: str, salary: float, department: str):
        self.name = name
        self.salary = salary
        self.department = department
    
    def get_salary_info(self) -> str:
        return f"{self.name} earns ${self.salary} in {self.department}"

print("\n=== End of Classes and Objects ===")
print("You've learned the basics of Object-Oriented Programming! 🏗️") 