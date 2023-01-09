print("Welcome to treasure Island")
print("Your Mission is to find the treasure")

decision1 = input('You are standing infront of a Wall, go "left" or "right"? ').lower()

if decision1 == "left":
    decision2 = input('Are you going for a "swim" or "wait"?' ).lower()
    if decision2 == "wait":
        decision3 = input('You ran for miles and are standing infront of a "Red", "Blue", and "Yellow" door, which onne will it be?' ).lower()
        if decision3 == "Blue":
            print("You are save, happy days!")
        elif decision3 == "Yellow":
            print("You fell down a hole and shattered into a million pieces")
        elif decision3 == "Red":
            print("Nahh Bruudda you dead")
    else: 
        print("You idiot .. an Allagotor eat you in 5 min time weak ass prick")
else:
    print("you are dead mofo Game Over")

