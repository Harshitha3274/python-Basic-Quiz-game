
quiz_game = [
    {
        "question": "Who is known as missile man of india?",
        "options": ["A) Abdul kalam", "B) Mahatma Gandhi", "C) Subash chandra Bose", "D) Sardar vallabhai patel"],
        "answer": "A"
    },
    {
        "question": "How many days does it take for the Earth to orbit the Sun?",
        "options": ["A) 365", "B) 500", "C) 1000", "D) 800"],
        "answer": "A"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["A) 9", "B) 7", "C) 6", "D) 5"],
        "answer": "B"
    }
]
def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").upper()
    return answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.")
        return False
def run_quiz(quiz_game):
    score = 0
    for question in quiz_game:
        user_answer = ask_question(question)
        if user_answer in ['A', 'B', 'C', 'D']:
            if check_answer(user_answer, question["answer"]):
                score += 1
        else:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = ask_question(question)
            if check_answer(user_answer, question_data["answer"]):
                score += 1
    
    print(f"\nYour final score is {score}/{len(quiz_game)}") 

run_quiz(quiz_game)    