print("Welcome to your personal Tip Calculator")

total_bill = float(input("What was the total bill? $"))

how_many_people = int(input("How many people are splitting the bill? "))

Tip_Percentage = int(input("How much do you want to Tip in Percent? 10, 12,or 15?\n"))

Tip_as_percent = Tip_Percentage / 100

Eventual_Tip = total_bill * Tip_as_percent

Final_tip = total_bill + Eventual_Tip

Group_bill = Final_tip / how_many_people


print(f"Each Bill paying participant has to pay  {Group_bill} !")

