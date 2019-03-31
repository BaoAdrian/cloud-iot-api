#!/usr/bin/env python3

import MySQLdb
import random
import cgitb
cgitb.enable()    




# Setup Connection to Database
conn = MySQLdb.connect( host 	= 'project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com',
			user 	= 'Admin',
			passwd 	= 'project2password',
			db 	= 'project2db')

# Setup cursor to query database
cursor = conn.cursor()

print("Content-Type: text/html;charset=utf-8")
print("Content-type:text/html\r\n\r\n")
print("""<html>
		<head>
			<title> On-Off </title>
		</head>
		<body>
			<br/>
			<h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
			<h2 align="center"> On/Off </h2>
			<br/>
			""")

cursor.execute("""SELECT status FROM power""")

for row in cursor.fetchall():
	device_status = int(row[0])

if device_status == 1:
	cursor.execute("""UPDATE power SET status=0;""")
	# Generate Device ON html page
	print("""
		<br/>
		<h2 align="center"> Device is currently ON </h2>
		
		 <center>
                                <h1 style="color:yellow">
                                        <svg align="center" viewBox="0 0 60 55" preserveAspectRatio="xMidYMin slice"
   style="width: 30%; padding-bottom: 30%; height: 1px; overflow: visible">
  <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb fa-w-11" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 352 512"><path fill-opacity="0.9" fill="currentColor" d="M96.06 454.35c.01 6.29 1.87 12.45 5.36 17.69l17.09 25.69a31.99 31.99 0 0 0 26.64 14.28h61.71a31.99 31.99 0 0 0 26.64-14.28l17.09-25.69a31.989 31.989 0 0 0 5.36-17.69l.04-38.35H96.01l.05 38.35zM0 176c0 44.37 16.45 84.85 43.56 115.78 16.52 18.85 42.36 58.23 52.21 91.45.04.26.07.52.11.78h160.24c.04-.26.07-.51.11-.78 9.85-33.22 35.69-72.6 52.21-91.45C335.55 260.85 352 220.37 352 176 352 78.61 272.91-.3 175.45 0 73.44.31 0 82.97 0 176zm176-80c-44.11 0-80 35.89-80 80 0 8.84-7.16 16-16 16s-16-7.16-16-16c0-61.76 50.24-112 112-112 8.84 0 16 7.16 16 16s-7.16 16-16 16z"></path></svg>
  </svg>
</svg>
<h1/>
<center/>
		<p align="center">
			<button type="button" align="center" onclick="window.location.reload()" style="height:150px; width:150px; background:rgb(220,20,60); font-size:24px;">Turn OFF</button>
		</p>
		</body></html>
		""")
else:
	cursor.execute("""UPDATE power SET status=1;""")
	# Generate Device OFF html page 
	print("""
                <br/>
                <h2 align="center"> Device is currently OFF </h2>
		 <center>
                                <h1 style="color:black">
                                        <svg align="center" viewBox="0 0 60 55" preserveAspectRatio="xMidYMin slice"
   style="width: 30%; padding-bottom: 30%; height: 1px; overflow: visible">
  <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="lightbulb" class="svg-inline--fa fa-lightbulb fa-w-11" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 352 512"><path fill="currentColor" d="M96.06 454.35c.01 6.29 1.87 12.45 5.36 17.69l17.09 25.69a31.99 31.99 0 0 0 26.64 14.28h61.71a31.99 31.99 0 0 0 26.64-14.28l17.09-25.69a31.989 31.989 0 0 0 5.36-17.69l.04-38.35H96.01l.05 38.35zM0 176c0 44.37 16.45 84.85 43.56 115.78 16.52 18.85 42.36 58.23 52.21 91.45.04.26.07.52.11.78h160.24c.04-.26.07-.51.11-.78 9.85-33.22 35.69-72.6 52.21-91.45C335.55 260.85 352 220.37 352 176 352 78.61 272.91-.3 175.45 0 73.44.31 0 82.97 0 176zm176-80c-44.11 0-80 35.89-80 80 0 8.84-7.16 16-16 16s-16-7.16-16-16c0-61.76 50.24-112 112-112 8.84 0 16 7.16 16 16s-7.16 16-16 16z"></path></svg>
  </svg>
</svg>
<h1/>
<center/>
                <p align="center">
                        <button type="button" align="center" onclick="window.location.reload()" style="height:150px; width:150px; background:rgb(60,220,60); font-size:24px;">Turn ON</button>
                </p>
                </body></html>
                """)



# Commit changes to Datbase and Cleanup
conn.commit()
cursor.close()
conn.close()
