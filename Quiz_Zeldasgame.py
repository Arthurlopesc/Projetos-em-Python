
print("Welcome to Zelda's Quiz")

answer_user=input("Shall we start? (Y/N)")

if answer_user.upper() != "Y":
    quit()
print("Starting...")

score = 0 

#Question 01
print("Who developed Zelda's game? \n (a)Rockstar games \n (b)Nintendo \n(c)Ubisoft ")
answer_1 = input("Type your answer: ")

if answer_1.lower() == "c":
    print("Correct!")
    score = score + 1 
else:
    print("Incorrect!")

#Question 02
print(" What is the name of the main character in Zelda?\n (a)Link \n (b)Zelda \n(c)Ganondorf")

answer_2 = input("Type your answer: ")

if answer_2.lower() == "a":
    print("Correct!")
    score  +=1 
else:
    print("Incorrect!The main character is Link. Zelda is the princess!")

#Question 03
print("What is the name of the evil king in many Zelda games?\n (a)Bowser \n (b)Ganon \n(c)Ridley")

answer_3 = input("Type your answer: ")

if answer_3.lower() == "b":
    print("Correct!")
    score  +=1 
else:
    print("Incorrect! The correct answer is Ganon.")


#Question 04
print("What item is often used to solve puzzles in dungeons?\n (a)Sword \n (b)Bow \n(c)Boomerang")

answer_4 = input("Type your answer: ")

if answer_4.lower() == "c":
    print("Correct!")
    score  +=1 
else:
    print("Incorrect! The Boomerang is often used to trigger switches or hit distant objects.")

print(" In which kingdom does most of the Zelda series take place?\n (a)Hyrule \n (b)Kakariko \n(c)Midgar")


#Question 05
answer_5 = input("Type your answer: ")

if answer_5.lower() == "a":
    print("Correct!")
    score  +=1 
else:
    print("Incorrect! The correct answer is Hyrule.")

#Final Score
print("You finished the Quiz!")
print(f"Your score was: {score}/5")
if score == 5:
    print("You're a true Zelda master!")
elif score >= 3:
    print("Nice job! You know your Zelda lore.")
else:
    print("Keep playing! There’s a lot more to discover in Hyrule.")


