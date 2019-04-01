#!/usr/bin/env python3

import MySQLdb
import random
import ip as ip
import cgitb
import cgi
cgitb.enable()



form = cgi.FieldStorage()

# Setup Connection to Database
conn = MySQLdb.connect( host    = 'project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com',
                        user    = 'Admin',
                        passwd  = 'project2password',
                        db      = 'project2db')

# Setup cursor to query database
cursor = conn.cursor()

# Create html document and print title/header
print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print("""<html>
		<head>
			<title> House Simulator </title>
		</head>
		<body>
			<br/>
			<h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
			<h2 align="center"> House Simulator </h2>
			""")


# Pull the status from the FORM
location = form["location"].value
r_conf = form["red"].value
g_conf = form["green"].value
b_conf = form["blue"].value

# Execute UPDATE on database (note that it is a string)
cursor.execute("""UPDATE windows SET red=%s,green=%s,blue=%s WHERE location=%s""",(r_conf, g_conf, b_conf, location))

# Print the house
print("""
	<div style="text-align:center;">
	<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1650 1080" style="margin-top:-90px; enable-background:new 0 0 1920 1080; width:70%;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#603813;}
	.st1{fill:none;stroke:#000000;stroke-miterlimit:10;}
	.st2{fill:#0000FF;}
	.st3{fill:#00FF00;}
	.st4{fill:#F7931E;}
	.st5{fill:#29ABE2;}
	.st6{fill:#FF0000;}
	.st7{fill:#666666;}
	.st8{fill:none;stroke:#000000;stroke-width:4;stroke-miterlimit:10;}
	.st9{fill:none;stroke:#000000;stroke-width:5;stroke-miterlimit:10;}
</style>
<g>
	<rect x="459.5" y="424.5" width="702" height="469"/>
	<path d="M1161,425v468H460V425H1161 M1162,424H459v470h703V424L1162,424z"/>
</g>
<g>
	<polygon points="460.11,421.5 810.35,137.64 1160.59,421.5 	"/>
	<path d="M810.35,138.29L1159.18,421H461.52L810.35,138.29 M810.35,137L458.7,422H1162L810.35,137L810.35,137z"/>
</g>
<g>
	<rect x="919.5" y="177.5" width="75" height="152"/>
	<path d="M994,178v151h-74V178H994 M995,177h-76v153h76V177L995,177z"/>
</g>
<g>
	<rect x="779" y="772" class="st0" width="64" height="122"/>
</g>
<g>
	<line class="st1" x1="810.5" y1="781.5" x2="810.5" y2="893.5"/>
</g>
<g>
	<line class="st1" x1="810.5" y1="781.5" x2="810.5" y2="771.5"/>
</g>
<g>
	<line class="st1" x1="778.5" y1="832.5" x2="842.5" y2="832.5"/>
</g>
<g>
	<rect x="540.5" y="478.5" class="st2" width="125" height="125"/>
	<path d="M665,479v124H541V479H665 M666,478H540v126h126V478L666,478z"/>
</g>
<g>
	<rect x="540.5" y="675.5" class="st3" width="125" height="125"/>
	<path d="M665,676v124H541V676H665 M666,675H540v126h126V675L666,675z"/>
</g>
<g>
	<rect x="950.5" y="479.5" class="st4" width="125" height="125"/>
	<path d="M1075,480v124H951V480H1075 M1076,479H950v126h126V479L1076,479z"/>
</g>
<g>
	<rect x="952.5" y="677.5" class="st5" width="125" height="125"/>
	<path d="M1077,678v124H953V678H1077 M1078,677H952v126h126V677L1078,677z"/>
</g>
<g>
	<rect x="746.5" y="556.5" class="st6" width="127" height="177"/>
	<path d="M873,557v176H747V557H873 M874,556H746v178h128V556L874,556z"/>
</g>
<g>
	<polygon class="st7" points="732.46,556.5 809.62,479.21 886.79,556.5 	"/>
	<path d="M809.62,479.92L885.59,556H733.66L809.62,479.92 M809.62,478.5L731.25,557H888L809.62,478.5L809.62,478.5z"/>
</g>
<g>
	<line class="st8" x1="809.5" y1="555.5" x2="810.5" y2="733.5"/>
</g>
<line class="st8" x1="746.5" y1="644.5" x2="873.5" y2="644.5"/>
<line class="st9" x1="602.5" y1="478.5" x2="602.5" y2="603.5"/>
<line class="st9" x1="539.5" y1="539.5" x2="665.5" y2="539.5"/>
<g>
	<line class="st9" x1="1012.5" y1="478.5" x2="1012.5" y2="604.5"/>
</g>
<line class="st9" x1="949.5" y1="541.5" x2="1075.5" y2="541.5"/>
<line class="st9" x1="1012.5" y1="676.5" x2="1012.5" y2="800.5"/>
<line class="st8" x1="951.5" y1="739.5" x2="1075.5" y2="739.5"/>
<line class="st9" x1="602.5" y1="676" x2="602.5" y2="801"/>
<line class="st9" x1="538" y1="738.5" x2="664" y2="738.5"/>
<line class="st1" x1="746" y1="556" x2="874" y2="557"/>
</svg></div></body></html>""")


# Commit changes to Datbase and Cleanup
conn.commit()
cursor.close()
conn.close()


