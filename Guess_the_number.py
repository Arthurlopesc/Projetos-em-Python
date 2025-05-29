import random 

print("Welcome to Guess the Number")
choice_number = input ("Type a number:")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print('Please type a number!')
    quit()

random_number=random.randint(0,choice_number)

n_choices = 0

while True:
    answer_user = input("Guess the number:")
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Please type a number!")
        continue

    n_choices +=1

    if answer_user == random_number:
        print("Well done! You got it!")
        break
    elif answer_user > random_number:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Your number of attempts was:" + str(n_choices) )

