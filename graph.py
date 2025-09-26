#
# Nathan Parker | 9/25/25
#
#	Sources Used:
#		- Lecture V (Lists and Dictionaries)
#		- Lecture VII (Basic Data Formatting and matplotlib)
#		- 
#

import matplotlib.pyplot as plot
import numpy as np

galaxies = [
    {"name": "N2805", "x": 96, "y": 1736},
    {"name": "N3348", "x": 149, "y": 2831},
    {"name": "N3365", "x": 55, "y": 986},
    {"name": "N3694", "x": 114, "y": 2279},
    {"name": "N4004", "x": 160, "y": 3366},
    {"name": "N4161", "x": 225, "y": 4941},
    {"name": "N4459", "x": 61, "y": 1215},
    {"name": "N4491", "x": 25, "y": 497},
    {"name": "N4627", "x": 38, "y": 828},
    {"name": "N4845", "x": 62, "y": 1232},
    {"name": "N5195", "x": 29, "y": 558},
    {"name": "N525",  "x": 77, "y": 1624},
    {"name": "N5550", "x": 370, "y": 7404},
    {"name": "N5671", "x": 451, "y": 9014},
    {"name": "N5725", "x": 76, "y": 1601},
    {"name": "N5940", "x": 564, "y": 10144},
    {"name": "N6007", "x": 527, "y": 10548},
    {"name": "N7189", "x": 438, "y": 9204},
    {"name": "N7682", "x": 257, "y": 5134},
    {"name": "N83",   "x": 350, "y": 6304},
]

# Galaxy coordinates
x_coords = np.array([galaxy["x"] for galaxy in galaxies])
y_coords = np.array([galaxy["y"] for galaxy in galaxies])

slope, intercept = np.polyfit(x_coords, y_coords, 1)
regression = slope * x_coords + intercept

# Annotating galaxies on the graph
for i, galaxy in enumerate(galaxies):
	print(x_coords[i], y_coords[i])
	plot.annotate(galaxy["name"], xy=(x_coords[i], y_coords[i]))

# Lonely galaxy coordinates
plot.scatter(x_coords, y_coords, color="black")

# Linear Regression a/k/a "Best Fit Line" (wanted)
plot.plot(x_coords, regression, color="cyan", linestyle="--")

plot.xlabel("Distance in Million LY")
plot.xlim(0, 600)
plot.ylabel("Radial Velocity (km/sec)")
plot.ylim(0, 25000)
plot.grid(True)
plot.show()

print(x_coords, y_coords)
