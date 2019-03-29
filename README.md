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

This project will use Amazon AWS for the MySQL Database Instance and two EC2 Instances that will run the Apache Webserver for the Python/HTML application that will be installed into each individual instance. The Web Application that is generated through the webserver will be broadcast to specific IP Addresses that can be accessible via an web browser. Since we will be running two EC2 Instances running these Apache Webservers, we will only have two IP Addresses that we can access the application through.



# Helpful Links
This link contains an API that we might be able to use to control the state of the lightbulb:
https://iot.mozilla.org/things/

This link shows Amazons IoT Management platform that we could possibly use to manage the devices using AWS.
https://aws.amazon.com/iot-device-management/

Maybe we can integrate one of these buttons once we get it working. Could do some cool stuff with it. https://aws.amazon.com/iotbutton/ 



# Video Examples
Here is a tutorial on connecting an IoT device and managing it using their dashboard. Not quite related to what we are trying to do since he is using JavaScript and some Edison device/ Robot Sphere but interesting to see how to interact with the console to 'develop' and 'test' the implementation.
https://www.youtube.com/watch?v=_0us6NzlaoQ



# Section Details
<h3> Servers </h3>
2 EC2 Instance that will have the python/html code installed with all dependencies on them and will point to the RDS DB Instance when connecting to MySQL Database. URL: https://aws.amazon.com/ec2/

<br/>



Setting up the server (utilized the EC2 instance created for Project 2). SSH'd into by first changing directory to the location where my ```key-pair-name.pem```file was located. (Also assuming you have completed the necessary configs described when clicking ```Connect``` next to Instance Actions).

Run ```ssh -i "key-pair-name.pem" ec2-user@<Public DNS (IPv4)>```

Once successfully inside the instance, ran the following install commands to configure the dependencies needed for this project:

```sudo yum install python3```<br/>
```sudo yum install mariadb```<br/>
```sudo yum install mariadb-devel```<br/>
```sudo yum install gcc```<br/>
```sudo yum install python3-devel``` (Required prior to pip3 install command)<br/>
```sudo pip3 install mysqlclient```<br/>
```sudo yum install git```<br/>
```sudo yum install MySQL-python```<br/>


<h3> Web application </h3> 
HTML generated through python scripts using the CGI framework. 
Will break the development into stages...  

- [ ] Simple button that controls on/off power for the bulb (amazon 'thing')
- [ ] Querying the database for pre-set RBG values (maybe some rgb sliders) 
- [ ] If possible, configure Amazon Alexa to have programmed commands for colors configs
  
  
<h3> Amazon MySQL DB </h3> 
  https://aws.amazon.com/getting-started/tutorials/create-mysql-db/
- MySQL for database, connected via Amazon RDS to our instances (WIP).
- Database will be its own instance.

<ul>  
  <li>Endpoint: project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com</li>
  <li>username: Admin </li>
  <li>password: project2password</li>
  <li>DBName: project2-iot-lightbulb</li>
</ul>

# Development - Milestones
Database:
- [x] Create MySQL DB Instance 
- [x] Link DB Instance to MySQL Workbench
- [x] Save important params for access into the python web application


Server:
- [x] Successfully launch Amazon EC2 
- [x] Install dependencies on the EC2 Instance (see above for steps to complete)
- [ ] Install python application on EC2 instances
  - [ ] Connect DB instance to EC2 instances   


Web Application:
- [x] HTML Mockup
- [ ] CGI/Python application that generates HTML
  - [ ] On/Off swith
  - [ ] Table of RGB Configs & RGB Slider & Brightness/Saturation Slider (https://www.w3schools.com/howto/howto_js_rangeslider.asp)
  - [ ] Possible integration with Amazon Alexa


Miscellaneous:
- [ ] Figure out if Amazon IoT Management API is required to handle communication between device and web application. (I.E. register device as 'thing' in the API and perform calls to database through interface.
