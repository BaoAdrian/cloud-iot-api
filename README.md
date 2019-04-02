# Cloud-Based IoT Web API
Cloud-serviced web application aimed to manage and utilize Internet-of-Things devices using Python, Amazon AWS, and a MySQL Database.

Specifications: https://lecturer-russ.appspot.com/classes/cs346/spring19/projects/proj02.pdf

# Project Description
There are three main parts for this application. 
<ol>
  <li> MySQL Database </li>
  <li> Amazon EC2 Instances Running Apache Webserver </li>
  <li> Python/HTML Web Application </li>
</ol>

This project will utilize the Amazon AWS Platform to spin up two mirrored EC2 Instances running Apache Webserver and one RDS MySQL Database Instance serve as the backend data persistance for the the Python/HTML web application that will be cloned into each instance from this repository (dev folder). The Web Application that is generated through the webserver will be broadcasted to specific IP Addresses that can be accessible via a web browser. The CGI framework for Python is used to generate the HTML code for the various pages and more information on configuring that inside the instance can be found in the `README.md` inside the `dev` folder.



# Helpful Links
This link contains an API that we might be able to use to control the state of the lightbulb:
https://iot.mozilla.org/things/

This link shows Amazons IoT Management platform that we could possibly use to manage the devices using AWS.
https://aws.amazon.com/iot-device-management/

Maybe we can integrate one of these buttons once we get it working. Could do some cool stuff with it. https://aws.amazon.com/iotbutton/ 


# Section Details
<h3> Servers </h3>
Two mirrored Amazon EC2 Instances running Apache Webservers will have our Web Application installed from this repository into each instance. Each instance will independently point to the RDS DB Instance when connecting to MySQL Database. 

Reference: https://aws.amazon.com/ec2/

<br/>


The EC2 Instances used to run the application were the ones created from Project 2 with all configurations already set. SSH'd into the instance by running the follwing:


```
ssh -i /path/to/private-key.pem ec2-user@<Public DNS (IPv4)>
```


Once successfully inside the instance, ran the following install commands to configure the dependencies needed for this project:

```sudo yum install python3```<br/>
```sudo yum install mariadb```<br/>
```sudo yum install mariadb-devel```<br/>
```sudo yum install gcc```<br/>
```sudo yum install python3-devel``` (Required prior to pip3 install command)<br/>
```sudo pip3 install mysqlclient```<br/>
```sudo yum install git```<br/>
```sudo yum install MySQL-python``` (Used to interface with RDS DB Instance)<br/>

Note that httpd is already installed within the linux-based instance so there are no further installation requirements to be done for the webservers. (See `dev` for webserver configuration for this project).

<h3> Web application </h3> 
The web application will serve as a series of simulators of the application interfacing with IoT devices. The main goal with this project is to create an application that will allow for an easy introduction to interfacing with IoT devices, with our main focal point being Smart Lightbulbs.  
Will break the development into stages...  

- [x] Welcome page that serves as a starting hub to our various services (scripts below)
- [x] Simple button that controls on/off power for the bulb (on-off.py)
- [x] Presenting user with pre-configured RGB settings attached to a table of buttons (color-table.py) 
- [ ] Various sliders to configure RGB settings as well as opacity and brightness (sliders.py)
= [x] Robust simulator that presents Scalable Vector Graphic of a house with various room in which the web application can interacty with individual rooms and set their RGB settings. (house-simulator.py)

Resources used throughout the development process:

  
  
<h3> Amazon MySQL DB </h3> 
  https://aws.amazon.com/getting-started/tutorials/create-mysql-db/
- Amazon RDS Database Instance that will serve as the backend between the two servers that point to it. Store the various tables used throughout the application for the various simulators used to interface with (at the moment) virtual IoT devices.

<ul>  
  <li>Endpoint: project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com</li>
  <li>username: Admin </li>
  <li>password: project2password</li>
  <li>DBName: project2db</li>
  <li>Linking the EC2 instances to the AWS RDS DB.</li>
   - https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html
  <li>W3Schools SQL.</li>
  -https://www.w3schools.com/sql/
</ul>

# Development - Milestones
Database:
- [x] Create MySQL DB Instance 
- [x] Link DB Instance to MySQL Workbench
- [x] Save important params for access into the python web application


Server:
- [x] Successfully launch Amazon EC2 
- [x] Install dependencies on the EC2 Instance (see above for steps to complete)
- [x] Install python application on EC2 instances
- [x] Connect DB instance to EC2 instances   


Web Application:
- [x] HTML Mockup
- [x] CGI/Python application that generates HTML
  - [x] On/Off swith
  - [x] Table of RGB Configs
  - [ ] RGB/Opacity/Brightness Sliders (https://www.w3schools.com/howto/howto_js_rangeslider.asp)
  - [x] House Simulator

Miscellaneous:
- [ ] Investigate integration with the Amazon IoT Core API to interact with IoT devices.
EDIT: It appears as though the student account generated for the course does not have access to utilize this part of the AWS platform. Additionally, other resources for interacting with IoT devices required a Rasberry PI which we did not have at the time of completing this assignment.
