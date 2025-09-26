#
# Nathan Parker | 9/25/25
#
#	Sources Used:
#		- A115 Week 5 Exploration's New General Catalog (NGC) of non-stellar objects
#		- CSCI-H 200 Lecture V (Lists and Dictionaries)
#		- CSCI-H 200 Lecture VII (Basic Data Formatting and matplotlib)
#		- https://matplotlib.org/stable/ (Docs)
#

import matplotlib.pyplot as plot
import numpy as np

IS_LABELED = False

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

print(slope)

# Annotating galaxies on the graph
if IS_LABELED != False:
	for i, galaxy in enumerate(galaxies):
		print(x_coords[i], y_coords[i])
		plot.annotate(galaxy["name"], xy=(x_coords[i], y_coords[i]))

# Lonely galaxy coordinates
plot.scatter(x_coords, y_coords, color="hotpink", label="Galaxy")

# Linear Regression a/k/a "Best Fit Line" (wanted)
plot.plot(x_coords, regression, color="black", linestyle="--", label="Hubble's Constant (Regression)")

# General velocity lines (given)
velocities = [
	{"name": "40 km/s per million LY", "color": "red", "m": 40, "b": 0},
	{"name": "30 km/s per million LY", "color": "yellow", "m": 30, "b": 0},
	{"name": "20 km/s per million LY", "color": "green", "m": 20, "b": 0},
	{"name": "10 km/s per million LY", "color": "blue", "m": 10, "b": 0},
	{"name": "5 km/s per million LY", "color": "darkmagenta", "m": 5, "b": 0},
]

x = np.linspace(0,600)
for line in velocities:
	y = line["m"] * x + line["b"]
	plot.plot(x, y, color=line["color"], linestyle="-", label=line["name"])

plot.title(f"Estimating Hubble's Constant: ~{round(slope, 3)}km/s per MLY \nBy: Nathan Parker", fontsize=10)
plot.xlabel("Distance in Million LY")
plot.xlim(0, 600)
plot.ylabel("Radial Velocity (km/sec)")
plot.ylim(0, 25000)
plot.grid(True)
plot.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0., fancybox=True, shadow=True)
plot.subplots_adjust(right=0.55)
plot.show()