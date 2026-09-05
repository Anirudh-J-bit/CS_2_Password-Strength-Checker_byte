
MIN_LENGTH = 8
STRONG_LENGTH = 12

WEAK_MAX_SCORE = 2
MODERATE_MAX_SCORE = 5


password = input("Enter password: ")

score = 0
reasons = []

#Score based on length
if len(password) >= MIN_LENGTH:
    score += 1
else:
    reasons.append("Password is shorter than 8 characters")

if len(password) >= STRONG_LENGTH:
    score += 1

#Score based on uppercase characters
if any(char.isupper() for char in password):
    score += 1
else:
    reasons.append("No uppercase letter")

#Score based on lowercase characters
if any(char.islower() for char in password):
    score += 1
else:
    reasons.append("No lowercase letter")

#Score based on numbers
if any(char.isdigit() for char in password):
    score += 1
else:
    reasons.append("No number")

#Score based on special characters
if any(not char.isalnum() for char in password):
    score += 1
else:
    reasons.append("No special character")

#Score category
if score <= WEAK_MAX_SCORE:
    strength = "Weak"
elif score <= MODERATE_MAX_SCORE:
    strength = "Moderate"
else:
    strength = "Strong"



print("Score:", score, "/ 6")
print("Strength:", strength)

#Display reasons
if reasons:
    print("\nReasons:")
    for reason in reasons:
        print(reason)
else:
    print("\nReasons:")
    print("Password satisfies all security requirements")