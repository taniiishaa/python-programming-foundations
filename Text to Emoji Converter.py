import time

def text_to_emoji_pro():
    """
    Ek advanced converter jo categories aur slow-print effect ka use karta hai.
    """
    # 1. Badi Emoji Dictionary (Impressive dikhne ke liye)
    emoji_store = {
        # Emotions
        "happy": "😊", "sad": "😢", "angry": "😠", "cool": "😎",
        # Nature & Food
        "fire": "🔥", "water": "💧", "coffee": "☕", "pizza": "🍕",
        # Tech & Work
        "python": "🐍", "code": "💻", "rocket": "🚀", "star": "⭐",
        "love": "❤️", "gift": "🎁", "party": "🥳"
    }

    print("--- 🚀 Professional Text-to-Emoji Engine Activated ---")
    time.sleep(0.5)
    print("Available keywords:", ", ".join(emoji_store.keys()))
    print("-" * 50)

    while True:
        user_input = input("\n Write your text or type 'exit' to leave: ").strip()

        # Exit condition
        if user_input.lower() == 'exit':
            print("Engine shutting down... Goodbye! 👋")
            break

        # Processing logic
        words = user_input.split()
        converted_list = []

        for word in words:
            # Punctuation hatane ke liye (optional par achha hai)
            clean_word = word.lower().strip(".,!?;:")
            
            # Dictionary check
            emoji = emoji_store.get(clean_word, word)
            converted_list.append(emoji)

        # Result ko join karna
        final_output = " ".join(converted_list)
        
        print(f"Original:  {user_input}")
        print(f"Converted: {final_output}")

# Program ko run karein
if __name__ == "__main__":
    text_to_emoji_pro()
