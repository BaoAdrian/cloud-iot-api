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

if "location" not in form and "red" not in form and "green" not in form and "blue" not in form:
        # Query

else:
        # Update
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
	.st15{font-size:21px;}
	.st16{fill:none;stroke:#00C905;stroke-width:5;stroke-miterlimit:10;}
	.st17{fill:none;stroke:#00D800;stroke-width:6;stroke-miterlimit:10;}
	.st18{fill:#666666;stroke:#666666;stroke-width:2;stroke-miterlimit:10;}
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
<path class="st13" d="M954,154.5c3.3-0.7,3.5-5.6,1.9-8.6s-4.2-5.9-3.8-9.2c0.3-2.7,2.5-4.8,4.2-6.9c1.7-2.2,3-5.3,1.3-7.5"/>
<path class="st13" d="M932.8,158.8c3.1-3.2,3.6-8.5,1.3-12.3c-1.3-2.1-3.4-3.7-4.9-5.7s-2.5-4.8-1.2-7c0.8-1.4,2.4-2.1,3.6-3.2
	c3-2.6,3.8-7.5,1.8-11c-1.9-3.3-6.1-6.6-4.2-9.8c1.1-1.8,3.5-2.2,5.1-3.6c2.8-2.6,1.5-7.2-0.4-10.5s-4.3-6.9-3.2-10.5"/>
<path class="st14" d="M632,603c0-9,0-18,0-27"/>
<path class="st14" d="M631.1,551.7c-2.5-1.3-5.2-2.7-8-2.3c-5.4,0.7-7.8,7.9-5.7,12.9s7.1,8.1,11.9,10.6c3.1,1.6,6.4,3,9.8,3.2
	s7.2-1.2,9-4.2c1.5-2.6,1.3-6,0.4-8.9c-2.2-7.3-10.3-13.6-17.3-10.6"/>
<path class="st14" d="M655.1,582.4c-6.7,2.1-13.5,4.1-20.2,6.2c-5-1.7-13.9-3.9-18.9-5.6"/>
<path class="st14" d="M982.9,603c0.5-6.7,0.3-13.4-0.5-20"/>
<path class="st14" d="M982,557.9c-5.8-0.6-11.2,4.8-11.2,10.6s4.7,11,10.3,12.4c5.1,1.2,11.3-1.1,13-6c1.6-4.6-1.1-9.9-5.2-12.7
	s-9-3.7-13.9-4.6"/>
<path class="st14" d="M967,596.9c4.9-2.5,9.9-4.9,14.8-7.4c5.3,1,10.9,3.6,16.2,4.5"/>
<path class="st14" d="M630.7,799.9c-1-10-2-19.9-3.1-29.9"/>
<path class="st14" d="M622.9,751.3c-3.5-0.5-6.9,2.8-7.1,6.4c-0.3,3.6,1.9,7,4.9,9s6.6,2.8,10.1,3.2c1.8,0.2,3.7,0.3,5.3-0.6
	c3.5-1.9,3.2-7.1,1.7-10.8c-1.7-4.4-4.8-8.8-9.3-10.2c-4.6-1.4-10.5,1.9-10.2,6.7"/>
<path class="st14" d="M619,787c0-4.2,3.9-7.9,8-7.9c3.5,3.4,10.3,6.3,14.9,4.4c4.6-1.9,7.8-6.6,7.9-11.5"/>
<path class="st14" d="M1046,800c0.2-7.4-0.5-14.8-2.2-22"/>
<path class="st14" d="M1042.3,751.1c-5.1-1.8-11.3,0.6-13.9,5.3s-1.4,11.2,2.8,14.7c2.1,1.8,4.8,2.7,7.5,3.3c3,0.7,6.4,1,9.2-0.3
	c4.6-2.2,6.1-8.4,4.3-13.1c-1.7-4.7-6-8.2-10.4-10.5c-0.9-0.5-2.5-0.5-2.4,0.5"/>
<path class="st14" d="M1063.7,773c0.7,4.6-1.1,9.4-4.7,12.4c-3.5,3-8.6,4-13,2.5c-6,3.3-16.9-1.2-18.3-7.9"/>
<text transform="matrix(1 0 0 1 604.117 323)" class="st10 st11 st15">Please select a location and enter the desired </text>
<text transform="matrix(1 0 0 1 680.117 348.2)" class="st10 st11 st15">RGB values for that location.</text>
<text transform="matrix(1 0 0 1 613.417 373.4)" class="st10 st11 st15">You may use any of the following locations:</text>
<text transform="matrix(1 0 0 1 557.317 398.6)" class="st10 st11 st15">top-left, top-right, middle, bottom-right, bottom-left, all.</text>
<path class="st16" d="M1237,847.1c-6.9,2-9.3,10.5-10.5,17.6s-2.4,14.2-3.6,21.3c0.8-4.8-4-15.8-4.1-21.7
	c-0.2-11.2,0.1-22.3,1.4-33.4"/>
<path class="st16" d="M1215.8,886c0-12.6-6.7-25-17.3-31.8"/>
<path class="st16" d="M1194.1,862.9c5.7,6.3,9.3,14.6,10,23.1c0-8.9,3.9-23.8,3.9-32.7c0-2.9,1.3-6.9,4.1-6.2"/>
<path class="st16" d="M1213.6,885c-0.2-11,10.4-21,21.4-20.1"/>
<path class="st16" d="M1135.6,832.4c15.1,15.1,27.8,32.6,37.4,51.6"/>
<path class="st16" d="M1176.1,891c0.4-7.6,0.8-15.3,1.2-22.9c0.1-1.7,1.3-4,2.7-3"/>
<path class="st16" d="M1186.2,892.1c1.8-5.1,4.4-9.9,7.8-14.1"/>
<path class="st16" d="M1176.6,894c0.2-13.3-0.5-26.7-1.9-40"/>
<path class="st16" d="M1183.3,888c1.2-13.4,4.2-26.7,9-39.3"/>
<path class="st16" d="M1169,894c0.4-10.8,0.8-21.6,1.3-32.4c0.1-2.7,0.2-5.5,1.5-7.8"/>
<path class="st16" d="M451,854c-0.3,10.1-1.3,20.1-2.9,30"/>
<path class="st16" d="M434.2,893c1.2-16.3,0.4-32.8-2.6-48.9"/>
<path class="st16" d="M441.2,874.1c3.2-8.4,7.5-16.5,12.7-23.8c1.8-2.5,4-5.2,7.1-5.5"/>
<path class="st16" d="M447.2,890c-3.1-19.6-17-37.1-35.3-44.7"/>
<path class="st16" d="M420.1,881.7c2.8-5,3.7-10.8,4.5-16.5s1.7-11.5,4.6-16.4s8.3-8.8,14-8.2"/>
<path class="st16" d="M410.2,882.9c-0.8-7.4-1.9-14.8-3.3-22.2c-0.7-4-1.5-8.1-3.5-11.6s-5.4-6.5-9.5-7"/>
<path class="st16" d="M416.2,890c2.9-23.2,3.8-46.7,2.6-70"/>
<path class="st16" d="M448,904c0.8-8.7,5.7-17.8,5.6-26.3c-0.1-8.3-6.8-14.4-8.4-22.3c-1.6-8,0.6-29.2,12.7-27.6"/>
<path class="st16" d="M468,899c0,1.2,0,2.5,0,3.7c2.4-8.9,5.7-17.5,10-25.7"/>
<path class="st16" d="M456.1,916c5.2-12.7,6.9-24.4,6.9-38c-3.2,9.6-7.2,19-12,28"/>
<path class="st16" d="M438.1,913c0.4-13.6-2-27.3-7.1-40"/>
<path class="st16" d="M409.1,909c1.5-10.3,1.1-20.9-1.2-31"/>
<path class="st16" d="M421.9,901c2.4-10.7,6.8-21,12.9-30.1"/>
<path class="st16" d="M399,887c1.3-14.2-1.9-28.7-9-41"/>
<path class="st16" d="M385,899c1.2-27.4-2.7-54.9-11.2-80.9"/>
<path class="st16" d="M393,890c2.8-18.3,5.5-36.6,8.3-55"/>
<path class="st16" d="M1146.3,906c4.3-27.6,14.1-54.3,28.6-78.1"/>
<path class="st16" d="M1157,899.2c3.7-19.8,4.6-40.1,2.7-60.2"/>
<path class="st16" d="M1205.8,886c-3.9-22.5-11.3-40.3-20.8-61c2.9,21.9,2.9,44.1,0,66"/>
<path class="st16" d="M1235.2,843c-0.1-0.5,0.9-0.5,0.8,0"/>
<path class="st16" d="M1208.1,894c-0.1-20.1,3.7-40.2,10.9-59"/>
<path class="st16" d="M1220.3,889.1c2.9-16.7,11.8-22.8,6-40c-5.4-16-12.8-31.2-22.7-44.9"/>
<path class="st16" d="M1196.8,894c2.3-14.3,6-28.4,11.1-42"/>
<path class="st16" d="M1232.2,896.1c4.9-16.4,14.3-31.4,26.9-42.9"/>
<path class="st16" d="M1224.7,892c0.2-7.5,0.3-15,0.5-22.5c0.4-16.5,0.9-33.5,7.5-48.7"/>
<path class="st16" d="M1156,904c0.4,0.9,0.7,1.7,1.1,2.6c-9.8-16.9-21.3-32.8-34.2-47.5"/>
<path class="st16" d="M1166,901c0.1-5.4-3-10.2-6-14.6c-8.3-12.5-16.6-24.9-25-37.4"/>
<path class="st16" d="M1209.6,894.2c-8.5-16.7-18-21.5-10.7-41.2"/>
<path class="st16" d="M1186.1,903.9c-7-12.3-13.9-24.7-20.9-37"/>
<path class="st16" d="M1198.1,904c2.4-8,6.5-15.6,12-22"/>
<path class="st16" d="M1224.8,907c-2.5-16.6-7.5-32.9-14.8-48.1"/>
<path class="st16" d="M398.5,907.9c-4.4-18.7-14.3-36-28.2-49.2"/>
<path class="st16" d="M387.2,909.1c5-14.3,20.6-24.1,35.7-22.4"/>
<path class="st16" d="M423.1,910c-0.5-12.7-0.3-25.4,0.8-38"/>
<path class="st17" d="M1121.5,906.2c6.1-20.1,0.4-43.3-14.4-58.2"/>
<path class="st17" d="M1107.1,902c2.1-10.3,5.8-20.3,10.8-29.5c3-5.5,7.7-11.5,14-11.2"/>
<path class="st17" d="M1135.6,905.1c1.8-19,0.7-38.3-3-57"/>
<path class="st17" d="M1088.2,907c1.5-14.5,4.1-28.9,7.8-43"/>
<path class="st17" d="M1073.9,899c0.8-10,0.2-20.2-1.9-30"/>
<path class="st17" d="M1093.9,905c5.6-22.2,13.4-43.7,23.3-64.3"/>
<path class="st17" d="M1077.2,907.1c3.4-11.3-1.6-23.3-7.4-33.6c-5.8-10.4-12.6-20.3-19.3-30.2"/>
<path class="st17" d="M1045.9,910.9c-2.6-27.5-17.9-53.5-40.8-69.1"/>
<path class="st17" d="M1063.2,862.8c-3.9,12.7-5.1,15-15.5,22.6c-9.8,7.2-18.4,15.9-25.7,25.6"/>
<path class="st17" d="M1073.4,905.1c3.6-21,6.7-42,9.3-63.1"/>
<path class="st17" d="M1053.1,899c1.9-7.8,3.9-15.6,3.9-23.6c0.1-8-2-16.3-7.1-22.4"/>
<path class="st17" d="M478.8,907c-2.6-17.2-4.3-34.6-4.9-52"/>
<path class="st17" d="M511.7,861.9c-6.5,15.6-12.7,31.3-18.6,47.2c1.1-14.4,1.4-32.2-7.3-43.8"/>
<path class="st17" d="M515,912c3-13.5,3.1-27.6,0.3-41.1"/>
<path class="st17" d="M525.6,902.6c6.5-7.2,13-14.4,19.5-21.6"/>
<path class="st17" d="M546.1,921c5.6-11.3,11.3-22.7,16.9-34"/>
<path class="st17" d="M562.3,920.1c3.6-20.5-7.2-40.5-18.3-58.1"/>
<path class="st17" d="M544,911c3.8-13.5,16.1-24.1,30-25.9"/>
<path class="st17" d="M588.2,917c0.3-15.1-10.2-28-20.6-38.9c-5.7-5.9-11.5-11.6-17.5-17.2"/>
<path class="st17" d="M522.8,912.9c-1.2,2.1-1.2,4.8-0.1,7c3.4-19.4,6.8-38.7,10.3-58.1"/>
<path class="st17" d="M534.2,907c2.4-11.8,6.8-23.2,13.1-33.5"/>
<path class="st17" d="M590.8,906.8c-6.2-22-19.7-41.8-37.9-55.6"/>
<path class="st17" d="M573.1,913c8.2-15.7,16.5-31.4,24.7-47.1"/>
<path class="st17" d="M605.4,907.1c3.2-12.9,6.9-25.7,11.2-38.2"/>
<path class="st17" d="M624.7,905.9c-1.1-7.4-6.7-15.8-6.1-23.2c0.7-8.6,10.7-19,16.4-24.7"/>
<path class="st17" d="M647.8,904.9c2.3-7.8,5.8-15.2,10.3-21.9"/>
<path class="st17" d="M650.4,917.1c6-24.3,5.1-50.2-2.5-74.1"/>
<path class="st17" d="M640.4,897c0.1-10.7-2.5-21.5-7.6-30.9"/>
<path class="st17" d="M616.6,906.8c-5.8-23-16.5-44.8-31.1-63.5"/>
<path class="st17" d="M657.8,910c3.4-18.8,9.5-37,18-54.1"/>
<path class="st17" d="M642,904c-5-15.2-14.9-28.8-27.9-38.1"/>
<path class="st17" d="M683.7,906.9c6.3-17,12.6-34,18.9-51"/>
<path class="st17" d="M696.8,909.9c3.4-7.4,8.7-14,15.2-18.9"/>
<path class="st17" d="M683.4,918.1c2.8-15.6,1.9-31.8-2.6-47"/>
<path class="st17" d="M662.3,906c0.4-11.1,1.6-22.1,3.7-33"/>
<path class="st17" d="M685,884c0.7-1,1.3-2,2-3"/>
<path class="st17" d="M664.7,925.9c5.4-20.5,8.2-41.7,8.4-62.9"/>
<path class="st17" d="M609.9,916c0.2,1.4-0.4,2.9-1.5,3.9c-3.1-9.2-7-18.2-11.5-26.9"/>
<path class="st17" d="M575,889c0.1,1.9,0.2,3.8,0.3,5.7c-2.3-7.2-5.5-14.2-9.4-20.7"/>
<path class="st17" d="M553.9,892c0.3,1.3,0.2,2.7-0.3,3.9c-1.9-11.4-4.4-22.7-7.6-33.9"/>
<path class="st17" d="M535.1,899c-0.3,0.9-0.5,1.7-0.8,2.6c0.6-5.5,1.2-11,1.8-16.6"/>
<path class="st17" d="M525.8,901.9c-1.6,2.6-3.1,5.3-4.7,7.9c1-5.1,2.7-10.1,4.9-14.8"/>
<path class="st17" d="M496.7,925.4c0.5,0,0,0.9-0.4,0.6c-0.4-0.2-0.4-0.8-0.3-1.3c1-5.9,2.1-11.8,3.1-17.8"/>
<path class="st17" d="M495.9,893c-3.6,5.3-7.5,10.3-11.9,15c0-16.6-0.1-33.3-0.1-49.9"/>
<path class="st17" d="M515.9,917.1c1.8-20.9-1-42.2-8.3-62"/>
<path class="st17" d="M556.1,903c0.2,0.8,1.6,0.9,1.9,0.1c0.4-4.7,0.1-9.5-0.7-14.2"/>
<path class="st17" d="M563.8,929c-2.3-19.3-16.7-34.7-30.3-48.6"/>
<path class="st17" d="M533.9,915c0.8-13.4,3.9-26.6,9.1-39"/>
<path class="st17" d="M454.2,914c3.5-18.8,9.8-37.1,18.8-54.1"/>
<path class="st17" d="M442.2,860c-3,17.5-8,34.7-14.8,51.1c-1.5-15.1-9.8-28-17.6-41"/>
<path class="st17" d="M716.2,904c1.9-14.2-0.9-24-1.6-38.3c-8.1,11.9-12.8,26-13.7,40.3"/>
<path class="st17" d="M724.9,903c3.6-16.2,2.2-33.5-3.9-49"/>
<path class="st17" d="M730.5,911.7c7.3-13.3,13.2-27.2,17.8-41.6"/>
<path class="st17" d="M721,904.1c-2.1-0.6-4.5,1.2-4.6,3.3c-5.8-13.8-11.6-27.6-17.6-41.4"/>
<path class="st17" d="M700.3,911.9c-4.1-10.7-8.7-21.3-13.7-31.7"/>
<path class="st17" d="M697.3,918.8c-10.1-17.2-21.6-33.5-34.3-48.8"/>
<path class="st17" d="M687.1,914c3.4-8,6.7-16,10.1-24"/>
<path class="st17" d="M712.2,922.1c3-8.7,6-17.3,9-26"/>
<path class="st17" d="M626.9,919.1c-2.2-4.7-4.5-9.4-6.7-14.1"/>
<path class="st17" d="M582.5,920c-0.1-13.5,3.8-27,11-38.4"/>
<path class="st17" d="M598.7,923c2.8-17.4,9.5-34.3,19.4-48.9"/>
<path class="st17" d="M714.1,843.9c11.9,16.6,23.3,33.5,34.2,50.7c4,6.3,8.1,13,8.6,20.4c0.7-17.3,6-33.7,6.7-51"/>
<path class="st17" d="M744.5,914c1-17.6,5.3-35,12.4-51.1"/>
<path class="st17" d="M858.1,911c-0.9-17.1,0.3-34.3,3.6-51.1"/>
<path class="st17" d="M869.7,908c0.4-8.4,1.8-16.8,4.3-24.8c1.6-5.1,4.6-10.9,9.9-11.5"/>
<path class="st17" d="M902.7,852.6c-6.3,5.2-8.5,13.7-10.1,21.8c-2.1,10.8-3.8,21.8-5.4,32.7"/>
<path class="st17" d="M898.8,905c3.4-14,8.8-27.5,16.1-39.9c1.6-2.7,4.1-5.7,7.1-5.1"/>
<path class="st17" d="M897.1,906.9c-14.2-20.6-28.6-41.8-38.8-64.6"/>
<path class="st17" d="M884.2,913c1.2-16.6,10.1-40.5,25.3-49.7c19-11.5,26.6,24.9,28.3,38.6"/>
<path class="st17" d="M922.5,902.7c-3.5-7.6-7.8-14.8-12.7-21.7"/>
<path class="st17" d="M940.7,903.2c3.7-12.9,8.6-25.5,14.8-37.5"/>
<path class="st17" d="M957.1,906c4.1-14.1,10.8-27.5,19.6-39.2"/>
<path class="st17" d="M986,903c2-3.7,4-7.3,6-11"/>
<path class="st17" d="M1017,905c-6.9-22.9-24.1-42.4-46-52.2"/>
<path class="st17" d="M970.6,898.1c4.2-16.1,10.2-31.7,17.7-46.5"/>
<path class="st17" d="M998.4,904c1.3-15.6,4.7-31.1,10-45.8c1.8-5.1,4.1-10.3,8.3-13.6"/>
<path class="st17" d="M980.1,904c1.8-18.3,5.4-36.4,10.9-54"/>
<path class="st17" d="M954.1,911c-1.2-22.5-9.7-44.6-23.9-62.1"/>
<path class="st17" d="M931.1,899c-1.1-9.1-2.8-18.1-5.1-27"/>
<path class="st17" d="M993.8,911.9c4.9-14,13.1-26.9,23.8-37.3"/>
<path class="st17" d="M1038.4,909.8c-8.2-16.6-17.7-32.6-28.4-47.8"/>
<path class="st17" d="M971.2,916c-3.6-20.1-10-39.7-19.1-58"/>
<path class="st17" d="M925.3,906.9c-5.9-21.4-14.8-41.9-26.3-60.9"/>
<path class="st17" d="M933.5,917c0.9-18.7,1.7-37.4,2.6-56.1"/>
<path class="st17" d="M738.8,919.1c-6-19.3-14.3-37.8-24.7-55.1"/>
<path class="st17" d="M968.7,918c1.9-18.6-3.1-38.9,5.9-55.3"/>
<path class="st17" d="M997,914c3.3-16,8.9-31.6,16.6-46c3-5.7,7.1-11.7,13.4-13.1"/>
<path class="st17" d="M1030.4,914.1c3.7-16.9,8.3-33.6,13.8-50"/>
<path class="st17" d="M1068.4,904.1c2.3-14.2,8.6-27.7,18-38.6"/>
<path class="st17" d="M1124.6,904.7c-11.1-22.7-29.8-38.6-52.4-49.8c14.8,16.2,24.1,37.3,26,59.1"/>
<path class="st17" d="M1155.9,907c6.8-14.1,15.5-27.4,25.8-39.2"/>
<path class="st17" d="M1140,920c1.4-22.3,1.4-44.7,0-67"/>
<path class="st17" d="M891.6,919.8c9.7-16.7,13.7-36.6,11.1-55.7"/>
<path class="st17" d="M873.4,902.9c-2.8-17-5.6-34-8.3-50.9"/>
<path class="st17" d="M910,912.1c1.9-8.6,3.8-17.3,5.8-25.9c1.1-5,2.3-10.1,4.9-14.4c2.7-4.4,7.1-7.9,12.2-8.1"/>
<path class="st17" d="M949.1,916c0-16.5,5.6-33,15.8-46.1"/>
<path class="st17" d="M990,920c3.9-15.8,6.9-31.8,9-48"/>
<path class="st17" d="M632.5,926c1.1-18,0.9-36.1-0.4-54"/>
<path class="st17" d="M644.3,923.1c5.4-16.7,11.4-33.2,18-49.4"/>
<path class="st17" d="M583.7,929.8c-6.3-18.8-16.2-36.4-28.9-51.6"/>
<path class="st17" d="M679.6,924.1c2.3-14.9,7.4-29.3,15-42.3"/>
<path class="st17" d="M705,922c-9.2-17.3-19.6-34-31.2-49.9"/>
<path class="st17" d="M596.3,924.4c2.3-10-0.1-20.7-4.8-29.9c-4.7-9.2-11.5-17-18.7-24.4"/>
<path class="st17" d="M543.2,926.1c2.1-11.4-0.8-23.3-6.2-33.6c-5.4-10.3-13.1-19.1-21.2-27.4"/>
<path class="st17" d="M475.8,920.9c4.7-20,10.8-39.7,18.2-58.9"/>
<path class="st17" d="M394.3,911.9c-4.8-16.2-12.1-31.7-21.5-45.8"/>
<path class="st17" d="M388.3,874c-1.9-21.3-3.8-42.6-5.7-63.9"/>
<path class="st17" d="M402.9,856c3.8-9.5,9.3-18.3,16-26"/>
<path class="st17" d="M422,868c5.1-10.8,8.8-22.2,11-34"/>
<path class="st17" d="M438.8,869.8c8.4-9.6,16.9-19.2,25.3-28.7"/>
<path class="st17" d="M418.4,873.9c-5.4-16.5-12.9-32.3-22.4-46.9"/>
<path class="st17" d="M1179.1,864c3.5-15.1,5.1-30.6,4.9-46"/>
<path class="st17" d="M1192.9,880c0.6-24.5,2.8-48.9,6.7-73.1"/>
<path class="st17" d="M1202.2,875.1c12.6-22.4,25.2-44.7,37.8-67.1"/>
<path class="st17" d="M1232.6,877.8c4.6-8.8,10.2-17.1,16.5-24.7"/>
<path class="st17" d="M1184,861c-1.6-10.8-5-21.3-9.9-31"/>
<path class="st17" d="M1204.8,877c-0.4-15.3-0.8-30.6-1.2-46"/>
<path class="st17" d="M1234.2,902c3.8-21.7,11.3-42.7,21.8-62"/>
<path class="st17" d="M1254.9,893c-5.6-18.6-15.9-35.7-29.7-49.3"/>
<path class="st17" d="M1240.8,899c-0.6-17.3-9.1-34.2-22.7-45.1"/>
<path class="st17" d="M368.6,901.9c5.9-21.1,12.4-42.1,19.3-62.9"/>
<path class="st17" d="M352.9,888.1c1.8-17.7,3.1-35.4,3.9-53.1"/>
<path class="st17" d="M353.9,906c-0.6,0-0.2,1.1,0.4,1c0.6-0.1,0.8-0.8,0.9-1.4c3.5-16.5,6.9-33.1,10.4-49.6"/>
<path class="st17" d="M374.3,906.1c2.9-13.7,5.8-27.4,8.6-41.1"/>
<path class="st17" d="M406.6,913.8c-7.7-27.5-16.2-54.8-25.6-81.8"/>
<path class="st17" d="M728.3,926c-2.8-19-10.2-37.3-21.4-52.9"/>
<path class="st17" d="M745.2,917.9c1.2-14.9,3.8-29.6,7.7-44"/>
<path class="st17" d="M755.4,921c-0.1-26.8-4.8-53.6-13.8-78.8"/>
<path class="st17" d="M866.8,916.2c0.8-0.1,0.2,1.4-0.5,1.1c-0.7-0.3-0.7-1.3-0.6-2.1c3.3-24.1,6.7-48.2,10-72.2"/>
<path class="st17" d="M877.9,920c4.5-15.5,6.2-31.9,4.9-48"/>
<path class="st17" d="M903.7,922c0.6-26.1-1.8-52.3-7.3-77.9"/>
<path class="st17" d="M918.4,913c0.3-18.3,0.6-36.7,0.9-55"/>
<path class="st17" d="M1011.4,847.5c20,18.9,35.6,42.4,45.2,68.2c2-19.9,6.2-43.4,10.7-62.9"/>
<path class="st17" d="M1071.8,913.9c3.8-12.7,7.9-25.4,12.4-37.9"/>
<path class="st17" d="M1086.8,921c3-13,7.1-25.7,12.2-37.9"/>
<path class="st17" d="M1011.5,919c-0.8-17.1-8.4-33.8-20.7-45.7"/>
<path class="st17" d="M1107.4,916c0.7-9.7,1.5-19.4,2.2-29.1"/>
<path class="st17" d="M1123,915c0.8-12.4-0.5-25-4-37"/>
<path class="st17" d="M1172.3,912.9c-1.9-9.9-4.8-19.5-8.4-28.9"/>
<path class="st17" d="M1178.7,909.9c3.4-15.1,7.2-30,11.4-44.9"/>
<path class="st17" d="M1185.3,841.4c8,10.9,16,21.8,22.2,33.9c6.1,12,10.3,25.3,10.2,38.8"/>
<line class="st18" x1="779" y1="894" x2="763.5" y2="929.8"/>
<line class="st18" x1="843" y1="894" x2="857.8" y2="929.8"/>
<line class="st18" x1="763.5" y1="929.8" x2="857.8" y2="929.8"/>
<path class="st7" d="M854.7,920.8c-1.2-2.8-3.2-5.1-4.9-7.6c2-2.7,1.1-7.4-2.8-8.1c0-0.3,0-0.6,0-0.8c0-1.6-0.5-2.8-1.4-3.6
	c0.8-2.9-0.7-6.5-4.6-6.6c-15.1-0.2-30.3-0.1-45.4,0.2c-0.5-0.2-1-0.2-1.6-0.2c-0.4,0-0.7,0-1,0.1c-0.3-0.1-0.6-0.1-1-0.1
	c-0.6,0-1.1,0.1-1.5,0.2c-0.9-0.2-1.9-0.2-2.9,0c-0.5-0.2-1-0.2-1.6-0.2c-0.4,0-0.7,0-1,0.1c-0.3-0.1-0.6-0.1-1-0.1
	c-0.4,0-0.7,0-1,0.1c-0.3-0.1-0.7-0.1-1-0.1c-2.1,0-3.5,1.1-4.2,2.5c-2.4,1.2-3.2,4.3-2.2,6.7c-2.1,4.7-4,9.4-5.7,14.3
	c-1.6,0.7-2.5,2.2-2.7,3.9c-4.6,1.7-4,9.7,1.8,9.7c1.9,0,3.2-0.9,4-2.1c1.8,0.3,3.4,0.3,4.9,0c0.4,0.1,0.9,0.2,1.4,0.2
	c3,0,6,0,9-0.1c1.3,0.1,2.6,0.1,4,0c0.1,0,0.2,0,0.3,0c15.2,0,30.3,0.3,45.5,1.1c0.5,0,0.9,0,1.3-0.1c1.3,0.3,2.7,0.2,4-0.3
	c0.3-0.1,0.6-0.2,0.8-0.4c0.4,0.4,0.8,0.7,1.4,1c2.6,1.4,5.4,1,7.4-0.4C857.4,929.2,858,923,854.7,920.8z"/>
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


