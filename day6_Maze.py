def turn_right():
    turn_left()
    turn_left()
    turn_left()

def stay_right():
    while front_is_clear():
        move()
        if wall_in_front() and wall_on_right():
            turn_left()
        elif at_goal():
            done()
        else:
            turn_right()
    while wall_in_front():
        turn_left()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_left()

def correct():
    if right_is_clear():
        turn_right()
    else:
        turn_left()

def correct_empty():
    while front_is_clear() and right_is_clear():
        move()
        turn_right()
        if wall_on_right():
            move()
            turn_right()
        elif wall_in_front():
            turn_left()
        else:
            move()

while not at_goal():
    if wall_on_right():
        stay_right()
    elif wall_in_front():
        correct()
    else:
        correct_empty()