import random
import time

class Question:
    def __init__(self, prompt, options, correct_answer, category):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer.upper()
        self.category = category

class QuizManager:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def display_welcome(self):
        print("=" * 50)
        print("       WELCOME TO THE ULTIMATE CHALLENGE")
        print("=" * 50)
        print(f"Total Questions: {len(self.questions)}")
        print("Rules: Enter A, B, C, or D. Good luck!\n")
        time.sleep(1)

    def get_valid_input(self):
        """Ensures the user only enters A, B, C, or D."""
        valid_choices = ['A', 'B', 'C', 'D']
        while True:
            user_input = input("Enter your choice: ").strip().upper()
            if user_input in valid_choices:
                return user_input
            print("Invalid input! Please enter A, B, C, or D.")

    def start_quiz(self):
        self.display_welcome()
        
        # Randomize question order
        random.shuffle(self.questions)

        for q in self.questions:
            self.question_index += 1
            print(f"CATEGORY: {q.category}")
            print(f"Question {self.question_index}: {q.prompt}")
            
            for option in q.options:
                print(option)

            user_answer = self.get_valid_input()

            if user_answer == q.correct_answer:
                print("✨ Correct! Well done.")
                self.score += 1
            else:
                print(f"❌ Incorrect. The right answer was {q.correct_answer}.")
            
            print(f"Current Score: {self.score}/{self.question_index}")
            print("-" * 30)
            time.sleep(0.5)

        self.show_final_results()

    def show_final_results(self):
        percentage = (self.score / len(self.questions)) * 100
        print("\n" + "=" * 50)
        print("                QUIZ FINISHED")
        print("=" * 50)
        print(f"Final Score: {self.score} out of {len(self.questions)}")
        print(f"Grade: {percentage:.1f}%")
        
        if percentage == 100:
            print("Perfect score! You're a genius! 🏆")
        elif percentage >= 70:
            print("Great job! You passed! 🎉")
        else:
            print("Better luck next time! 📚")
        print("=" * 50)

# --- Data Initialization ---

# Creating a list of Question Objects
question_bank = [
    Question(
        "Which planet is known as the Red Planet?",
        ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "B", "Science"
    ),
    Question(
        "Who wrote 'Romeo and Juliet'?",
        ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) J.K. Rowling"],
        "C", "Literature"
    ),
    Question(
        "What is the largest ocean on Earth?",
        ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "D", "Geography"
    ),
    Question(
        "What is the chemical symbol for Gold?",
        ["A) Gd", "B) Au", "C) Ag", "D) Fe"],
        "B", "Science"
    ),
    Question(
        "In what year did World War II end?",
        ["A) 1945", "B) 1939", "C) 1918", "D) 1950"],
        "A", "History"
    )
]

# --- Main Execution ---
if __name__ == "__main__":
    my_quiz = QuizManager(question_bank)
    my_quiz.start_quiz()
