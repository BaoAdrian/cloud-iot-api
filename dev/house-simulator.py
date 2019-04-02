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
			<h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
			<h2 align="center"> House Simulator </h2>
			""")



# Set default values prior to pulling from URL
location = "all"
r_conf = 0
g_conf = 0
b_conf = 0

# Pull the status from the FORM if the exist
if "location" in form:
	location = form["location"].value

if "red" in form:
	r_conf = form["red"].value

if "green" in form:
	g_conf = form["green"].value

if "blue" in form:
	b_conf = form["blue"].value


# Used by welcome script to initialize house with all white windows
if location == "all":
	# Execute UPDATE on database (note that it is a string)
        cursor.execute("""UPDATE windows SET red=%s,green=%s,blue=%s;""",(r_conf, g_conf, b_conf))
else:
	# Execute UPDATE on database (note that it is a string)
	cursor.execute("""UPDATE windows SET red=%s,green=%s,blue=%s WHERE location=%s;""",(r_conf, g_conf, b_conf, location))


# Commit updated changes 
conn.commit()

# Query DB for required values to generate windows
top_left = [0,0,0] 	# st2
top_right = [0,0,0]	# st4
bottom_left = [0,0,0]	# st3
bottom_right = [0,0,0]	# st5
middle = [0,0,0]	# st6

cursor.execute("""SELECT * FROM windows;""")

# Using fetchall(), pull the individual colors for each window
for row in cursor.fetchall():
	if str(row[0]) == "top-left":
		top_left[0] = int(row[1])
		top_left[1] = int(row[2])
		top_left[2] = int(row[3])
	elif str(row[0]) == "top-right":
		top_right[0] = int(row[1])
		top_right[1] = int(row[2])
		top_right[2] = int(row[3])
	elif str(row[0]) == "bottom-left":
		bottom_left[0] = int(row[1])
		bottom_left[1] = int(row[2])
		bottom_left[2] = int(row[3])
	elif str(row[0]) == "bottom-right":
		bottom_right[0] = int(row[1])
		bottom_right[1] = int(row[2])
		bottom_right[2] = int(row[3])
	elif str(row[0]) == "middle":
		middle[0] = int(row[1])
		middle[1] = int(row[2])
		middle[2] = int(row[3])

# Print the house
print("""
	<div style="text-align:center;">
	<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1650 1080" style="margin-top:-75px; margin-bottom:-100px; enable-background:new 0 0 1920 1080; width:70%;" xml:space="preserve">""")

print("""<style type="text/css">
	.st0{fill:#603813;}
	.st1{fill:none;stroke:#000000;stroke-miterlimit:10;}
	.st2{fill:rgb(%d,%d,%d);}
	.st3{fill:rgb(%d,%d,%d);}
	.st4{fill:rgb(%d,%d,%d);}
	.st5{fill:rgb(%d,%d,%d);}
	.st6{fill:rgb(%d,%d,%d);}
	.st7{fill:#666666;}
	.st8{fill:none;stroke:#000000;stroke-width:4;stroke-miterlimit:10;}
	.st9{fill:none;stroke:#000000;stroke-width:5;stroke-miterlimit:10;}
	.st10{fill:#FFFFFF;}
	.st11{font-family:'ArialMT';}
	.st12{font-size:23.5751px;}
	.st13{fill:none;stroke:#666666;stroke-width:5;stroke-miterlimit:10;}
	.st14{fill:none;stroke:#002A74;stroke-width:5;stroke-miterlimit:10;}
	.st15{font-family:'MyriadPro-Regular';}
	.st16{font-size:21px;}
	.st17{fill:none;stroke:#00C905;stroke-width:5;stroke-miterlimit:10;}
</style>""" % (top_left[0], top_left[1], top_left[2], bottom_left[0], bottom_left[1], bottom_left[2], top_right[0], top_right[1], top_right[2], bottom_right[0], bottom_right[1], bottom_right[2], middle[0], middle[1], middle[2]))

print("""<g>
	<rect x="459.5" y="424.5" width="702" height="469"/>
	<path d="M1161,425v468H460V425H1161 M1162,424H459v470h703V424L1162,424z"/>
</g>
<g>
	<polygon points="460.1,421.5 810.3,137.6 1160.6,421.5 	"/>
	<path d="M810.3,138.3L1159.2,421H461.5L810.3,138.3 M810.3,137L458.7,422H1162L810.3,137L810.3,137z"/>
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
	<polygon class="st7" points="732.5,556.5 809.6,479.2 886.8,556.5 	"/>
	<path d="M809.6,479.9l76,76.1H733.7L809.6,479.9 M809.6,478.5L731.2,557H888L809.6,478.5L809.6,478.5z"/>
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
<text transform="matrix(0.9604 0 0 1 568 465.1069)" class="st10 st11 st12">top-left</text>
<text transform="matrix(0.9604 0 0 1 970 465.1069)" class="st10 st11 st12">top-right</text>
<text transform="matrix(0.9604 0 0 1 548 835.7754)" class="st10 st11 st12">bottom-left</text>
<text transform="matrix(0.9604 0 0 1 778 543.1064)" class="st10 st11 st12">middle</text>
<text transform="matrix(0.9604 0 0 1 955 830.7754)" class="st10 st11 st12">bottom-right</text>
<path class="st13" d="M977.8,157.7c3.6-2.4,5-7.5,3-11.4c-1.9-3.7-6.4-6.2-6.6-10.4c-0.3-7,11.6-10.2,10.6-17.1
	c-0.5-3.4-4-5.6-4.9-8.9c-1.9-7.1,9.1-13.5,6.2-20.3"/>
<path class="st13" d="M954,154.5c3.3-0.7,3.5-5.6,1.9-8.6c-1.6-3-4.2-5.9-3.8-9.2c0.3-2.7,2.5-4.8,4.2-6.9c1.7-2.2,3-5.3,1.3-7.5"/>
<path class="st13" d="M932.8,158.8c3.1-3.2,3.6-8.5,1.3-12.3c-1.3-2.1-3.4-3.7-4.9-5.7c-1.5-2-2.5-4.8-1.2-7
	c0.8-1.4,2.4-2.1,3.6-3.2c3-2.6,3.8-7.5,1.8-11c-1.9-3.3-6.1-6.6-4.2-9.8c1.1-1.8,3.5-2.2,5.1-3.6c2.8-2.6,1.5-7.2-0.4-10.5
	s-4.3-6.9-3.2-10.5"/>
<path class="st14" d="M632,603c0-9,0-18,0-27"/>
<path class="st14" d="M631.1,551.7c-2.5-1.3-5.2-2.7-8-2.3c-5.4,0.7-7.8,7.9-5.7,12.9c2.1,5,7.1,8.1,11.9,10.6
	c3.1,1.6,6.4,3,9.8,3.2s7.2-1.2,9-4.2c1.5-2.6,1.3-6,0.4-8.9c-2.2-7.3-10.3-13.6-17.3-10.6"/>
<path class="st14" d="M655.1,582.4c-6.7,2.1-13.5,4.1-20.2,6.2c-5-1.7-13.9-3.9-18.9-5.6"/>
<path class="st14" d="M982.9,603c0.5-6.7,0.3-13.4-0.5-20"/>
<path class="st14" d="M982,557.9c-5.8-0.6-11.2,4.8-11.2,10.6s4.7,11,10.3,12.4c5.1,1.2,11.3-1.1,13-6c1.6-4.6-1.1-9.9-5.2-12.7
	s-9-3.7-13.9-4.6"/>
<path class="st14" d="M967,596.9c4.9-2.5,9.9-4.9,14.8-7.4c5.3,1,10.9,3.6,16.2,4.5"/>
<path class="st14" d="M630.7,799.9c-1-10-2-19.9-3.1-29.9"/>
<path class="st14" d="M622.9,751.3c-3.5-0.5-6.9,2.8-7.1,6.4c-0.3,3.6,1.9,7,4.9,9c3,2,6.6,2.8,10.1,3.2c1.8,0.2,3.7,0.3,5.3-0.6
	c3.5-1.9,3.2-7.1,1.7-10.8c-1.7-4.4-4.8-8.8-9.3-10.2c-4.6-1.4-10.5,1.9-10.2,6.7"/>
<path class="st14" d="M619,787c0-4.2,3.9-7.9,8-7.9c3.5,3.4,10.3,6.3,14.9,4.4c4.6-1.9,7.8-6.6,7.9-11.5"/>
<path class="st14" d="M1046,800c0.2-7.4-0.5-14.8-2.2-22"/>
<path class="st14" d="M1042.3,751.1c-5.1-1.8-11.3,0.6-13.9,5.3c-2.6,4.7-1.4,11.2,2.8,14.7c2.1,1.8,4.8,2.7,7.5,3.3
	c3,0.7,6.4,1,9.2-0.3c4.6-2.2,6.1-8.4,4.3-13.1c-1.7-4.7-6-8.2-10.4-10.5c-0.9-0.5-2.5-0.5-2.4,0.5"/>
<path class="st14" d="M1063.7,773c0.7,4.6-1.1,9.4-4.7,12.4c-3.5,3-8.6,4-13,2.5c-6,3.3-16.9-1.2-18.3-7.9"/>
<text transform="matrix(1 0 0 1 620.117 323)"><tspan x="0" y="0" class="st10 st15 st16">Please select a location and enter the desired </tspan><tspan x="76" y="25.2" class="st10 st15 st16">RGB values for that location.</tspan><tspan x="9.3" y="50.4" class="st10 st15 st16">You may use any of the following locations:</tspan><tspan x="-46.8" y="75.6" class="st10 st15 st16">top-left, top-right, middle, bottom-right, bottom-left, all.</tspan></text>
<path class="st17" d="M1237,847.1c-6.9,2-9.3,10.5-10.5,17.6c-1.2,7.1-2.4,14.2-3.6,21.3c0.8-4.8-4-15.8-4.1-21.7
	c-0.2-11.2,0.1-22.3,1.4-33.4"/>
<path class="st17" d="M1215.8,886c0-12.6-6.7-25-17.3-31.8"/>
<path class="st17" d="M1194.1,862.9c5.7,6.3,9.3,14.6,10,23.1c0-8.9,3.9-23.8,3.9-32.7c0-2.9,1.3-6.9,4.1-6.2"/>
<path class="st17" d="M1213.6,885c-0.2-11,10.4-21,21.4-20.1"/>
<path class="st17" d="M1135.6,832.4c15.1,15.1,27.8,32.6,37.4,51.6"/>
<path class="st17" d="M1176.1,891c0.4-7.6,0.8-15.3,1.2-22.9c0.1-1.7,1.3-4,2.7-3"/>
<path class="st17" d="M1186.2,892.1c1.8-5.1,4.4-9.9,7.8-14.1"/>
<path class="st17" d="M1176.6,894c0.2-13.3-0.5-26.7-1.9-40"/>
<path class="st17" d="M1183.3,888c1.2-13.4,4.2-26.7,9-39.3"/>
<path class="st17" d="M1169,894c0.4-10.8,0.8-21.6,1.3-32.4c0.1-2.7,0.2-5.5,1.5-7.8"/>
<path class="st17" d="M451,854c-0.3,10.1-1.3,20.1-2.9,30"/>
<path class="st17" d="M434.2,893c1.2-16.3,0.4-32.8-2.6-48.9"/>
<path class="st17" d="M441.2,874.1c3.2-8.4,7.5-16.5,12.7-23.8c1.8-2.5,4-5.2,7.1-5.5"/>
<path class="st17" d="M447.2,890c-3.1-19.6-17-37.1-35.3-44.7"/>
<path class="st17" d="M420.1,881.7c2.8-5,3.7-10.8,4.5-16.5c0.8-5.7,1.7-11.5,4.6-16.4c2.9-4.9,8.3-8.8,14-8.2"/>
<path class="st17" d="M410.2,882.9c-0.8-7.4-1.9-14.8-3.3-22.2c-0.7-4-1.5-8.1-3.5-11.6s-5.4-6.5-9.5-7"/>
<path class="st17" d="M416.2,890c2.9-23.2,3.8-46.7,2.6-70"/>
<path class="st17" d="M448,904c0.8-8.7,5.7-17.8,5.6-26.3c-0.1-8.3-6.8-14.4-8.4-22.3c-1.6-8,0.6-29.2,12.7-27.6"/>
<path class="st17" d="M468,899c0,1.2,0,2.5,0,3.7c2.4-8.9,5.7-17.5,10-25.7"/>
<path class="st17" d="M456.1,916c5.2-12.7,6.9-24.4,6.9-38c-3.2,9.6-7.2,19-12,28"/>
<path class="st17" d="M438.1,913c0.4-13.6-2-27.3-7.1-40"/>
<path class="st17" d="M409.1,909c1.5-10.3,1.1-20.9-1.2-31"/>
<path class="st17" d="M421.9,901c2.4-10.7,6.8-21,12.9-30.1"/>
<path class="st17" d="M399,887c1.3-14.2-1.9-28.7-9-41"/>
<path class="st17" d="M385,899c1.2-27.4-2.7-54.9-11.2-80.9"/>
<path class="st17" d="M393,890c2.8-18.3,5.5-36.6,8.3-55"/>
<path class="st17" d="M1146.3,906c4.3-27.6,14.1-54.3,28.6-78.1"/>
<path class="st17" d="M1157,899.2c3.7-19.8,4.6-40.1,2.7-60.2"/>
<path class="st17" d="M1205.8,886c-3.9-22.5-11.3-40.3-20.8-61c2.9,21.9,2.9,44.1,0,66"/>
<path class="st17" d="M1235.2,843c-0.1-0.5,0.9-0.5,0.8,0"/>
<path class="st17" d="M1208.1,894c-0.1-20.1,3.7-40.2,10.9-59"/>
<path class="st17" d="M1220.3,889.1c2.9-16.7,11.8-22.8,6-40c-5.4-16-12.8-31.2-22.7-44.9"/>
<path class="st17" d="M1196.8,894c2.3-14.3,6-28.4,11.1-42"/>
<path class="st17" d="M1232.2,896.1c4.9-16.4,14.3-31.4,26.9-42.9"/>
<path class="st17" d="M1224.7,892c0.2-7.5,0.3-15,0.5-22.5c0.4-16.5,0.9-33.5,7.5-48.7"/>
<path class="st17" d="M1156,904c0.4,0.9,0.7,1.7,1.1,2.6c-9.8-16.9-21.3-32.8-34.2-47.5"/>
<path class="st17" d="M1166,901c0.1-5.4-3-10.2-6-14.6c-8.3-12.5-16.6-24.9-25-37.4"/>
<path class="st17" d="M1209.6,894.2c-8.5-16.7-18-21.5-10.7-41.2"/>
<path class="st17" d="M1186.1,903.9c-7-12.3-13.9-24.7-20.9-37"/>
<path class="st17" d="M1198.1,904c2.4-8,6.5-15.6,12-22"/>
<path class="st17" d="M1224.8,907c-2.5-16.6-7.5-32.9-14.8-48.1"/>
<path class="st17" d="M398.5,907.9c-4.4-18.7-14.3-36-28.2-49.2"/>
<path class="st17" d="M387.2,909.1c5-14.3,20.6-24.1,35.7-22.4"/>
<path class="st17" d="M423.1,910c-0.5-12.7-0.3-25.4,0.8-38"/>
</svg></div></body></html>""")

# Generate a form that will submit a HTTP for the following query/update
print("""
	<h1 align="center">
	
	<form style="font-size:24px;" action="/cgi-bin/house-simulator.py" method="get">
		Location:<br>
		<input style="height:35px; width:200px;" type="text" name="location"><br>
		Red:<br>
		<input style="height:35px; width:200px;" type="text" name="red"><br>
		Green:<br>
		<input style="height:35px; width:200px;" type="text" name="green"><br>
		Blue: <br>
		<input style="height:35px; width:200px;" type="text" name="blue"><br>
		<input style="height:100px; width:150px; padding-top: 50px; font-size:32px;" type="submit" value="Submit">
	</form></h1>""")



# Commit changes to Datbase and Cleanup
conn.commit()
cursor.close()
conn.close()


