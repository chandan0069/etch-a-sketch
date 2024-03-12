# Sketch Maker

This Python script allows users to create sketches using the Turtle module. Users can control the movement of the turtle, drawing lines as it moves, and clear the canvas to start anew.

## Description

The script sets up a Turtle object named `mnk` on a graphical window using the Turtle module. Users can control the turtle's movement using the following keys:

- **W / Up Arrow**: Move the turtle forward.
- **S / Down Arrow**: Move the turtle backward.
- **A / Left Arrow**: Turn the turtle left.
- **D / Right Arrow**: Turn the turtle right.
- **C**: Clear the canvas.

Users can adjust the movement step size and turn angle by modifying the parameters passed to the `forward()` and `setheading()` functions, respectively.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the script file `sketch_maker.py`.
3. Run the script using the command `python sketch_maker.py`.
4. Use the specified keys to control the turtle and create your sketch.
5. Press 'C' to clear the canvas and start over.

## Features

- **Customizable Controls**: Users can define their own key bindings for controlling the turtle's movement and clear function.
- **Interactive Canvas**: The Turtle graphics window provides immediate visual feedback, allowing users to see their sketches as they draw.
- **Efficient Clearing**: The script efficiently clears the canvas and resets the turtle's position for a seamless sketching experience.

## Requirements

- Python 3.x
- Turtle module (usually bundled with standard Python distributions)

