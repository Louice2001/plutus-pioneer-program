flashcards = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest ocean on Earth?": "Pacific",
}

score = 0
for question, answer in flashcards.items():
    user_answer = input(f"{question} ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {answer}.\n")

print(f"You got {score} out of {len(flashcards)} correct.")
