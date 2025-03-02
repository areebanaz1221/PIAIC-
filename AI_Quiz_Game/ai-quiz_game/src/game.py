import random
from src.questions import questions
from src.animation import show_loading_animation

def play_quiz():
    print("🤖 Welcome to the AI Quiz Game! 🤖")
    print("~" * 50)
    show_loading_animation()

    random.shuffle(questions)

    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\nCalculating Results...")
    show_loading_animation()

    print(f"\n🎉 Your Final Score: {score}/10")

    if score == 10:
        print("🔥 Excellent! You are an AI Master.")
    elif score >= 7:
        print("👍 Good Job! Strong AI knowledge.")
    elif score >= 5:
        print("🙂 Not bad! Keep learning.")
    else:
        print("😅 Time to study AI basics again!")

    print("\nThanks for playing the AI Quiz Game! 😊")
    print("~" * 50)
