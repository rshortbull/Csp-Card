import turtle
import time

# Create a wn object (window)
wn = turtle.Screen()

# Set the wn to full-screen (maximize)
wn.setup(width=wn.window_width(), height=wn.window_height())
wn.title("Fade Transition with Solid Colors")

# Initialize the original background color and the new color
original_color = "white"
new_color = "lightblue"
fade_color = "black"

# Function to simulate a fade transition from one color to another
def fade_transition(from_color, to_color, steps=6):
    # Convert color names to RGB values
    def color_to_rgb(color):
        if color == "black":
            return (0, 0, 0)
        elif color == "white":
            return (1, 1, 1)
        elif color == "lightblue":
            return (0.678, 0.847, 0.902)
        return (1, 1, 1)  # Default to white

    from_r, from_g, from_b = color_to_rgb(from_color)
    to_r, to_g, to_b = color_to_rgb(to_color)
    
    # Calculate the step size for each color component (R, G, B)
    step_r = (to_r - from_r) / steps
    step_g = (to_g - from_g) / steps
    step_b = (to_b - from_b) / steps

    # Gradually transition from the "from_color" to the "to_color"
    for i in range(steps):
        # Calculate the intermediate color values
        intermediate_r = from_r + step_r * i
        intermediate_g = from_g + step_g * i
        intermediate_b = from_b + step_b * i

        # Update the wn background color to the intermediate value
        wn.bgcolor(intermediate_r, intermediate_g, intermediate_b)

        # Pause for a short duration to create a fade effect
        time.sleep(0.05)

# Function to change the background color based on mouse click
def change_color(x, y):
    wn_width = wn.window_width()
    
    # Define left and right half boundaries
    left_boundary = -wn_width / 2
    right_boundary = wn_width / 2
    
    # Only fade to black if clicked on the left or right side
    if x > right_boundary / 1.3:  # Right half of the screen
        fade_transition(wn.bgcolor(), fade_color)
        fade_transition(fade_color, new_color)
    elif x < left_boundary / 1.3:  # Left half of the screen
        fade_transition(wn.bgcolor(), fade_color)
        fade_transition(fade_color, original_color)

# Set the initial background to the original color
wn.bgcolor(original_color)

# Bind the click event (clicking anywhere on the wn)
wn.onclick(change_color)

# Main loop
wn.mainloop()
