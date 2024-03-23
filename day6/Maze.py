def turn_right():
    turn_left()
    turn_left()
    turn_left()


    
def force_right():
    while not is_facing_north():
        turn_left()
    turn_right()
    
force_right() 
while   front_is_clear():
    move()
turn_left()

while not at_goal():  
    while right_is_clear():
        turn_right()
        move()
    while (not right_is_clear() and front_is_clear()):
        move()
    while (not right_is_clear() and not front_is_clear()):
        turn_left()
    
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
