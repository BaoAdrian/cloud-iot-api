#!/usr/bin/env python3

import MySQLdb
import random
import ip as ip
import cgitb
import cgi
cgitb.enable()

# Create HTML Environment and print header
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Color Table</title>')
print('</head>')

# Setup Connection to Database
conn = MySQLdb.connect( host 	= 'project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com',
			user 	= 'Admin',
			passwd 	= 'project2password',
			db 	= 'project2db')

# Setup cursor to query database
cursor = conn.cursor()

# Set up form
form = cgi.FieldStorage()

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

# Analyze the form and update database
r_conf = form["red"].value
g_conf = form["green"].value
b_conf = form["blue"].value
opacity = form["opacity"].value

cursor.execute("""UPDATE light_status SET red=%s, green=%s, blue=%s, opacity=%s;""",(r_conf, g_conf, b_conf, opacity))

# Print lightbulb
print("""<body>
	<center>
                <h1 style="color:rgb(%d,%d,%d)">""" % (int(r_conf), int(g_conf), int(b_conf)))
          
print("""<svg align="center" viewBox="0 0 60 55" preserveAspectRatio="xMidYMin slice" style="width: 30%; padding-bottom: 30%; height: 1px; overflow: visible">
  	<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb fa-w-11" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 352 512"><path fill-opacity="0.9" fill="currentColor" d="M96.06 454.35c.01 6.29 1.87 12.45 5.36 17.69l17.09 25.69a31.99 31.99 0 0 0 26.64 14.28h61.71a31.99 31.99 0 0 0 26.64-14.28l17.09-25.69a31.989 31.989 0 0 0 5.36-17.69l.04-38.35H96.01l.05 38.35zM0 176c0 44.37 16.45 84.85 43.56 115.78 16.52 18.85 42.36 58.23 52.21 91.45.04.26.07.52.11.78h160.24c.04-.26.07-.51.11-.78 9.85-33.22 35.69-72.6 52.21-91.45C335.55 260.85 352 220.37 352 176 352 78.61 272.91-.3 175.45 0 73.44.31 0 82.97 0 176zm176-80c-44.11 0-80 35.89-80 80 0 8.84-7.16 16-16 16s-16-7.16-16-16c0-61.76 50.24-112 112-112 8.84 0 16 7.16 16 16s-7.16 16-16 16z"></path></svg>
  	</svg>
	</svg>
	<h1/>
	<center/>""")


# Print Page Header
print("""<br/>
		<h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
		<h2 align="center"> Color Table </h2>
		<br/>

		<p align="center">""")

#Setup all buttons with their corresponding HTTP URLs

# Red
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="left" style="height:200px; width:200px; background:rgb(255,0,0); font-size:24px;">Red</button>""" % (ip.IP_ADDR,red_config[0], red_config[1], red_config[2], opacity))

# Green
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="center" style="height:200px; width:200px; background:rgb(0,255,0); font-size:24px;">Green</button>""" % (ip.IP_ADDR, green_config[0], green_config[1], green_config[2], opacity))

# Blue
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="right"  style="height:200px; width:200px; background:rgb(0,0,255); font-size:24px;">Blue</button> </p>""" % (ip.IP_ADDR, blue_config[0], blue_config[1], blue_config[2], opacity))

# Orange
print("""<p align="center">
         	<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="left"  style="height:200px; width:200px; background:rgb(255,127,80);  font-size:24px;">Orange</button>""" % (ip.IP_ADDR, orange_config[0], orange_config[1], orange_config[2], opacity))
         
# Purple       
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="center" style="height:200px; width:200px; background:rgb(147,112,219); font-size:24px;">Purple</button>""" % (ip.IP_ADDR, purple_config[0], purple_config[1], purple_config[2], opacity))
                
# Yellow
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="right"  style="height:200px; width:200px; background:rgb(255,255,0);   font-size:24px;">Yellow</button </p>""" % (ip.IP_ADDR, yellow_config[0], yellow_config[1], yellow_config[2], opacity))
        
# Turquoise        
print("""<p align="center">
                <button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="left"   style="height:200px; width:200px; background:rgb(0,206,209); font-size:24px;">Turquoise</button>""" % (ip.IP_ADDR, turq_config[0], turq_config[1], turq_config[2], opacity))
         
# Maroon
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="center" style="height:200px; width:200px; background:rgb(128,0,0);   font-size:24px;">Maroon</button>""" % (ip.IP_ADDR, maroon_config[0], maroon_config[1], maroon_config[2], opacity))
                
# Random
print("""<button type="button" onclick="window.location.href = 'http://%s/cgi-bin/color-table.py?red=%s&green=%s&blue=%s&opacity=%s'" align="right"  style="height:200px; width:200px; background:rgb(%d,%d,%d);  font-size:24px;">Random</button> </p>""" % (ip.IP_ADDR, random_config[0], random_config[1], random_config[2], opacity, rand_red, rand_green, rand_blue))

# Print Random Config numbers that were generated
print("""<br/>

                <p align="center">
                RNG Values for Random Color:<br/> 
                Red:   %d <br/>
                Green: %d <br/>
                Blue:  %d <br/>
                </p>


	</body>""" % (rand_red, rand_green, rand_blue))

print('</html>')


# Commit changes to Datbase and Cleanup
conn.commit()
cursor.close()
conn.close()



