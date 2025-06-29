# Solution: Grade Calculator Exercise
# This file contains the solution for Exercise 1 from 03_control_flow

def calculate_grade(score):
    """
    Calculate letter grade based on numerical score.
    
    Args:
        score (int/float): Numerical score (0-100)
    
    Returns:
        str: Letter grade (A, B, C, D, F) or "Invalid score"
    """
    # Check for invalid scores first
    if score < 0 or score > 100:
        return "Invalid score"
    
    # Determine grade based on score ranges
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_grade_with_message(score):
    """
    Calculate letter grade with descriptive message.
    
    Args:
        score (int/float): Numerical score (0-100)
    
    Returns:
        tuple: (letter_grade, message) or ("Invalid score", "Invalid input")
    """
    # Check for invalid scores first
    if score < 0 or score > 100:
        return "Invalid score", "Invalid input"
    
    # Determine grade and message based on score ranges
    if score >= 90:
        return "A", "Excellent work!"
    elif score >= 80:
        return "B", "Good job!"
    elif score >= 70:
        return "C", "Satisfactory performance"
    elif score >= 60:
        return "D", "Needs improvement"
    else:
        return "F", "Failing grade - requires attention"

# Test the functions
if __name__ == "__main__":
    print("=== Basic Grade Calculator ===")
    test_scores = [95, 87, 73, 65, 45, 105, -5]
    
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score: {score} → Grade: {grade}")
    
    print("\n=== Grade Calculator with Messages ===")
    for score in test_scores:
        grade, message = calculate_grade_with_message(score)
        print(f"Score: {score} → Grade: {grade} - {message}")
    
    print("\n=== Additional Test Cases ===")
    edge_cases = [0, 59, 60, 69, 70, 79, 80, 89, 90, 100]
    
    for score in edge_cases:
        grade = calculate_grade(score)
        print(f"Score: {score} → Grade: {grade}")

# Alternative solution using a more compact approach
def calculate_grade_compact(score):
    """
    Compact version of grade calculator using a different approach.
    """
    if not (0 <= score <= 100):
        return "Invalid score"
    
    # Use integer division to determine grade
    grade_index = (100 - score) // 10
    
    if grade_index == 0:  # score is 90-100
        return "A"
    elif grade_index == 1:  # score is 80-89
        return "B"
    elif grade_index == 2:  # score is 70-79
        return "C"
    elif grade_index == 3:  # score is 60-69
        return "D"
    else:  # score is 0-59
        return "F"

# Test the compact version
print("\n=== Compact Version Test ===")
for score in test_scores:
    grade = calculate_grade_compact(score)
    print(f"Score: {score} → Grade: {grade}") 