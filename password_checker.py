import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"[0-9]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = {
        "Minimum length of 8 characters": length_error,
        "At least one uppercase letter": uppercase_error,
        "At least one lowercase letter": lowercase_error,
        "At least one number": digit_error,
        "At least one special character": special_char_error,
    }

    if not any(errors.values()):
        return "✅ Password Strength: STRONG", []
    else:
        failed_criteria = [rule for rule, failed in errors.items() if failed]
        return "⚠️ Password Strength: WEAK", failed_criteria

print("🔐 Password Strength Checker")
user_password = input("Enter your password: ")

strength, feedback = check_password_strength(user_password)

print(strength)
if feedback:
    print("Please improve your password by meeting the following:")
    for issue in feedback:
        print(f"- {issue}")
