#!/usr/bin/env python3

import random
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Color Table</title>')
print('</head>')

# Generate RGB for random color
rand_red = random.randint(0, 255)
rand_green = random.randint(0, 255)
rand_blue = random.randint(0, 255)

# Lists to store the values of the RGB settings
red_config = [255,0,0]
green_config = [0,255,0]
blue_config = [0,0,255]

orange_config = [255,127,80]
purple_config = [147,112,219]
yellow_config = [255,255,0]

turq_config = [0,206,209]
maroon_config = [128,0,0]
random_config = [rand_red, rand_green, rand_blue]


print("""<body>
		<br/>
		<h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
		<h2 align="center"> Color Table </h2>
		<br/>
		<p align="center">
		<button type="button" align="left"   style="height:200px; width:200px; background:rgb(255,0,0); font-size:24px;">Red</button>
		<button type="button" align="center" style="height:200px; width:200px; background:rgb(0,255,0); font-size:24px;">Green</button>
		<button type="button" align="right"  style="height:200px; width:200px; background:rgb(0,0,255); font-size:24px;">Blue</button>
		</p>
		<p align="center">
                <button type="button" align="left"   style="height:200px; width:200px; background:rgb(255,127,80);  font-size:24px;">Orange</button>
                <button type="button" align="center" style="height:200px; width:200px; background:rgb(147,112,219); font-size:24px;">Purple</button>
                <button type="button" align="right"  style="height:200px; width:200px; background:rgb(255,255,0);   font-size:24px;">Yellow</button>
                </p>
	
		<p align="center">
                <button type="button" align="left"   style="height:200px; width:200px; background:rgb(0,206,209); font-size:24px;">Turquoise</button>
                <button type="button" align="center" style="height:200px; width:200px; background:rgb(128,0,0);   font-size:24px;">Maroon</button>
                <button type="button" align="right"  style="height:200px; width:200px; background:rgb(%d,%d,%d);  font-size:24px;">Random</button>
                </p>
                <br/>
                <p align="center">
                RNG Values for Random Color:<br/> 
                Red:   %d <br/>
                Green: %d <br/>
                Blue:  %d <br/>
                </p>
	</body>""" % (rand_red, rand_green, rand_blue, rand_red, rand_green, rand_blue))

print('</html>')
