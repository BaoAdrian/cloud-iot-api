# Testing how to integrate CGI with Python on Apache Webserver

*Note that the following was done on a machine running Ubuntu 18.04*

*Currently a Work-in-progress*

URL provided in specifications for setup: http://httpd.apache.org/docs/2.2/howto/cgi.html


With Apache Webserver running, find the corresponding .conf file to modify the acceptable scripts. In my case, since apache2 was installed on my Ubuntu machine, this was located at ```etc/apache2/conf-available/serve-cgi-bin.conf```. Modified/added the commands/directives explained in the webpage (currently still not working). 

Once that was setup, reloaded apache server by running ```sudo service apache reload``` and verifying it was back up and running using the command ```sudo systemctl status apache2```. 

Once that was verified, navigated to the directory where the cgi scripts should be stored ```/usr/lib/cgi-bin/```. Created the following scipts (bash, cgi, python) to see what was accepted by apache in the current state: <br/>
```test-site.sh```<br/>
```test-site.cgi```<br/>
```test-site-py```<br/>

When running any of these scripts, they first need to be made executable using ```sudo chmod a+x <script_name>``` and the output can be tested directly in the terminal using ```curl http://127.0.0.1/cgi-bin/test-site.sh```. The output for this command is the following:
```
Hello World!
```

This was working fine, however, when the configs were adjusted to accept .py and .cgi scripts, I could not get past the 500 Internal Server Error or the 403 Forbidden Error despite adjusting permissions, checking error logs (located at ```/var/logs/apache2/error.log```).

# Current State

As it is currently in the repo, the bash script works fine, the cgi (untested) and python (403 Error) scripts are currently not working.
