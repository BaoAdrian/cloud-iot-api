#!/usr/bin/env python3



import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Welcome</title>')
print('</head>')

print("""<body>
                <br/>
                <h1 align="center"> Cloud Computing - Project 2 - IoT Web Application</h1>
                <h2 align="center"> Welcome to our Web Application </h2>
                <h2 align="center"> Please Make a Selection Below </h2>
                <br/>

                <p align="center">
                <button type="button" align="left" onclick="window.location.href = 'http://127.0.0.1/cgi-bin/on-off.py';"  style="height:175px; width:250px; background:rgb(34,139,34); font-size:30px;">On/Off</button>
                
                <button type="button" align="center" onclick="window.location.href = 'http://127.0.0.1/cgi-bin/color-table.py';" style="height:175px; width:250px; background:rgb(50,80,160); font-size:30px;">Color Table</button>

                <button type="button" align="right" onclick="window.location.href = 'https://www.boredpanda.com/cute-wholesome-dog-puppy-memes/?utm_source=google&utm_medium=organic&utm_campaign=organic';" style="height:175px; width:250px; background:rgb(220,170,200); font-size:30px;">Dog Memes</button>
                </p>

	</body>""")

print('</html>')


