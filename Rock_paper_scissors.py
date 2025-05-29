import random

user_points = 0
computer_points = 0

options = ["r", "p", "s"]

while True:
    user_choice = input("R to Rock, P to Paper, S to Scissors or Q to Quit: ").lower()

    if user_choice == 'q':
        break
    if user_choice not in options:
        print("Invalid option. Try again.")
        continue

    computer_choice = random.choice(options)

    print("The computer chose", computer_choice.upper())

    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("You win!")
        user_points += 1
    else:
        print("You lose!")
        computer_points += 1

    print(f"Score: You {user_points} - {computer_points} Computer\n")

print("Final Score: You =", user_points, "Computer =", computer_points)
print("Goodbye!")

    
