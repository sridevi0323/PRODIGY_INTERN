import re

def check_password_strength(password):
  
    # Criteria for password strength
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[@$!%*#?&]", password) is not None

    # Strength evaluation
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Feedback based on score
    if score == 5:
        return "Strong password! Your password meets all security criteria."
    elif score == 4:
        return "Good password. Consider adding special characters for added security."
    elif score == 3:
        return "Moderate password. Try including numbers and special characters."
    elif score == 2:
        return "Weak password. Ensure it's at least 8 characters long with a mix of letters and numbers."
    else:
        return "Very weak password! Consider using a longer password with a mix of uppercase, lowercase, numbers, and special characters."

if __name__ == "__main__":
    # User input for password
    password = input("Enter your password: ")
    
    # Check the strength of the password
    feedback = check_password_strength(password)
    print(feedback)

