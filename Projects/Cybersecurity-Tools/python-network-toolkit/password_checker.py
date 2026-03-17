import string

def check_password():
    password = input("Enter password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 1:
        print("Weak password")

    elif score == 2 or score == 3:
        print("Moderate password")

    else:
        print("Strong password")
