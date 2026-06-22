import random

max_attempts = 12
while True:
    guess = int(input("Pick a number from one to ten."))
    AI_p = random.randint(1, 10)
    print(AI_p)
    if guess:
        max_attempts -= 1
        if max_attempts == 0:
            print("Game Over")
    if guess == AI_p:
        print("Wow you are correct!!!")
    if guess == AI_p:
        print("Wow you are really good at this.")
    elif guess > 10 or guess < 0:
        print("Invalid guess.")
    else:
        print("Better luck next time.")



















