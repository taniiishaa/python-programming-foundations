def get_secret_number():
    """Asks Player 1 for a number and hides it."""
    secret = int(input("Player 1, enter a secret number (1-100): "))
    # Print 50 lines to hide the number from Player 2's eyes
    print("\n" * 50)
    return secret

def play_game(secret, total_lives):
    """The main logic for Player 2 to guess the number."""
    lives = total_lives
    
    while lives > 0:
        print(f"\nRemaining Lives: {'❤️' * lives}")
        guess = int(input("Player 2, what is your guess? "))

        if guess == secret:
            print("🏆 Correct! You win!")
            return True # This tells the computer the player won
        
        if guess < secret:
            print("Too LOW!")
        else:
            print("Too HIGH!")
            
        lives -= 1
        
    print(f"Out of lives! The number was {secret}.")
    return False # This tells the computer the player lost

# --- STARTING THE GAME ---
print("--- WELCOME TO THE FUNCTIONAL GAME ---")
secret = get_secret_number()
play_game(secret, 5)
