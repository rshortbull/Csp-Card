import turtle
import time


wn = turtle.Screen()

wn.setup(width=wn.window_width(), height=wn.window_height())
wn.title("E Card")
wn.bgpic("BG2.png")


wn.register_shape("cow.gif")
wn.addshape("ufo.gif")
wn.addshape("ufobeam.gif")

# sets up sign
sign = turtle.Turtle()
sign.fillcolor("black")
sign.speed(0)
sign.pensize(5)
sign.pencolor("orange")
sign.begin_fill()
sign.penup()
sign.goto(-950, 520)
sign.pendown()




# creates sign
for rectangle in range(2):
    sign.forward(270)
    sign.right(90)
    sign.forward(150)
    sign.right(90)
sign.end_fill()




sign.penup()
sign.goto(-933, 400)
sign.pendown()
sign.color('orange')
style = ('Times New Roman', 13, 'normal')
sign.write(
    'Instructions: \n'
    '1. Click around to explore \n'
    'the area.\n'
    '2. After all has been clicked, \n'
    'click the right side to the next scene.',
    font=style)
sign.hideturtle()





cow = turtle.Turtle()
cow.speed(0)
cow.setheading(90)
cow.shape("cow.gif")
cow.color("red")
cow.penup()
cow.goto(200,-50)

ufobeam = turtle.Turtle()
ufobeam.hideturtle()
ufobeam.setheading(90)
ufobeam.penup()
ufobeam.shape("ufobeam.gif")
ufobeam.goto(198,1)
ufobeam.hideturtle

ufo = turtle.Turtle()
ufo.hideturtle()
ufo.speed(0)
ufo.setheading(90)
ufo.shape("ufo.gif")
ufo.penup()
ufo.goto(500,500)
ufo.speed(1)


def move_ufo(x, y):
    ufo.showturtle()  
    ufo.goto(200, 150)  
    time.sleep(0.5)
    ufobeam.showturtle()
    time.sleep(1)
    cow.hideturtle() 
    ufobeam.hideturtle()
    ufo.goto(500, 500)
    ufo.hideturtle() 

def move_sign():
    # sets up sign
    sign = turtle.Turtle()
    sign.fillcolor("black")
    sign.speed(0)
    sign.pensize(5)
    sign.pencolor("green")
    sign.begin_fill()
    sign.penup()
    sign.pendown()


    # creates sign
    for rectangle in range(2):
        sign.forward(970)
        sign.right(90)
        sign.forward(550)
        sign.right(90)
    sign.end_fill()


    sign.penup()
    sign.goto(-360, -40)
    sign.pendown()
    sign.color('Green')
    style = ('Times New Roman', 50, 'normal')
    sign.write(
        'HAPPY ALIEN ABDUCTION \n'
        '                  DAY!!',
        font=style)

    sign.goto(-450, -300)
    sign.goto(-450, 300)





# Bind the cow turtle to respond to clicks
cow.onclick(move_ufo)

def change_color(x, y):
    wn_width = wn.window_width()
    
    # Define left and right half boundaries
    left_boundary = -wn_width / 2
    right_boundary = wn_width / 2
    
    # Only fade to black if clicked on the left or right side
    if x > right_boundary / 1.3:  # Right half of the screen
        wn.bgpic("BG1.png")
        cow.hideturtle()
    elif x < left_boundary / 1.3:  # Left half of the screen
        wn.bgpic("BG2.png")
        cow.showturtle()

# Bind the click event (clicking anywhere on the wn)
wn.onclick(change_color)


# Main loop
wn.mainloop()


