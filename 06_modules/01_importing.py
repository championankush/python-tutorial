# Importing Modules in Python
# How to use existing modules and libraries

# ==========================================
# 1. Basic Import Statements
# ==========================================

print("=== Basic Import Statements ===")

# Import entire module
import math
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Import specific functions/classes
from math import sqrt, factorial
print(f"Pi (from math): {math.pi}")
print(f"Factorial of 5: {factorial(5)}")

# Import with alias
import math as m
print(f"Pi (alias): {m.pi}")

# Import specific items with alias
from math import sqrt as square_root
print(f"Square root of 25: {square_root(25)}")

# ==========================================
# 2. Importing Multiple Items
# ==========================================

print("\n=== Importing Multiple Items ===")

# Import multiple items from one module
from math import sqrt, log
print(f"Pi (from math): {math.pi}")
print(f"Euler's number: {math.e}")
print(f"Natural log of 10: {log(10)}")

# Import from multiple modules
from random import randint
from datetime import datetime

print(f"Random number: {randint(1, 100)}")
print(f"Current time: {datetime.now()}")

# ==========================================
# 3. Importing All Items (Not Recommended)
# ==========================================

print("\n=== Importing All Items ===")

# Import all items from a module
from math import *
print(f"Pi: {pi}")
print(f"E: {e}")
print(f"Tau: {tau}")

# Warning: This can cause naming conflicts
# Better to import specific items or use module name

# ==========================================
# 4. Conditional Imports
# ==========================================

print("\n=== Conditional Imports ===")

# Import modules conditionally
try:
    import numpy as np
    print("NumPy is available")
    print(f"NumPy version: {np.__version__}")
except ImportError:
    print("NumPy is not installed")

# Alternative approach
import sys
if 'pandas' in sys.modules:
    print("Pandas is already imported")
else:
    print("Pandas is not imported")

# ==========================================
# 5. Importing from Different Locations
# ==========================================

print("\n=== Importing from Different Locations ===")

# Import from current directory
import os
print(f"Current working directory: {os.getcwd()}")

# Import from parent directory
import sys
sys.path.append('..')
# Now you can import from parent directory

# Import from specific path
import sys
sys.path.append('/path/to/your/modules')
# Now you can import modules from that path

# ==========================================
# 6. Built-in Modules Examples
# ==========================================

print("\n=== Built-in Modules Examples ===")

# Math module
import math
print(f"Math functions:")
print(f"  Ceiling of 3.7: {math.ceil(3.7)}")
print(f"  Floor of 3.7: {math.floor(3.7)}")
print(f"  Absolute value of -5: {math.fabs(-5)}")
print(f"  Power 2^8: {math.pow(2, 8)}")

# Random module
import random
print(f"\nRandom functions:")
print(f"  Random float: {random.random()}")
print(f"  Random int (1-10): {random.randint(1, 10)}")
print(f"  Random choice: {random.choice(['apple', 'banana', 'orange'])}")

# Datetime module
import datetime
now = datetime.datetime.now()
print(f"\nDatetime functions:")
print(f"  Current date/time: {now}")
print(f"  Current year: {now.year}")
print(f"  Current month: {now.month}")
print(f"  Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# ==========================================
# 7. OS and System Modules
# ==========================================

print("\n=== OS and System Modules ===")

import os
import sys

print(f"OS functions:")
print(f"  Current directory: {os.getcwd()}")
print(f"  Platform: {sys.platform}")
print(f"  Python version: {sys.version}")
print(f"  Environment variables: {list(os.environ.keys())[:5]}")

# ==========================================
# 8. Collections Module
# ==========================================

print("\n=== Collections Module ===")

from collections import Counter, defaultdict, namedtuple

# Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(f"Word count: {word_count}")

# DefaultDict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"DefaultDict: {dict(dd)}")

# NamedTuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 25, 'New York')
print(f"Person: {person}")

# ==========================================
# 9. JSON Module
# ==========================================

print("\n=== JSON Module ===")

import json

# Python object to JSON
data = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'hobbies': ['reading', 'swimming']
}

json_string = json.dumps(data, indent=2)
print(f"JSON string:\n{json_string}")

# JSON to Python object
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# ==========================================
# 10. Re (Regular Expressions) Module
# ==========================================

print("\n=== Re Module ===")

import re

text = "My phone number is 123-456-7890 and email is alice@example.com"

# Find phone number
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_match = re.search(phone_pattern, text)
if phone_match:
    print(f"Phone number found: {phone_match.group()}")

# Find email
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email_match = re.search(email_pattern, text)
if email_match:
    print(f"Email found: {email_match.group()}")

# ==========================================
# 11. Urllib Module (Web Requests)
# ==========================================

print("\n=== Urllib Module ===")

# Note: This is a basic example. In practice, use 'requests' library
try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
    
    # Parse URL
    url = "https://www.python.org"
    parsed = urlparse(url)
    print(f"URL components:")
    print(f"  Scheme: {parsed.scheme}")
    print(f"  Netloc: {parsed.netloc}")
    print(f"  Path: {parsed.path}")
    
    # Note: Actually opening URLs requires internet connection
    # and proper error handling
    
except ImportError:
    print("urllib module not available")

# ==========================================
# 12. Import Best Practices
# ==========================================

print("\n=== Import Best Practices ===")

# ✅ Good: Import specific items
from math import sqrt
from datetime import datetime

# ✅ Good: Use aliases for clarity
# import numpy as np
# import pandas as pd

# ✅ Good: Group imports
# Standard library imports
import os
import sys
import json

# Third-party imports
# import numpy as np
# import pandas as pd

# Local imports
# from .my_module import my_function

# ❌ Avoid: Import all items
# from math import *

# ❌ Avoid: Importing unused modules
# import unused_module

# ==========================================
# 13. Module Attributes
# ==========================================

print("\n=== Module Attributes ===")

import math

print(f"Math module attributes:")
print(f"  __name__: {math.__name__}")
print(f"  __file__: {math.__file__}")
if math.__doc__:
    print(f"  __doc__: {math.__doc__[:100]}...")

# List all attributes
print(f"  Available functions: {[attr for attr in dir(math) if not attr.startswith('_')][:10]}")

# ==========================================
# 14. Reloading Modules
# ==========================================

print("\n=== Reloading Modules ===")

# In Python 3.4+, use importlib
import importlib

# Example: reload a module
# importlib.reload(module_name)

# This is useful during development when you modify a module
# and want to reload it without restarting the interpreter

# ==========================================
# 15. Practical Example: Weather App
# ==========================================

print("\n=== Practical Example: Weather App ===")

# Simulated weather app using multiple modules
import random
from datetime import datetime
from collections import defaultdict

class WeatherApp:
    def __init__(self):
        self.weather_data = defaultdict(list)
    
    def generate_weather(self, city):
        """Generate simulated weather data"""
        temperature = random.randint(15, 35)
        humidity = random.randint(30, 90)
        condition = random.choice(['Sunny', 'Cloudy', 'Rainy', 'Windy'])
        
        weather_info = {
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition,
            'timestamp': datetime.now()
        }
        
        self.weather_data[city].append(weather_info)
        return weather_info
    
    def get_weather_report(self, city):
        """Get current weather for a city"""
        if city in self.weather_data:
            return self.weather_data[city][-1]
        else:
            return self.generate_weather(city)

# Use the weather app
weather_app = WeatherApp()
report = weather_app.get_weather_report('New York')
print(f"Weather in New York: {report}")

print("\n=== End of Module Importing ===")
print("You've learned how to import and use modules effectively! 📦") 