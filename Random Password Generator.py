import random
import string
import sys

def generate_secure_password():
    print("=" * 30)
    print("  ADVANCED PASSWORD GENERATOR  ")
    print("=" * 30)

    try:
        # User input for parameters
        length = int(input("Enter desired length (min 4): "))
        if length < 4:
            print("Length too short for a secure password. Setting to 8.")
            length = 8

        use_upper = input("Include Uppercase? (y/n): ").lower() == 'y'
        use_digits = input("Include Numbers? (y/n): ").lower() == 'y'
        use_syms = input("Include Symbols? (y/n): ").lower() == 'y'

        # Building character sets
        chars = string.ascii_lowercase
        mandatory_chars = [random.choice(string.ascii_lowercase)]

        if use_upper:
            chars += string.ascii_uppercase
            mandatory_chars.append(random.choice(string.ascii_uppercase))
        if use_digits:
            chars += string.digits
            mandatory_chars.append(random.choice(string.digits))
        if use_syms:
            chars += string.punctuation
            mandatory_chars.append(random.choice(string.punctuation))

        # Fill the rest of the length randomly
        remaining_length = length - len(mandatory_chars)
        password_list = mandatory_chars + [random.choice(chars) for _ in range(remaining_length)]

        # Shuffle to ensure the mandatory characters aren't always at the start
        random.shuffle(password_list)
        
        final_password = "".join(password_list)

        print("-" * 30)
        print(f"GENERATED PASSWORD: {final_password}")
        print("-" * 30)
        
        # Calculate Strength
        strength = "Weak"
        if length >= 12 and use_upper and use_digits and use_syms:
            strength = "Very Strong"
        elif length >= 8 and (use_upper or use_digits):
            strength = "Medium"
            
        print(f"Password Strength: {strength}")
        print("=" * 30)

    except ValueError:
        print("Critical Error: Please enter a valid number for length.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        generate_secure_password()
        if input("\nGenerate another? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break
