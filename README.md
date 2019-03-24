# Cloud-Based IoT Web API
CSC346 Project 2

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
<h2> Database </h2>
- MySQL for database, connected via Amazon RDS to our instances (WIP).
- Database will be its own instance.

<h2> Servers </h2>
- EC2 (~)


<h2> Web application </h2> 
- HTML generated through python scripts. 
- Idea: Break the development into stages...  
  <ol>
  <li>Simple button that controls on/off power for the bulb (amazon 'thing')  </li>
  <li>Querying the database for pre-set RBG values (maybe some rgb sliders) </li>
  <li>If possible, configure Amazon Alexa to have programmed commands for colors configs </li>
  </ol>
