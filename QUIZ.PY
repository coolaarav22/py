def run_quiz(questions):
    score = 0
    for question_data in questions:
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["answer"]

        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        user_answer = input("Enter your answer (1, 2, 3, etc.): ")
        
        try:
            user_choice_index = int(user_answer) - 1
            if 0 <= user_choice_index < len(options) and options[user_choice_index] == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {correct_answer}\n")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to an option.\n")
        except IndexError:
            print("Invalid option number. Please choose from the given options.\n")

    print(f"Quiz finished! You scored {score} out of {len(questions)}.")

# Define your quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]

if __name__ == "__main__":
    print("Welcome to the Python Quiz!\n")
    run_quiz(quiz_questions)