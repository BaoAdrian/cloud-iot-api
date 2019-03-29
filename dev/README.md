# Development Environment for Web Application

This repo will serve as the development environment that we will use when cloning the repo inside the EC2 Instance.


# Getting Started

Launch the EC2 Insance and ssh into the instance using your `.pem` file.

Once inside (assuming the EC2 instance is configured with all the required libraries and dependencies), you will be in the home directoy where you can then clone this repo. Copy the `git` url and run `git clone <repo.git>` inside the instance. 

Since all we are going to use inside the instance are the python scripts (located inside our `dev` subdirectory), you can simply copy the scripts into the necessary file for the Apache Webserver to pick them up and utilize them. 

Change directory into `dev/` and run `cp ./* /var/www/cgi-bin/` to copy all of the scripts inside the development folder into the `cgi-bin` that the webserver will use to run our application. 

Once those are copied over, change directories to `/var/www/cgi-bin` and modify the IP address inside the ip.py file to the IP address of the EC2 instance that you are running in. This is so that the rest of the python scripts can automatically pick up that new IP address instead of having to change them in each individual one.

