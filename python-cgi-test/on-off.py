#!/usr/bin/env python3

import cgitb
cgitb.enable()    
print("Content-Type: text/html;charset=utf-8")

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>On-Off</title>')
print('</head>')

print("""<body>
                <br/>
                <h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
                <h2 align="center"> On/Off </h2>
                <br/>

                <p align="center">
                <button type="button" align="left" style="height:150px; width:150px; background:rgb(34,139,34); font-size:24px;">On</button>
                <button type="button" align="right" style="height:150px; width:150px; background:rgb(220,20,60); font-size:24px;">Off</button>
                </p>

	</body>""")

print('</html>')
