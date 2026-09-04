# calculator.py
# ---------------------------
# A Simple Command-Line Calculator
# Supports: Addition, Subtraction, Multiplication, Division
# ---------------------------

# --- Step 1: Define Functions for each operation ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error! Division by zero is not allowed."
    return a / b

# --- Step 2: Main Program Loop ---
def calculator():
    print("\n=== 🧮 Simple CLI Calculator ===")
    print("Operations available: +  -  *  /")
    print("Type 'exit' anytime to quit.\n")

    while True:
        # Ask user to choose operation
        choice = input("👉 Choose operation (+, -, *, /) or 'exit': ")

        if choice.lower() == "exit":
            print("\n👋 Thank you for using the calculator. Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("⚠️ Invalid choice! Please enter +, -, *, / or exit.\n")
            continue

        # Get numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numeric values!\n")
            continue

        # Perform calculation
        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)

        print(f"✅ Result: {result}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()
