Password Complexity Checker tool

Python-based Password Complexity Checker tool that evaluates the strength of a password based on common security criteria. The tool provides feedback to users based on the strength of their password.

Explanation:
Password Strength Criteria:
Length: Minimum of 8 characters.
Uppercase Letters: At least one uppercase letter.
Lowercase Letters: At least one lowercase letter.
Numbers: At least one number.
Special Characters: At least one special character (e.g., @, $, #, %).
Strength Scoring:
The password is evaluated based on how many of these criteria it meets.
A score of 5 indicates a strong password, and lower scores give corresponding feedback.
Feedback:
Provides suggestions based on which criteria the password meets or fails.

  """
    Evaluates the strength of a password based on various criteria:
    - Length (minimum 8 characters)
    - Contains both uppercase and lowercase letters
    - Includes numbers
    - Contains special characters (e.g., @, #, $, etc.)
    
  Parameters:
    - password: str, the password to evaluate
    
  Returns:
    - str: Feedback on password strength
    """
    
