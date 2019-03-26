# Testing how to integrate CGI with Python on Apache Webserver

*Note that the following was done on a machine running Ubuntu 18.04*

URL provided in specifications for setup: http://httpd.apache.org/docs/2.2/howto/cgi.html <br/>
This URL tutorial worked for me: https://tasdikrahman.me/2015/09/30/Running-CGI-Scripts-on-Apache2-Ubuntu/


# Getting Started

If you have successfully installed apache2 on your machine, the installer should install the config files somewhere. In my case, the two config files I had to modify were located at the following: 

apache2.conf -> ```/etc/apache2/apache.conf```<br/>
serve-cgi-bin.conf -> ```/etc/apache2/conf-available/serve-cgi-bin.conf```<br/>


<h2> apache2.conf </h2>
First, you need to modify apache2.conf using 

```
sudo vim /etc/apache2/apache.conf
```

and pasting the following code at the bottom of that config file.


```
###################################################################
#########     Adding capaility to run CGI-scripts #################
ServerName localhost
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
Options +ExecCGI
AddHandler cgi-script .cgi .pl .py
```
Save and exit the vim editor with `:wq`.

Note the `ScriptAlias` directive here which is telling apache to look for all cgi scripts inside the directory `/var/www/cgi-bin/`. This directory is where you should store all of python scripts which I have included a test script in this repo.


<h2> serve-cgi-bin.conf </h2>
The next step is to modify the serve-cgi-bin.conf config file. This is similar to what was done above where you run 

```
sudo vim /etc/apache2/conf-available/serve-cgi-bin.conf
```

and paste the following into the config file:

```
<IfModule mod_alias.c>
	<IfModule mod_cgi.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfModule mod_cgid.c>
		Define ENABLE_USR_LIB_CGI_BIN
	</IfModule>

	<IfDefine ENABLE_USR_LIB_CGI_BIN>
		#ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
		#<Directory "/usr/lib/cgi-bin">
		#	AllowOverride None
		#	Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		#	Require all granted
		#</Directory>

		## cgi-bin config
		ScriptAlias /cgi-bin/ /var/www/cgi-bin/
	    <Directory "/var/www/cgi-bin/">
	        AllowOverride None
	        Options +ExecCGI 
	    </Directory>

	</IfDefine>
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```
Save and exit the vim editor with `:wq`.


Note here that the Directory that we have our `AllowOverride` and `Options` Directives is in fact the one we added earlier in the apache2.conf config file. It is also important to restart the Apache Webserver to pick up the changes we made above so run `sudo service apache2 restart` and proceed to the next step.


<h2> Creating Directory and Testing first site </h2>
Assuming the above has been sucessfully implemented, you can create the directory we set Apache to look for. Do this by running 

```
sudo mkdir /var/www/cgi-bin
```

and cd into that directory. Now you can create a simple test python script that uses cgi. Run:

```
sudo vim test-site.py 
```

and insert the following 'Hello World' script:


```python
#!/usr/bin/env python

import cgitb
cgitb.enable()    
print("Content-Type: text/html;charset=utf-8")

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '</body>'
print '</html>'
```
As always, save and exit vim editor using `:wq`. 

Make sure the python script is executable:

```
sudo chmod o+x test-site.py
```

Now with all that set up, you can access the output in two different ways. Right in the terminal, you can run `curl http://127.0.0.1/cgi-bin/test-site.py` and it should spit out the HTML for the website. The other way is to check directly in your browser following the same URL in the curl command (`http://127.0.0.1/cgi-bin/test-site.py`). Here, you should see the Hello World HTML text from the python script which confirms its all up and running.


# Using HTML Mockups inside the CGI

The python scripts `color-table.py` and `on-off.py` are simple coversions from the HTML Mockup into the python/cgi script that we can use to dynimcally generate our website. The idea here could be that we perform queries on the database and feed in specific parameters to the HTML code that is generated. This could easily be used in our simulation of the light bulb PRIOR to implementing it into the physical device. 

<br/>

What we can do for the simulation is create a webpage that has a picture of a lightbulb that we can change the color of. The python script (for simple testing purposes) can generate random RBG values using the values as parameters to generate a background color for the light bulb. In essence, this would mimic changing the color of the physical light bulb in our future implementation where we feed those parameters to the database AND the physical light bulb so that the physical state is changed and the web application will reflect the shared state when refreshing the page since it will perfrom the query on the database to generate the new HTML page.


