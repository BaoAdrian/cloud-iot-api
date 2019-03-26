# Setting up Apache Webserver on local machine (***The following was done on Ubuntu 18.04***)
*Although this was created on an Ubuntu machine, it should still work similarly to setup and run on either macOS/Windows.*


```sudo apt update```

Install apache2 with ```sudo apt install apache2```

Check status of webserver (was active when I checked) ```sudo systemctl status apache2```

Navigated to ```127.0.0.1``` to see default Apache Webserver page to confirm it was active.


# Testing Apache With Basic 'Hello World' Website

On my machine, the folder I added a ```test.html``` file to was ```/var/www/html```. Here resides the ```index.html``` for the default Apache Webserver.

Created the following test file by running ```sudo vim /var/www/html/test.html``` which will open up the editor and I inserted this basic Hello World Site.

```html
<html>
  <body>
    <h1> Hello World </h1>
  </body>
</html>
```

Saved and exited the editor and navigated to ```127.0.0.1/test.html``` and confirmed the server picked up the new file.


# Integrating Mockups and Testing Locally using Apache Webserver

With apache webserver running (can be checked using the ```sudo systemctl status apache2``` command), created the following html files for the current mockups:

```sudo vim on-off.html``` <br/>
```sudo vim color-table.html```

Sudo was required here since the folder that is being modified required root permissions (that being ```/var/www/html```). See the corresponding folders above for the html code for each mockup along with images of their output to ```127.0.0.1/on-off.html``` and ```127.0.0.1/color-table.html``` respectively.
