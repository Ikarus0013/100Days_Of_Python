import random
from day7_wordList import word_list
from day7_stages import stages

computer_secret_word = random.choice(word_list)

#testing code
print(f'psst, the solution is {computer_secret_word}.')

lives = 6
display = []
word_length = len(computer_secret_word)

for _ in range(word_length):
    display += "_"   

#loop until user wins
end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()


    if user_guess in display:
        print("You have already guessed this letter, go again")

    for position in range(word_length):
        letter = computer_secret_word[position]
        #print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {user_guess}\n")
        if letter == user_guess:
            display[position] = letter

    if user_guess in display:
        lives = lives
        print(f"You have {lives} lives remaining ")
    elif user_guess not in display:
        lives = lives - 1
        print(f"You lost a life, you have {lives} lives remaining ")
        if lives == 0:
            print("bro you dump, you lost, play again mate")
            end_of_game = True

        
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    
    print(stages[lives])
    



#while "_" in display:
    
#    user_guess = input("Guess a letter: ").lower()

 #   for position in range(word_length):
  #      letter = computer_secret_word[position]
        #print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {user_guess}\n")
   #     if letter == user_guess:
    #        display[position] = letter
        
    #print(display)

#print("You have Won!")


#user_guess = input("Guess a letter: ").lower()

#guessed_letter = []

#for letter in computer_secret_word:
#    if user_guess == letter:
#        guessed_letter.append(user_guess)
#    else:
#        guessed_letter.append(blank)

#print(guessed_letter)

#computer_secret_word_letters = list(computer_secret_word)




