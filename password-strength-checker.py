#This is password strength checker
import re
import math

def calculate_entropy(password):
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32  # Approximate special characters

    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    return round(entropy, 2)

def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e9  # Assume 1 billion guesses/sec
    seconds = guesses / guesses_per_second
    return seconds

def strength_rating(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter your password: ")
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)
    rating = strength_rating(entropy)

    print(f"\nPassword Strength Report:")
    print(f"- Entropy: {entropy} bits")
    print(f"- Estimated crack time: {crack_time:.2e} seconds")
    print(f"- Rating: {rating}")

if __name__ == "__main__":
    main()
