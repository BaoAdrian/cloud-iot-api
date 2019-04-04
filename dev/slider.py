#!/usr/bin/env python3

import random
import cgitb
import cgi
import MySQLdb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")

print("Content-type:text/html\r\n\r\n")
form = cgi.FieldStorage()

# Setup Connection to Database
conn = MySQLdb.connect( host    = 'project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com',
                        user    = 'Admin',
                        passwd  = 'project2password',
                        db      = 'project2db')

# Setup cursor to query database
cursor = conn.cursor()

print('<html>')
print('<head>')
print('<title>RBG Sliders</title>')
print('</head>')

#try:
red_val = form.getvalue("red")
green_val = form.getvalue("green")
blue_val = form.getvalue("blue")
#except TypeError:
#    red_val, green_val, blue_val = 1,1,1
if red_val is not None:
    cursor.execute("""UPDATE light_status SET red=%d;"""%int(red_val))
    cursor.execute("""UPDATE light_status SET green=%d;"""%int(green_val))
    cursor.execute("""UPDATE light_status SET blue=%d;"""%int(blue_val))
    conn.commit()
else:
    cursor.execute("""SELECT * FROM light_status;""")
    for row in cursor.fetchall():
        red_val = row[0]
        green_val = row[1]
        blue_val = row[2]


print("""<body>
	<form name="rbg" action="slider.py" method="get">
<input type="range" name="red" id="redId" value="1" min="1" max="255" oninput="redoutputId.value = redId.value">
<output name="redoutput" id="redoutputId">1</output>
<input type="range" name="green" id="greenId" value="1" min="1" max="255" oninput="greenoutputId.value = greenId.value">
<output name="greenoutput" id="greenoutputId">1</output>
<input type="range" name="blue" id="blueId" value="1" min="1" max="255" oninput="blueoutputId.value = blueId.value">
<output name="blueoutput" id="blueoutputId">1</output>
<input type="submit" value="Submit">
</form>

<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb fa-w-11" role="img"  viewBox="0 0 352 512"><path fill-opacity="0.9" fill="rgb(%d,%d,%d)" d="M96.06 454.35c.01 6.29 1.87 12.45 5.36 17.69l17.09 25.69a31.99 31.99 0 0 0 26.64 14.28h61.71a31.99 31.99 0 0 0 26.64-14.28l17.09-25.69a31.989 31.989 0 0 0 5.36-17.69l.04-38.35H96.01l.05 38.35zM0 176c0 44.37 16.45 84.85 43.56 115.78 16.52 18.85 42.36 58.23 52.21 91.45.04.26.07.52.11.78h160.24c.04-.26.07-.51.11-.78 9.85-33.22 35.69-72.6 52.21-91.45C335.55 260.85 352 220.37 352 176 352 78.61 272.91-.3 175.45 0 73.44.31 0 82.97 0 176zm176-80c-44.11 0-80 35.89-80 80 0 8.84-7.16 16-16 16s-16-7.16-16-16c0-61.76 50.24-112 112-112 8.84 0 16 7.16 16 16s-7.16 16-16 16z"></path></svg>
	</body>"""%(int(red_val), int(green_val), int(blue_val)))


print('</html>')





