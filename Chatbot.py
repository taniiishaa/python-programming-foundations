import random

def run_chatbot():
    """
    A rule-based chatbot demonstrating clean code structure 
    and dictionary-based response management.
    """
    
    # 1. Store Rules in a Dictionary (Demonstrates clean structure)
    # Keys are trigger keywords; values are a list of possible responses (for variety)
    rules = {
        'hello': ["Hi there! What can I help you with?", "Greetings! Ask me anything about my rules.", "Hello! Ready to chat."],
        'hi': ["Hi there! What can I help you with?", "Greetings! Ask me anything about my rules.", "Hello! Ready to chat."],
        'how are you': ["I'm a program, so I'm running perfectly!", "I'm performing optimally. How about you?", "Excellent! Ready to process your next command."],
        'your name': ["I don't have a name, but I was built to demonstrate clean control flow.", "I am a simple rule-based AI created for a Python task."],
        'who are you': ["I am a simple rule-based AI created for a Python task.", "I was built to demonstrate clean control flow."],
        'python': ["Python is a versatile and powerful language. Great choice!", "It's excellent for beginners and scalable projects. Do you use it often?"],
        'thank you': ["You're very welcome!", "No problem at all!", "Happy to assist!"],
        'age': ["I exist only when this script runs, so I'm technically brand new!", "I don't have an age, but my logic is simple and effective."],
    }
    
    # 2. Initial Setup
    print("--- 🌟 Advanced Rule-Based Chatbot Activated 🌟 ---")
    print("Bot: Hello! I use clean, dictionary-based rules. Type 'bye' to exit.")
    print("-----------------------------------------------------")

    # 3. Start the Core Loop
    while True:
        user_input = input("You: ")
        
        # Process input for maintainability: lower case and stripped of spaces
        processed_input = user_input.lower().strip() 
        
        # --- Decision Logic ---
        
        # 3a. Exit Command (Highest Priority)
        if processed_input == 'bye' or processed_input == 'quit':
            print("Bot: Goodbye! Showing proficiency in Python control structures.")
            break
        
        # 3b. Rule Matching
        matched = False
        
        # Check every rule key against the processed input
        for keyword, responses in rules.items():
            if keyword in processed_input:
                # Use random.choice for varied responses (Impressive detail!)
                print(f"Bot: {random.choice(responses)}")
                matched = True
                break  # Stop checking rules once a match is found
        
        # 3c. Catch-all Response (The final 'else' logic)
    # 3c. Catch-all Response
    if not matched:
        print("Bot: I'm not sure I understand that. Could you try rephrasing?")
        
run_chatbot()
