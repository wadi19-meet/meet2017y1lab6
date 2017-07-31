
import turtle
def up():
    global direction
    direction=UP
    print('you moved up')
def down():
    global direction
    direction=DOWN
    print('you moved down')
def left():
    global direction
    direction=LEFT
    print('you moved left')
def right():
    global direction
    direction=RIGHT
    print('you moved right')




#################################################################



import turtle
UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction=UP

##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('shape')
##square.penup()
##square.goto(100,100)
##square.pendown()
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.onkeypress
turtle.onkeypress
