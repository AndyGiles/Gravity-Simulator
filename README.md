# Gravity-Simulator
A program using Python's 2D graphics module Pygame that simulates gravity physics between point masses.


To use, put both gravity.py, PlanetClass.py, and background.wav in the same directory, and run gravity.py. Make sure you have Pygame installed. 

The program will start off with a single large mass in the center of the screen. Click and drag to create a new point thats intitial velocity is proportional to the vector that you drew.

Press the space bar to start and pause the simulation.

Pressing 't' will toggle trails.

Pressing the up and down arrows will increase or decrease the value of G, the gravitational constant used in the simulation. A higher G value will make everything exert a greater force on the other bodies.

Pressing the left and right arrow keys will decrease or increase the mass of any new body that is created with the click and drag feature.

Pressing 'r' will reset the screen, so there will once again be a single large mass in the center. Pressing 'r' will not affect the trail state or pause state.
