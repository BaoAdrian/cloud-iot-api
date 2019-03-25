# Cloud-Based IoT Web API
CSC346 Project 2

Specifications: https://lecturer-russ.appspot.com/classes/cs346/spring19/projects/proj02.pdf

# Helpful Links
This link contains an API that we might be able to use to control the state of the lightbulb:
https://iot.mozilla.org/things/

This link shows Amazons IoT Management platform that we could possibly use to manage the devices using AWS.
https://aws.amazon.com/iot-device-management/

Maybe we can integrate one of these buttons once we get it working. Could do some cool stuff with it. https://aws.amazon.com/iotbutton/ 



# Video Examples
Here is a tutorial on connecting an IoT device and managing it using their dashboard. Not quite related to what we are trying to do since he is using JavaScript and some Edison device/ Robot Sphere but interesting to see how to interact with the console to 'develop' and 'test' the implementation.
https://www.youtube.com/watch?v=_0us6NzlaoQ



# Brainstorm
<h2> Servers </h2>
https://aws.amazon.com/ec2/

- 2 EC2 Instance that will have the python/html code installed with all dependencies on them and will point to the RDS DB Instance when connecting to MySQL Database.


<h2> Web application </h2> 
- HTML generated through python scripts. 
- Idea: Break the development into stages...  
  <ol>
  <li>Simple button that controls on/off power for the bulb (amazon 'thing')  </li>
  <li>Querying the database for pre-set RBG values (maybe some rgb sliders) </li>
  <li>If possible, configure Amazon Alexa to have programmed commands for colors configs </li>
  </ol>
  
  
<h2> Amazon MySQL DB </h2> 
  https://aws.amazon.com/getting-started/tutorials/create-mysql-db/
- MySQL for database, connected via Amazon RDS to our instances (WIP).
- Database will be its own instance.
  
  <li>username: Admin password: project2password</li>
  <li>Endpoint: project2-iot-lightbulb.ccdjm6mfovyw.us-west-1.rds.amazonaws.com</li>
  <li>DBName: project2-iot-lightbulb</li>


# Development
<h3> Database </h3>
- [x] Create MySQL DB Instance
- [x] Link DB Instance to MySQL Workbench
- [ ] Save important params for access into the python web application
<h3> Server </h3>
- [x] Successfully launch Amazon EC2 
- [ ] Install python application on EC2 instances
  - [ ] Connect DB instance to EC2 instances   
<h3> Web Application </h3>
- [ ] Mockup
- [ ] CGI/Python application that generates HTML
  - [ ] On/Off swith
  - [ ] Table of RGB Configs & RGB Slider & Brightness/Saturation Slider
  - [ ] Possible integration with Amazon Alexa

