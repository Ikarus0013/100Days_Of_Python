import random


rock = "👊🏾"

paper = "🧻"

scissors = "✄"

game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors!\n"))
if user_choice >= 3 or user_choice < 0:
    print("Wrong Number mate")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer Choose: ")
    print(game_image[computer_choice])



    print(f"Computer Chose {computer_choice}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("Its a Draw, play again")



