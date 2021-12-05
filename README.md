# Introduction

## Development
For local development of this solution I used the following:
* Windows 11 + Ubuntu 20.04 LTS (WSL2)
* Python 3.8.10 (WSL2)
* Code base (WSL2)
* Docker (WSL2)
* VS Code (Windows)

There is a plugin in VS Code that allows us to develop in a live Container. You can read more here: https://code.visualstudio.com/docs/remote/containers

I like that setup because I can easily use my current OS instead of using terminals but we are still able to harness the flexbility and compability of a Linux distribution inside WSL2.

## AWS Stack

![image](https://user-images.githubusercontent.com/22838513/144736978-57f4a665-8f2d-4ff1-ba6c-eb3499e2eec5.png)


# Setting up your first data stream

## Creating your Container
We are going throught the following steps:
1. Create folder and start project (virtual environment)
2. Install VS Code Extensions
3. Create Python3 + Jupyter Container

### 1. Create folder and start project (virtual environment)
---
Create the folder that is going to hold your project inside WSL2:<br>
`$ mkdir app`

Now, inside the new folder, let's create Python's virtual environment so we have a blank slate to work with:

`$ python3 -m venv env` <br>

`$ source env/bin/activate` <br>

You will notice there is a (env) at the beginning of every line. This indicates that we are using the virtual environment. Now we will install the packages we need:

`$ pip install boto3` <br>
`$ pip install Faker` <br>
`$ pip install numpy` <br>

`$ pip freeze >> requirements.txt` <br>

### 2. Install VS Code Extensions
---
For this solution we are going to use the "Remote - Containers" extension. This extension enables us to quickly create standardized Containers that we can code while it is running inside WSL2.

Remote - Containers: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers <br>
Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python <br>
Jupyter: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter <br>

### 3. Create Python3 + Jupyter Container
---
With the folder created, just run the command `$ code .` to open VS Code at that folder. When the folder is openned, press `Ctrl + Shift + p` and you can see the following option:

[ ] Add images <br>
(Add Development Container Configuration Files...) <br>
(Show All Definitions...)<br>

You can see there are dozens of different stacks built-in and these are completely customizable, just like Docker itself. We will choose the "Jupyter Data Science Notebooks" option.

As soon as you click it, new files will be created inside the folder .devcontainer. <br>

Dockerfile
: Steps taken when you build the container.
<br>
devcontainer.json
: This files contains configurations of the remote container that is going to run on WSL2's Docker Engine.

(Reopen in Container)

Now we are inside the application (Container) we have created. It is a specific Linux distribution **INSIDE** the WSL2. When we tell VS Code to Reopen/Rebuild the container it will do the same thing as `docker build` does and immediately access the container within a new VS Code instance.

## Working inside your Container
---
After you successfully build your container, your Jupyter Server should be already running. If you look at the Ports tab in VS Code, there is one application running:
![image](https://user-images.githubusercontent.com/22838513/144737177-905477ba-4e34-4f6e-ac07-3cddb7996b12.png)

However, if you access it directly through your web browser you will see a authentication screen. What you should do is run the following command **inside your container** to list all Jupyter servers running in your machine:<br>

``` jupyter notebook list ```

With the following output we are able to access Jupyter directly through browser if you click the link:

![image](https://user-images.githubusercontent.com/22838513/144737167-065a163e-1d74-4d73-8819-b2a139dd12fc.png)

Since we are using VS Code, **you can create .ipynb files whithin your Container and any changes made will be translated to the files located in WSL2** (Or to whatever folder you have run your build command).

For now, our Container just contains the necessary files to build our technology stack. There are no python or jupyter notebook files.

## Create Firehose data stream
---
We can achieve this through AWS Console Panel or through boto3 Python library. Using AWS console is easier when we are handling a small project:



## Create Credential files inside your project
---
Inside the .devcontainer folder, create a folder called .aws. Then inside this folder we should create two files without any extension:

config
: Default region and output type when interacting with AWS.

```
[default]
output = json
region = us-east-1
```

credentials
: Tokens needed to access AWS services as a specific user.

```
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXX
```
The packages boto3 will use these information interact with AWS' services.

# References
https://www.youtube.com/watch?v=rYbS5ihk_xg<br>
https://docs.aws.amazon.com/solutions/latest/aws-streaming-data-solution-for-amazon-kinesis<br>
https://aws.amazon.com/kinesis/getting-started/?nc=sn&loc=3<br>
https://faun.pub/apache-kafka-vs-apache-kinesis-57a3d585ef78<br>
https://ruslanmv.com/blog/Real-Time-Data-Analysis-with-Kinesis-in-EC2<br>
https://www.ioconnectservices.com/insight/using-lambda-and-the-new-firehose-console-to-transform-data<br>