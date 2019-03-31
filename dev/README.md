# Development Environment for Web Application

This repo will serve as the development environment that we will use when cloning the repo inside the EC2 Instance.


# Getting Started

In order to get the web application running on the EC2 Instances, there are a number of steps that need to be completed to get it running.

## Launching Instance and Cloning Repo

Launch the EC2 Instance and ssh into the instance using your `.pem` file.

Once inside (assuming the EC2 instance is configured with all the required libraries and dependencies), you will be in the home directoy where you can then clone this repo. Copy the `git` url and run `git clone <repo.git>` inside the instance.  

Also as a sanity check, you can ensure that your webserver is active and running using `sudo systemctl status httpd`.

## Copy scripts into cgi-bin

Change directory into `dev/` and run `cp ./*.py /var/www/cgi-bin/` to copy all of the python scripts inside the dev folder into the `cgi-bin` that the webserver will use to run our application. 

With all the necessary scripts copied over into the correct directory, run `cd /var/www/cgi-bin` and proceed to the next steps to configure the new IP address and make scripts executable


## Configure Scripts & IP Address for EC2 Instance

Modify the IP address inside the `ip.py` file to the IP address of the EC2 instance (Public DNS IPv4) that you are running in. In my case, I changed the `IP_ADDR` var to `ec2-34-226-218-189.compute-1.amazonaws.com`. This is so that the rest of the python scripts used for the web application can automatically pick up that new IP address instead of having to change them in each individual one.

Once that is completed and saved, run `sudo chmod o+x *.py` to make all of the scripts within the current directory executable. Now we can run the web application inside the EC2 instance.

Open your web browser and you should be able to view the web application following the URL in your configuration. In my case, this was the following URL:

```
http://ec2-34-226-218-189.compute-1.amazonaws.com/cgi-bin/welcome.py
```

But in general for any instance, it should be the following (where IP_ADDR is the var you set for your specific instance):

```
http://IP_ADDR/cgi-bin/welcome.py
```

This should now reflect the live web application in your browser and any changes made within the instance will be immediately reflected in the web application.


## Creating a dev environment within the instance

Creating a dev environment inside the instance with Git makes things a lot easier to control the workflow. Instead of having to remove files and re-cloning the repo every time a change is made, you can create a remote repository and manage your changes in the instance. 

To do this, inside your instance, navigate to where you have your cloned repo and `cd` into `cloud-iot-api`. 

Once inside, you can run `git remote add upstream https://github.com/<USERNAME>/cloud-iot-api.git` where you insert your github username. Now that you have a remote repository set up that is linked to the master branch, you can make changes locally on your machine and push them into the main branch with the following steps:

`Make changes`

`git add <FILES CHANGED>`

`git commit -m "<MESSAGE>`

`git push -u origin master`

And now these changes will be reflected in the master branch for the rest of the team to see the changes.

If someone makes a change to the master branch and your remote repository is 'behind' the master branch, simply run `git pull` which will update your remote repository to the current state of the master branch. 

## Setting up hard links for files in cgi-bin

Since we will have two seperate locations inside the instance where we have our python scripts, it would be incredibly tedious to have to keep track of changes made to both sets. By both sets, I mean the scripts inside `/var/www/cgi-bin` and inside the `cloud-iot-api/dev` cloned repo folder. To combat this, you can set HARD LINKS to the files that are in both these folders. This will basically allow for any changes made to one file be immediately reflected on the other. This will allow for us to simply make changes inside our repo rather than having to change directories to the cgi-bin everytime. 

To do this, navigate to the `dev` folder where the original python scripts are. Assuming you have already copied over the scripts to the `/var/www/cgi-bin` folder, you can set the hard link by running the following

```
sudo ln -f <SCRIPT> /var/www/cgi-bin/<SCRIPT>
```

For example:

```
sudo ln -f on-off.py /var/www/cgi-bin/on-off.py
```

This will link the on-off.py script inside the `dev` folder to the one located in `/var/www/cgi-bin`. The `-f` flag forces the link command to overwrite any script that is already in there (which in our case, we have scripts copied there already so this simply overwrites them with the newly linked files). 

Now any changes made inside the `cloud-iot-api/dev` folder will be reflected in both locations and will also be immediately reflected when refreshing the browser.

See this StackExchange answer for more info: https://unix.stackexchange.com/a/295629


## Logging into mysql through the terminal

Inside the EC2 instance with the MySQL RDS Instance up and running, you can use the following command with the credentials for the given database.

```
mysql -u <USERNAME> -h <HOST/ENDPOINT> -p
```

It will then prompt for the password and should end up inside the interactive shell for the mysql database.

