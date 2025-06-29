# Basic File Operations in Python
# Opening, reading, writing, and closing files

import os
import shutil
import datetime
import io

# ==========================================
# 1. Creating a Sample File
# ==========================================

print("=== Creating a Sample File ===")

# First, let's create a sample text file
sample_content = """Hello, this is a sample text file.
This file contains multiple lines of text.
We'll use this file to demonstrate file operations.
Python makes file handling very easy and intuitive.
"""

# Write the content to a file
with open('sample.txt', 'w') as file:
    file.write(sample_content)

print("Sample file 'sample.txt' created successfully!")

# ==========================================
# 2. Basic File Opening and Closing
# ==========================================

print("\n=== Basic File Opening and Closing ===")

# Method 1: Traditional way (explicit close)
file = open('sample.txt', 'r')
content = file.read()
file.close()
print("File content (traditional method):")
print(content)

# Method 2: Using context manager (recommended)
with open('sample.txt', 'r') as file:
    content = file.read()
print("\nFile content (context manager):")
print(content)

# ==========================================
# 3. Different File Modes
# ==========================================

print("\n=== Different File Modes ===")

# 'r' - Read mode (default)
with open('sample.txt', 'r') as file:
    print("Read mode - reading entire file:")
    print(file.read())

# 'w' - Write mode (overwrites existing content)
with open('output.txt', 'w') as file:
    file.write("This is new content.\n")
    file.write("The old content was overwritten.\n")
print("Write mode - created 'output.txt'")

# 'a' - Append mode (adds to existing content)
with open('output.txt', 'a') as file:
    file.write("This line was appended.\n")
    file.write("The file now has more content.\n")
print("Append mode - added content to 'output.txt'")

# 'r+' - Read and write mode
with open('output.txt', 'r+') as file:
    content = file.read()
    print(f"Current content:\n{content}")
    file.write("This was added in read+write mode.\n")

# ==========================================
# 4. Reading Files in Different Ways
# ==========================================

print("\n=== Reading Files in Different Ways ===")

# Read entire file as a string
with open('sample.txt', 'r') as file:
    full_content = file.read()
print("1. Reading entire file:")
print(full_content)

# Read file line by line
with open('sample.txt', 'r') as file:
    print("\n2. Reading line by line:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.rstrip()}")

# Read all lines into a list
with open('sample.txt', 'r') as file:
    lines = file.readlines()
print(f"\n3. Reading all lines into list:")
print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.rstrip()}")

# Read specific number of characters
with open('sample.txt', 'r') as file:
    first_20_chars = file.read(20)
print(f"\n4. Reading first 20 characters:")
print(f"'{first_20_chars}'")

# ==========================================
# 5. Writing Different Types of Content
# ==========================================

print("\n=== Writing Different Types of Content ===")

# Write a single string
with open('single_string.txt', 'w') as file:
    file.write("This is a single string written to a file.")

# Write multiple lines
lines_to_write = [
    "First line of the file.",
    "Second line of the file.",
    "Third line of the file.",
    "Fourth line of the file."
]

with open('multiple_lines.txt', 'w') as file:
    for line in lines_to_write:
        file.write(line + '\n')

# Write using writelines (more efficient for multiple lines)
with open('writelines_example.txt', 'w') as file:
    file.writelines(lines_to_write)

print("Created files: single_string.txt, multiple_lines.txt, writelines_example.txt")

# ==========================================
# 6. File Position and Seeking
# ==========================================

print("\n=== File Position and Seeking ===")

with open('sample.txt', 'r') as file:
    # Get current position
    print(f"Initial position: {file.tell()}")
    
    # Read first 10 characters
    first_part = file.read(10)
    print(f"After reading 10 chars, position: {file.tell()}")
    print(f"First 10 chars: '{first_part}'")
    
    # Seek to beginning
    file.seek(0)
    print(f"After seeking to 0, position: {file.tell()}")
    
    # Seek to specific position
    file.seek(20)
    print(f"After seeking to 20, position: {file.tell()}")
    next_part = file.read(10)
    print(f"Next 10 chars: '{next_part}'")

# ==========================================
# 7. Working with Binary Files
# ==========================================

print("\n=== Working with Binary Files ===")

# Create a simple binary file
binary_data = bytes([65, 66, 67, 68, 69, 70])  # ASCII: ABCDEF

with open('binary_file.bin', 'wb') as file:
    file.write(binary_data)

# Read binary file
with open('binary_file.bin', 'rb') as file:
    read_data = file.read()
    print(f"Binary data: {read_data}")
    print(f"As ASCII: {read_data.decode('ascii')}")

# ==========================================
# 8. File Information
# ==========================================

print("\n=== File Information ===")

# Get file size
file_size = os.path.getsize('sample.txt')
print(f"File size of 'sample.txt': {file_size} bytes")

# Check if file exists
print(f"Does 'sample.txt' exist? {os.path.exists('sample.txt')}")
print(f"Does 'nonexistent.txt' exist? {os.path.exists('nonexistent.txt')}")

# Get file modification time
mod_time = os.path.getmtime('sample.txt')
print(f"Last modified: {mod_time}")

# ==========================================
# 9. Error Handling in File Operations
# ==========================================

print("\n=== Error Handling in File Operations ===")

# Try to open a non-existent file
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File 'nonexistent.txt' not found")

# Try to write to a read-only file (simulated)
try:
    with open('sample.txt', 'r') as file:
        file.write("This will fail")
except io.UnsupportedOperation:
    print("Error: Cannot write to file opened in read mode")

# ==========================================
# 10. Practical Example: Log File
# ==========================================

print("\n=== Practical Example: Log File ===")

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
    
    def log(self, message, level="INFO"):
        """Add a log entry with timestamp"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        with open(self.log_file, 'a') as file:
            file.write(log_entry)
    
    def read_logs(self):
        """Read all log entries"""
        try:
            with open(self.log_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "No log file found"

# Use the logger
logger = Logger('application.log')
logger.log("Application started")
logger.log("User logged in", "INFO")
logger.log("Database connection failed", "ERROR")
logger.log("Application shutdown", "INFO")

print("Log entries created. Reading logs:")
print(logger.read_logs())

# ==========================================
# 11. File Copying and Moving
# ==========================================

print("\n=== File Copying and Moving ===")

# Copy a file
shutil.copy('sample.txt', 'sample_copy.txt')
print("File copied: sample.txt → sample_copy.txt")

# Copy with metadata
shutil.copy2('sample.txt', 'sample_copy2.txt')
print("File copied with metadata: sample.txt → sample_copy2.txt")

# Move/rename a file
shutil.move('sample_copy.txt', 'sample_renamed.txt')
print("File moved: sample_copy.txt → sample_renamed.txt")

# ==========================================
# 12. Directory Operations
# ==========================================

print("\n=== Directory Operations ===")

# Create a directory
os.makedirs('test_directory', exist_ok=True)
print("Created directory: test_directory")

# Create a file in the directory
with open('test_directory/test_file.txt', 'w') as file:
    file.write("This is a test file in a subdirectory")

# List directory contents
print(f"Contents of test_directory: {os.listdir('test_directory')}")

# Check if it's a file or directory
for item in os.listdir('test_directory'):
    item_path = os.path.join('test_directory', item)
    if os.path.isfile(item_path):
        print(f"{item} is a file")
    elif os.path.isdir(item_path):
        print(f"{item} is a directory")

# ==========================================
# 13. Best Practices
# ==========================================

print("\n=== Best Practices ===")

# ✅ Good: Use context managers
with open('best_practice.txt', 'w') as file:
    file.write("This is the recommended way to handle files")

# ✅ Good: Handle exceptions
try:
    with open('best_practice.txt', 'r') as file:
        content = file.read()
    print("File read successfully")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

# ✅ Good: Use appropriate encoding
with open('unicode_file.txt', 'w', encoding='utf-8') as file:
    file.write("This file contains Unicode characters: é, ñ, 中文")

# ✅ Good: Close files explicitly if not using context manager
file = open('explicit_close.txt', 'w')
try:
    file.write("This file will be explicitly closed")
finally:
    file.close()

# ==========================================
# 14. Cleanup
# ==========================================

print("\n=== Cleanup ===")

# Remove test files
files_to_remove = [
    'sample.txt', 'output.txt', 'single_string.txt', 
    'multiple_lines.txt', 'writelines_example.txt',
    'binary_file.bin', 'application.log', 'sample_copy2.txt',
    'sample_renamed.txt', 'best_practice.txt', 'unicode_file.txt',
    'explicit_close.txt'
]

for file_name in files_to_remove:
    try:
        os.remove(file_name)
        print(f"Removed: {file_name}")
    except FileNotFoundError:
        print(f"File not found (already removed): {file_name}")

# Remove test directory
try:
    shutil.rmtree('test_directory')
    print("Removed directory: test_directory")
except FileNotFoundError:
    print("Directory not found (already removed): test_directory")

print("\n=== End of Basic File Operations ===")
print("You've learned the fundamentals of file handling in Python! 📁") 