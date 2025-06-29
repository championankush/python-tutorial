# Exercise 1: Grade Calculator

## 🎯 Objective
Create a program that calculates and assigns letter grades based on numerical scores using conditional statements.

## 📋 Requirements

Create a function called `calculate_grade(score)` that:

1. **Takes a numerical score** as input (0-100)
2. **Returns a letter grade** based on the following scale:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: 0-59
3. **Handles invalid scores** (negative numbers or scores above 100) by returning "Invalid score"

## 🧪 Test Cases

Your function should work correctly with these test cases:

```python
print(calculate_grade(95))  # Should return "A"
print(calculate_grade(87))  # Should return "B"
print(calculate_grade(73))  # Should return "C"
print(calculate_grade(65))  # Should return "D"
print(calculate_grade(45))  # Should return "F"
print(calculate_grade(105)) # Should return "Invalid score"
print(calculate_grade(-5))  # Should return "Invalid score"
```

## 💡 Hints

1. Use `if`, `elif`, and `else` statements
2. Check for invalid scores first
3. Use comparison operators (`>=`, `<=`)
4. Remember that conditions are checked in order

## 🚀 Bonus Challenge

Extend your function to also return a descriptive message along with the grade:

```python
def calculate_grade_with_message(score):
    # Your code here
    pass

# Example output:
# calculate_grade_with_message(95) → ("A", "Excellent work!")
# calculate_grade_with_message(87) → ("B", "Good job!")
# calculate_grade_with_message(45) → ("F", "Needs improvement")
```

## 📝 Solution Template

```python
def calculate_grade(score):
    """
    Calculate letter grade based on numerical score.
    
    Args:
        score (int/float): Numerical score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, F) or "Invalid score"
    """
    # Your code here
    pass

# Test your function
if __name__ == "__main__":
    test_scores = [95, 87, 73, 65, 45, 105, -5]
    
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score: {score} → Grade: {grade}")
```

## ✅ Success Criteria

- [ ] Function correctly assigns grades A through F
- [ ] Function handles invalid scores (negative or >100)
- [ ] All test cases pass
- [ ] Code is well-commented and readable
- [ ] Bonus challenge completed (optional)

## 🔗 Related Concepts

- Conditional statements (`if`, `elif`, `else`)
- Comparison operators
- Function definition and return values
- Input validation

---

**Good luck! Remember to test your function with different inputs to make sure it works correctly.** 🎓 