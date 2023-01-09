#age tiers
#<13
#13-17
#18
#>65
#height
#113cm

print("Welcome to your absolute favorite Rollercoaster!")

height = int(input("Stand by the Height-Pole and tell me how tall you are in cm: "))

if height >= 113:
    print("You are allowed on the ride")
    age = int(input("How old are you? "))
    if age < 13:
        print("Taking the ride costs you 5€")
    if age <= 18:
        print("Taking the ride costs you 10€ ")
    if age >= 19:
        print("Takig the ride costs you 23€")
    if age >= 65:
        print("Taking the ride costs you 1€")
else:
    print("Sorry, you are to small to take the Ride")



