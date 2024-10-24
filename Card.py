import turtle
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Spooky UFO Alien Music Loop _ REQUEST (1).mp3")
pygame.mixer.music.play(-1)


wn = turtle.Screen()

wn.setup(width=wn.window_width(), height=wn.window_height())
wn.title("E Card")
wn.bgpic("BG2.png")


wn.register_shape("cow.gif")
wn.addshape("ufo.gif")
wn.addshape("ufobeam.gif")
wn.addshape("flashlight.gif")
wn.addshape("kid.gif")

wn.addshape("frame 1.gif")
wn.addshape("frame 2.gif")
wn.addshape("frame 3.gif")
wn.addshape("frame 4.gif")
wn.addshape("frame 5.gif")

cow = turtle.Turtle()
cow.speed(0)
cow.setheading(90)
cow.shape("cow.gif")
cow.color("red")
cow.penup()
cow.goto(200,-50)

kid = turtle.Turtle()
kid.hideturtle()
kid.setheading(90)
kid.penup()
kid.shape("kid.gif")
kid.goto(650,-200)

ufobeam = turtle.Turtle()
ufobeam.hideturtle()
ufobeam.setheading(90)
ufobeam.penup()
ufobeam.shape("ufobeam.gif")
ufobeam.goto(198,1)
ufobeam.hideturtle

ufobeam2 = turtle.Turtle()
ufobeam2.hideturtle()
ufobeam2.setheading(90)
ufobeam2.penup()
ufobeam2.shape("ufobeam.gif")
ufobeam2.goto(650,0)


ufo = turtle.Turtle()
ufo.hideturtle
ufo.speed(0)
ufo.setheading(90)
ufo.shape("ufo.gif")
ufo.penup()
ufo.goto(500,500)
ufo.speed(1)

ufo = turtle.Turtle()
ufo.hideturtle()
ufo.speed(0)
ufo.setheading(90)
ufo.shape("ufo.gif")
ufo.penup()
ufo.goto(500,500)
ufo.speed(1)

flashlight = turtle.Turtle()
flashlight.hideturtle()
flashlight.speed(0)
flashlight.setheading(90)
flashlight.shape("flashlight.gif")
flashlight.penup()
flashlight.goto(360,435)

frame1 = turtle.Turtle()
frame1.hideturtle()
frame1.speed(0)
frame1.setheading(90)
frame1.shape("frame 1.gif")
frame1.penup()
frame1.goto(-300,-200)

frame2 = turtle.Turtle()
frame2.hideturtle()
frame2.speed(0)
frame2.setheading(90)
frame2.shape("frame 2.gif")
frame2.penup()
frame2.goto(-300,-200)

frame3 = turtle.Turtle()
frame3.hideturtle()
frame3.speed(0)
frame3.setheading(90)
frame3.shape("frame 3.gif")
frame3.penup()
frame3.goto(-300,-200)

frame4 = turtle.Turtle()
frame4.hideturtle()
frame4.speed(0)
frame4.setheading(90)
frame4.shape("frame 4.gif")
frame4.penup()
frame4.goto(-300,-200)

frame5 = turtle.Turtle()
frame5.hideturtle()
frame5.speed(0)
frame5.setheading(90)
frame5.shape("frame 5.gif")
frame5.penup()
frame5.goto(-300,-200)


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

def move_sign():
    # sets up sign
    sign = turtle.Turtle()
    sign.fillcolor("black")
    sign.speed(0)
    sign.pensize(5)
    sign.pencolor("green")
    sign.goto(-450, 300)
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

    sign.hideturtle()
    

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

# Bind the cow turtle to respond to clicks
cow.onclick(move_ufo)

def move_ufo_kid():
    ufo.showturtle()  
    ufo.goto(650,180)  
    time.sleep(0.5)
    ufobeam2.showturtle()
    time.sleep(1)
    kid.hideturtle() 
    ufobeam2.hideturtle()


def lastcut(x, y):

    move_ufo_kid()

    # WALK CYCLE
    x = 1
    step_size = 45  # Adjust this value for how far the animation should move each step
    kid.hideturtle()
    while x in range(10):
        # Move frames forward
        for frame in [frame1, frame2, frame3, frame4,frame5,flashlight]:
            frame.setx(frame.xcor() + step_size)  # Move frame forward

        frame1.showturtle()
        frame4.hideturtle()
        time.sleep(0.1)
        frame2.showturtle()
        frame1.hideturtle()
        time.sleep(0.1)
        frame3.showturtle()
        frame2.hideturtle()
        time.sleep(0.1)
        frame4.showturtle()
        frame3.hideturtle()
        time.sleep(0.1)

        x += 1

    frame5.showturtle()
    frame1.hideturtle()
    frame2.hideturtle()
    frame3.hideturtle()
    frame4.hideturtle()
    flashlight.showturtle()
    time.sleep(1)
    move_sign()

kid.onclick(lastcut)
# walkcycle()
cow.onclick(move_ufo)

click_cooldown = False

def change_color(x, y):
    global click_cooldown
    
    # Check if we're still in the cooldown period
    if click_cooldown:
        return

    wn_width = wn.window_width()
    
    # Define left and right half boundaries
    left_boundary = -wn_width / 2
    right_boundary = wn_width / 2
    
    # Change background based on the clicked area
    if x > right_boundary / 1.3:  # Right half of the screen
        wn.bgpic("BG1.png")
        cow.hideturtle()
        kid.showturtle()
        
    elif x < left_boundary / 1.3:  # Left half of the screen
        wn.bgpic("BG2.png")
        cow.hideturtle()

        

    
    # Set cooldown
    click_cooldown = True
    
    # Wait for a short period
    time.sleep(0.5)
    
    # Reset cooldown
    click_cooldown = False

wn.onclick(change_color)  # Call change_color on click



# Main loop
wn.mainloop()
