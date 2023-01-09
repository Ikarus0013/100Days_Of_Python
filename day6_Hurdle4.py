# Reeborgs World / reborg.ca/reborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def instant_jump():
    while wall_on_right() and wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            move()
        elif not wall_in_front():
            move()
        else:
            turn_left()
            turn_left()
            move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        instant_jump()

