#!/usr/bin/env python3

import MySQLdb
# import secrets as secrets
import random
import cgitb
cgitb.enable()    



'''
# Setup Connection to Database
conn = MySQLdb.connect( host 	= secrets.HOST,
			user 	= secrets.USER,
			passwd 	= secrets.PASSWORD,
			db 	= secrets.DB)

# Setup cursor to query database
cursor = conn.cursor()
'''

device_status = random.randint(0,1)


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
			%d
			<br/>""" % (device_status))




# This could be a possible way of handling the website generation 
# depending on the 'state' of the iot device.
# The idea here is that each time this script is run, it will 
# query the database for the respective entry and generate the
# corresponding database. For example

'''
# PsuedoCode
if (GET device_status FROM db) == 'on':
	Generate ON html page
else:
	Generate OFF html page
'''

# Code
if device_status == 1:
	# Generate Device ON html page
	print("""
		<br/>
		<h2 align="center"> Device is currently ON </h2>
		<br/>
		<p align="center">
			<button type="button" align="center" onclick="window.location.reload()" style="height:150px; width:150px; background:rgb(220,20,60); font-size:24px;">Turn OFF</button>
		</p>
		</body></html>
		""")
else:
	# Generate Device OFF html page 
	print("""
                <br/>
                <h2 align="center"> Device is currently OFF </h2>
                <br/>
                <p align="center">
                        <button type="button" align="center" onclick="window.location.reload()" style="height:150px; width:150px; background:rgb(60,220,60); font-size:24px;">Turn ON</button>
                </p>
                </body></html>
                """)


'''
# Commit changes to Datbase and Cleanup
conn.commit()
cursor.close()
conn.close()
'''

