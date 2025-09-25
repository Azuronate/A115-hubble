#
# Nathan Parker | 9/25/25
#
#	Sources Used:
#		- Lecture V (Lists and Dictionaries)
#		- Lecture VII (Basic Data Formatting and matplotlib)
#		- 
#

import matplotlib.pyplot as plot

galaxies = [
    {"Name": "N2805", "x": 96, "y": 1736},
    {"Name": "N3348", "x": 149, "y": 2831},
    {"Name": "N3365", "x": 55, "y": 986},
    {"Name": "N3694", "x": 114, "y": 2279},
    {"Name": "N4004", "x": 160, "y": 3366},
    {"Name": "N4161", "x": 225, "y": 4941},
    {"Name": "N4459", "x": 61, "y": 1215},
    {"Name": "N4491", "x": 25, "y": 497},
    {"Name": "N4627", "x": 38, "y": 828},
    {"Name": "N4845", "x": 62, "y": 1232},
    {"Name": "N5195", "x": 29, "y": 558},
    {"Name": "N525",  "x": 77, "y": 1624},
    {"Name": "N5550", "x": 370, "y": 7404},
    {"Name": "N5671", "x": 451, "y": 9014},
    {"Name": "N5725", "x": 76, "y": 1601},
    {"Name": "N5940", "x": 564, "y": 10144},
    {"Name": "N6007", "x": 527, "y": 10548},
    {"Name": "N7189", "x": 438, "y": 9204},
    {"Name": "N7682", "x": 257, "y": 5134},
    {"Name": "N83",   "x": 350, "y": 6304},
]

# Galaxy coordinates
x_coords = [galaxy["x"] for galaxy in galaxies]
y_coords = [galaxy["y"] for galaxy in galaxies]

plot.scatter(x_coords, y_coords)
plot.xlabel("Distance in Million LY")
plot.ylabel("Radial Velocity (km/sec)")
plot.show()

print(x_coords, y_coords)
