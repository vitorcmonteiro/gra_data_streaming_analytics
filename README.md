# Introduction
The goal of this tutorial is to help you build your own Data Streaming app inside AWS with very few steps.

# Development environment
This app uses the following development environment:
* Windows 11 + Ubuntu 20.04 LTS (WSL2)
* Python 3.8.10 (WSL2)
* Docker (WSL2)
* VS Code (Windows)
* Code base (WSL2)

This setup allows you to work on your regular OS instead of using solely terminals while still able to harness the advantages of running your project inside a Linux distribution.

To achieve that, we will use VS Code with a plugin that allows us to develop a container living inside our WSL2 distribution. [^1]

# Tech Stack
* AWS Kinesis Firehose [^2][^3][^4]
* AWS S3 (Data Storage)
* AWS EC2 (Optional - Data Producer) [^5]
* Jupyter Notebook (Local Development)

It is very similar to the following tech stack but with less components because we are building a small solution to test Firehose.

![AWS Stack](https://user-images.githubusercontent.com/22838513/147084989-62058c7d-51b7-42b9-b67e-912652482bbd.png)


# Setting up your first data stream

This tutorial comprises the following key steps:<br>

1. [Installing Docker Inside WSL2](#installing-docker-inside-wsl2)
2. [Setup Development Environment](#setup-development-environment)
3. [Setup AWS Services](#setup-aws-services)
4. [Code Project & Test](#code-project-&-test)

## Installing Docker inside WSL2
You should install Docker Engine to run your project inside WSL2. I've followed the steps from Docker website ("Install using the repository" - Ubuntu). [^6]

After installing Docker Engine, give it a try: <br>
```
$ sudo dockerd
```

![dockerd initialized](https://user-images.githubusercontent.com/22838513/147085558-15778d8c-4f9e-4acc-af18-6552ebd9d52c.png)

In another terminal, type `$ docker` and you should see docker options:

![Docker helper](https://user-images.githubusercontent.com/22838513/147085427-97fd67b4-7fa3-4275-80d6-112c1b9ffe0e.png)
<br><br>

## Setup Development Environment
We are going through the following key steps:
1. Create folder and start project (virtual environment)
2. Install VS Code Extensions
3. Create your Container
4. Working inside your Container
<br><br>

### **Create folder and start project (virtual environment)**
First, we create the folder inside WSL2 to hold our project files: <br>
```
$ mkdir app
```
<br>

![mkdir](https://user-images.githubusercontent.com/22838513/147085224-e8f240e6-c503-4814-8435-4a67da250b35.png)

Now, inside the newly created folder, let's start a Python virtual environment so we have a blank slate to work with:

```
$ python3 -m venv env
```
<br>

![venv](https://user-images.githubusercontent.com/22838513/147085319-e744a1ef-2838-4729-87c9-f2c3f46fcf35.png)

This virtual environment will create a new Python environment linked to your original Python installation. This will ensure that we have a clean slate to install packages for each projects and keep the original Python installation. [^7]

```
$ source env/bin/activate
```
<br>

![env activated](https://user-images.githubusercontent.com/22838513/147085989-7dc10d60-6f08-4e96-98c3-67d400e6e73a.png)


You will notice there is a (env) at the beginning of every line. This indicates that we are using the virtual environment. Now we will install the packages we need:

`$ pip install boto3` <br>
`$ pip install Faker` <br>
`$ pip install numpy` <br>
`$ pip install json` <br>

* boto3 [^8] is used to use a broad range of AWS services through your Python code.
* Faker [^9] will enable us to generate fake data to be consumed by AWS Kinesis using Python code.
* Numpy [^10]

```
$ pip freeze >> requirements.txt
```
<br>

Inside your project folder there will be a file called *requirements.txt* which will hold all your Python Packages and their dependencies. This file will be used by Docker during the container build to reproduce the same environment you have in your project.

### 2. Install VS Code Extensions

For this solution we are going to use the "Remote - Containers" extension. This extension enables us to quickly create standardized Containers that we can code while it is running inside WSL2.

Although some versions may change as the versions evolve, your requirements.txt file should have boto3, Faker, and numpy listed somehwere:

![requirements.txt](https://user-images.githubusercontent.com/22838513/147086118-dcb031c1-f9ca-4e64-ae0f-f193de7f4849.png)
<br><br>

### **Install VS Code Extensions**
Second, we are going to use the "Remote - Containers" extension for VS Code. This extension enables us to quickly create Containers that we can code while it is running inside WSL2. Additionally, we will install a few extra extensions like Python and Jupyter to allow for Notebook programming.

You can search these extensions inside VS Code or using the following links:

* [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
<br><br>

### **Create your Container**
With the extensions installed make sure you are inside your project's main folder `~/repos/app` in my case and run the command `$ code .` to open VS Code at current folder. When the folder is openned, press `Ctrl + Shift + P` and you will see the following option:

![Add development container](https://user-images.githubusercontent.com/22838513/147086868-118cfa19-774a-4de3-83a4-28948423c142.png)

That menu will give you the most used standardized containers, but we will use one called **"Jupyter Data Science Notebooks"** that should appear under the **"Show All Definitions..."** option.

As soon as you click it, new files will be created inside the folder called `.devcontainer`.

![devcontainer folder](https://user-images.githubusercontent.com/22838513/147086958-b4e0dee7-a2cb-4e24-9459-a27db148f47a.png)

Dockerfile
: Steps Docker will take when you ask it to build the container (app). <br>
devcontainer.json
: This files contains configurations of the remote container ("Remote VS Code") that is going to run on WSL2. This will create your project inside a Docker Container thus creating a separate Linux distro inside your WSL2.

We won't get into details for each file, but it is important to make a quick edit to the `devcontainer.json` file. **Uncomment line 31** of this file where it runs the command "postCreateCommand". This will make sure pip installs all packages listed in the `requirements.txt` file when you run your container. 

After the files are created, VS Code will prompt you to build/reopen the container as a remote container because it noticed that you have a `.devcontainer` folder within your project. If that doesn't happen, you may use the following option (`Ctrl + Shift + P`) to manually run the build function:

![Reopen container](https://user-images.githubusercontent.com/22838513/147087082-d1182203-3b03-47a8-9ff1-9b7520a32a19.png)

Now we are inside the application (Container) we have created. It is a specific Linux distribution **INSIDE** the WSL2. When we tell VS Code to Reopen/Rebuild the container it will do the same thing as `docker build` does and immediately access the container within a new VS Code instance.

Observe that before running build command your VS Code indicated WSL as the current folder we are working in. After running, it changes to " Dev Container:

![before](https://user-images.githubusercontent.com/22838513/147087170-e9df634b-7cb6-4d01-8525-ef10756af72b.png) >> ![after](https://user-images.githubusercontent.com/22838513/147087179-f52af9fb-ca6c-43d0-a93e-05c74ecfd39e.png)
<br><br>

### **Working inside your Container**
After you successfully built your container, your Jupyter Server should be already running in the background. If you look at the Ports tab in VS Code, there is one application running:

![Jupyter Server running on port 8888](https://user-images.githubusercontent.com/22838513/144737177-905477ba-4e34-4f6e-ac07-3cddb7996b12.png)

However, if you access it directly through your web browser you will see an authentication screen. What you should do is run the following command **inside your container** (using VS Code Terminal) to list all Jupyter servers running in your machine: <br>

```
$ jupyter notebook list
```

With the following output we are able to access Jupyter directly through browser if you `CTRL+Left Click` the link:

![Jupyter server link](https://user-images.githubusercontent.com/22838513/144737167-065a163e-1d74-4d73-8819-b2a139dd12fc.png)

Since we are using VS Code, **you can create .ipynb files whithin your Container and any changes made will be translated to the files located in WSL2**. For now, our Container just contains the necessary files to build our technology stack. There are no Python or Jupyter notebook files.

Now your project has been created successfully! :smiley:
<br><br>

## Setup AWS Services
We move forward to finally creating our tech stack at AWS. These are the key steps:

1. Create data stream
2. Create delivery stream
<br><br>

Kinesis will be responsible to receiving the streaming data that we will generate locally (or via EC2 machine) and periodically adds that data buffer to a S3 folder hence it is called Firehose.

We can achieve this through [AWS Management Console](https://aws.amazon.com/console/) or boto3 Python library. Using AWS console is easier when we are handling a small project thus we are using boto3 specifically to access services that we created using AWS Management Console.

After logging in to your account, search for "Kinesis" (`ALT + S`) in the search bar. At the main screen you will see three different services:

* Kinesis Data Streams
* **Kinesis Data Firehose**
* Kinesis Data Analytics

We will focus on Data Firehose and Data Analytics. The former is responsible to buffer the streaming data and add it into a S3 bucket. The latter runs a small app that constantly queries (SQL) the incoming data - You may skip that if you wish so.

Also important to remember the data flow:

`Local Machine >> Data Stream >> Data Firehose >> S3 Bucket`
<br><br>

### **Create data stream**
Click `Create delivery stream` to get started. Below you find suggested minimum configurations that would minimize the costs of creating this data stream while still keeping the app working.

* Data stream name = streaming-analytics-app
* Capacity mode = Provisioned
    * Provisioned shards = 1

![Create data stream config](https://user-images.githubusercontent.com/22838513/147087376-b62b7566-5b3d-4347-b0e6-3b82b5639704.png)

With the data stream up, you should see that we divide into two categories: Data Producers and Data Consumers.

![Data Producers and Consumers](https://user-images.githubusercontent.com/22838513/147087431-b59af1df-928b-42a0-bac0-4ac3892806e0.png)

Data Producers
: Create records for the Kinesis Data Stream. May be your local machine, app, or EC2. This time, it will be our local machine.
Data Consumers
: Put records into a specific service like Firehose (S3) or Kinesis Data Analyatics. There may be several recipients depending on your app.
<br><br>

### **Create delivery stream**
Return to Kinesis' Dashboard and create a delivery stream (Data Firehose). You can read more about it in the `How it works` section in the next window. Select the following:

* Source = Direct PUT
* Destination = Amazon S3

A few sections will be added to the screen. Choose the Data Stream in the following section. You may keep the random Delivery stream name as it is.<br>

Now inside `Transform and convert records` we will configure the output of the stream to a parquet file. We enable `Convert record format` and choose output format as `Apache Parquet`:

![transform](https://user-images.githubusercontent.com/22838513/148641313-562fc398-4661-42fb-933b-7ce12e454bbc.png)

We will not get into details of AWS Glue, but it is Glue that takes the input and transforms it before sending to S3. To acoomplish that you will need to create a Database and Table inside clue and then associate that with this stream. <br>

Next we jump to the Destination settings. Select a S3 Bucket that you previously created or create a new one at this point.

Expand the `Buffer hints, compression and encryption` section to configure the buffer size. Here we define the data size or time before Firehose send it to S3. Set both to minium:

* Size = 1MB
* Interval = 60 seconds

Done. Create your new delivery stream. You have setup all required AWS services.
<br><br>

### **Create a Credential**
Before we move our focus out of AWS, in order to access AWS functionalities we just created from your Python code, you need to setup a credential using the IAM function of AWS. Just search for `IAM`.

![iam](https://user-images.githubusercontent.com/22838513/147087668-d5d15c4e-44c1-4518-9691-70ef23dba7b1.png)

On the left panel, navigate to Access Management >> Users >> Add users.

![user](https://user-images.githubusercontent.com/22838513/147087687-f9d8d0be-51c8-4242-ad58-aef688f12bc4.png)

You can name it however you want but make sure that `Access key - Programmatic access` is ticked. I chose `firehose_user` as the username.

Now we move to the permissions section. Choose `Attach existing policies directly` and search and select the following policies:

* AmazonKinesisAnalyticsFullAccess
* AmazonS3FullAccess

After choosing these two policies you may proceed until you reach out the review screen. Create user if you see these two policies. **DO NOT CLOSE THE FOLLOWING WINDOW.**

![firehose_user](https://user-images.githubusercontent.com/22838513/147087771-2ac6df5b-5995-401b-9629-4a81bd30c283.png)

Save `Access key ID` and `Secret access key` in a safe place because we will use them during next step. If you lost it or clicked next without saving the keys, you have to browse the user you want to recover the key and you are able to issue a new key at the Security credentials tab.
<br><br>

## Code Project & Test
This is the last section. Now we focus on the development of the Data Producer and Analyzing incoming data being saved in S3.

We will cover:

1. Create Credential folder and files
2. Code & Run Data Producer
3. Analyze generated data
<br><br>

## Create Credential files inside your project
Inside the .devcontainer folder, create a folder called .aws. Then inside this folder we should create two files without any extension:

config
: Default region and output type when interacting with AWS.

```
[default]
output = json
region = us-east-1
```

**Make sure the region matches all streams' regions and S3 region.**

credentials
: Tokens needed to access AWS services as a specific user. We obtained these keys during this tutorial.

```
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXX
```

We are saving inside `.devcontainer` folder because these files will be copied to our Container every time we build de solution. Thus, we need to edit `Dockerfile`. Add this code to your `Dockerfile`:

```
COPY .aws /home/jovyan/.aws
```

Rebuild & Run your Container like we did at the beginning of this tutorial. If VS Code throws an error due to not enough privileges, visit this webpage: https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user.
<br><br>

### **Code & Run Data Producer**
Create a new Python file. I've called it `send_captains_to_cloud.py`. This file will use Faker package to generate a data stream of ratings given by people to famous movies and series space Captains.

The code is as follows:

```python
#!/usr/bin/env python
import boto3
from faker import Faker
import random
import time
import json

DeliveryStreamName = 'PUT-S3-qrZbv'
client = boto3.client('firehose')
fake = Faker()

captains = [
    "Jean-Luc Picard",
    "James T. Kirk",
    "Han Solo",
    "Kathryn Janeway",
    "Malcolm Reynolds",
    "William Adama",
    "Turanga Leela",
    "Jacob Keyes",
    "Wilhuff Tarkin",
    "Christopher Pike",
    "David Bowman",
    "The Doctor",
    "John Robinson",
    "Khan Noonien Singh"
];

record = {}
while True:

    record['user'] = fake.name();
    if random.randint(1,100) < 5:
        record['favoritecaptain'] = "Neil Armstrong";
        record['rating'] = random.randint(7000,9000);
    else:
        record['favoritecaptain'] = random.choice(captains);
        record['rating'] = random.randint(1, 1000);
    record['timestamp'] = time.time();
    response = client.put_record(
        DeliveryStreamName=DeliveryStreamName,
        Record={
            'Data': json.dumps(record)
        }
    )
    print('Record: ' + str(record));
```
**Remember to change `DeliveryStreamName` variable at line 8 to match the Delivery Stream name generated by AWS in the previous section.**

Save the file and close. Let's give it a quick test, inside your Container (Terminal of VS Code):

`$ python3 send_captains_to_cloud.py` 

You should see records being printed on the console after they are sent to your delivery stream. Let it send data for 5 minutes and hit `CTRL+Z` to stop the running code. We will run it parallel to analyzing after we test if data really went to our S3 bucket.

Browse your S3 bucket using AWS Management Console and you should see a folder with this structure:

`Year >> Month >> Day >> Hour (UTC)`
<br><br>

### **Analyze generated data**
Open the Jupyter server in your browser and create a new notebook. We will test if that was sent to our bucket. First create a new Python 3 notebook. Now we want to create a connection to our S3 bucket containing thedata that we streamed for a few minutes in the previous step.

All codes for this particular steps may be found on the file analysis.ipynb provided with this tutorial.

Cell 1:
```python
import boto3

s3 = boto3.client('s3')

print(s3)
```

(#image)

This code will use the credentials file we created before in order to connect to AWS services and returns an object that contains that connection.
<br>

Cell 2:
```python
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
```

(#image)

This is the list of buckets I have on my S3 currently. For this specific example, I created a bucket called ```captains-rating```.

Now for the next cell we will use two functions that handle both reading a single file and recursively aggregating parquet files generated by the stream so we can analyze data further.

Cell 3:
```python
import boto3
import pandas as pd
import io

def pd_read_s3_parquet(key, bucket, s3_client=None, **args):
    if s3_client is None:
        s3_client = boto3.client('s3')
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    return pd.read_parquet(io.BytesIO(obj['Body'].read()), **args)

def pd_read_s3_multiple_parquets(filepath, bucket, s3=None, 
                                 s3_client=None, verbose=False, **args):
    if not filepath.endswith('/'):
        filepath = filepath + '/'  # Add '/' to the end
    if s3_client is None:
        s3_client = boto3.client('s3')
    if s3 is None:
        s3 = boto3.resource('s3')
    s3_keys = [item.key for item in s3.Bucket(bucket).objects.filter(Prefix=filepath)
               if item.key.endswith('.parquet')]
    if not s3_keys:
        print('No parquet found in', bucket, filepath)
    elif verbose:
        print('Load parquets:')
        for p in s3_keys: 
            print(p)
    dfs = [pd_read_s3_parquet(key, bucket=bucket, s3_client=s3_client, **args) 
           for key in s3_keys]
    return pd.concat(dfs, ignore_index=True)
```

Run this cell before running the next. These functions do the following:

pd_read_s3_parquet
:Read a single parquet file and transforms it into Panda's Data Frame.

pd_read_s3_multiple_parquets
:Read files recursively with the prior function.

Finally, we will indicate both bucket and path of the parquet files and print the first few rows.

Cell 4:
```python
df = pd_read_s3_multiple_parquets('ratings2022/01/08/06/', 'captains-rating')

print(df.head())
```

Now with those functions we can use pandas and numpy to analyze the data you may have however you see fit.
<br><br>

# References
[^1]: [VS Code Remote Containers Documentation](https://code.visualstudio.com/docs/remote/containers) <br>
[^2]: [AWS Kinesis Tutorial for Beginners](https://www.youtube.com/watch?v=rYbS5ihk_xg) <br>
[^3]: [AWS Documentation on Kinesis](https://docs.aws.amazon.com/solutions/latest/aws-streaming-data-solution-for-amazon-kinesis) <br>
[^4]: [AWS Documentation Getting Started with Kinesis](https://aws.amazon.com/kinesis/getting-started/?nc=sn&loc=3) <br>
[^5]: [Real Time Data Analysis with Kinesis and EC2](https://ruslanmv.com/blog/Real-Time-Data-Analysis-with-Kinesis-in-EC2) <br>
[^6]: [Install Docker from repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) <br>
[^7]: [Python venv documentation](https://docs.python.org/3/library/venv.html) <br>
[^8]: [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) <br>
[^9]: [Faker Documentation](https://faker.readthedocs.io/en/master/) <br>
[^10]: [NumPy Documentation](https://numpy.org/doc/) <br>
