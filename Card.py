import turtle
import time


wn = turtle.Screen()

wn.setup(width=wn.window_width(), height=wn.window_height())
wn.title("E Card")
wn.bgpic("BG2.png")


def change_color(x, y):
    wn_width = wn.window_width()
    
    # Define left and right half boundaries
    left_boundary = -wn_width / 2
    right_boundary = wn_width / 2
    
    # Only fade to black if clicked on the left or right side
    if x > right_boundary / 1.3:  # Right half of the screen
        wn.bgpic("BG1.png")
    elif x < left_boundary / 1.3:  # Left half of the screen
        wn.bgpic("BG2.png")

# Bind the click event (clicking anywhere on the wn)
wn.onclick(change_color)


# Main loop
wn.mainloop()
