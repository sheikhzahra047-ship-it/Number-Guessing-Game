import random

print("🎮 Number Guessing Game")
print("Guess number between 1 to 10")

secret = random.randint(1, 10)

guess = int(input("Enter your guess: "))

if guess == secret:
    print("🎉 Correct! You Win")
elif guess > secret:
    print("📉 Too High! Try again")
else:
    print("📈 Too Low! Try again")

print("Secret number was:", secret)
