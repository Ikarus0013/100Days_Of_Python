import math

def paint_calc(height, width, cover):
    number_of_cans = height * width
    final_amount_of_cans = math.ceil(number_of_cans / cover)
    print(f"You will need {final_amount_of_cans} cans, in order to paint your wall")


test_h = int(input("Height of Wall: "))
test_w = int(input("Width of Wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


