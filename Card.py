import turtle
import time


wn = turtle.Screen()

wn.setup(width=wn.window_width(), height=wn.window_height())
wn.title("E Card")
wn.bgpic("BG2.png")


wn.register_shape("coww.gif")
wn.addshape("ufo.gif")


cow = turtle.Turtle()
cow.speed(0)
cow.setheading(90)
cow.shape("coww.gif")
cow.color("red")
cow.penup()
cow.goto(200,-50)

ufo = turtle.Turtle()
ufo.hideturtle
ufo.speed(0)
ufo.setheading(90)
ufo.shape("ufo.gif")
ufo.penup()
ufo.goto(500,500)
ufo.speed(1)


def move_ufo(x, y):
    ufo.showturtle()  
    ufo.goto(200, 150)  
    time.sleep(1) 
    cow.hideturtle() 
    ufo.goto(500, 500)  
    ufo.hideturtle() 

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
