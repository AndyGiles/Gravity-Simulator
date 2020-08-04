# Gravity-Simulator
A program using Python's 2D graphics module Pygame that simulates gravity physics between point masses.


To use, put both gravity.py and PlanetClass.py in the same directory, and run gravity.py. Make sure you have Pygame installed. 

The program will start off with a single large mass in the center of the screen. Click and drag to create a new point that's intitial velocity is proportional to the vector that you drew.

Press the space bar to start and pause the simulation.

Pressing 'c' will center the screen on the largest mass, and pressing 'm' will put you in the reference frame of the largest mass, so you can essentially get the camera to match its speed and follow the system.

Pressing 't' will toggle trails.

Pressing the up and down arrows will increase or decrease the value of G, the gravitational constant used in the simulation. A higher G value will make everything exert a greater force on the other bodies.

Pressing the left and right arrow keys will increase the mass of any new body that is created with the click and drag feature.
