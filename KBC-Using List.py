# Kaun Banega Crorepati (KBC) in Python using Lists

questions = [
    "What is the capital of Pakistan?",
    "Which planet is known as the Red Planet?",
    "What is the color of our Flag?",
    "What is the national animal of Pakistan?",
    "Prime Minister of Pakistan?"
]

options = [
    ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Pindi"],
    ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
    ["A. Green and white", "B. Green and Yellow", "C. Red", "D. Blue"],
    ["A. Markhor", "B. Lion", "C. Elephant", "D. Leopard"],
    ["A. Imran Khan", "B. Nawaz Sharif", "C. Maryam Nawaz", "D. Zardari"]
]

answers = ["B", "C", "A", "A", "A"]

prize_money = [1000, 5000, 10000, 50000, 100000]
total_earned = 0

print("🎉 Welcome to Kaun Banega Crorepati (KBC) 🎉")
print("Answer the following questions:\n")

for i in range(len(questions)):
    print(f"Q{i + 1}: {questions[i]}")
    for option in options[i]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == answers[i]:
        total_earned += prize_money[i]
        print(f"✅ Correct! You've earned ₹{prize_money[i]}\n")
    else:
        print(f"❌ Wrong answer! The correct answer was {answers[i]}.")
        break

print(f"🏆 You won a total of ₹{total_earned}")
print("Thank you for playing Kaun Banega Crorepati!")

