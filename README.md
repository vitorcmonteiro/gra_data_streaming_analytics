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

## Running your Container
After you successfully build your container, your Jupyter Server should be already running. If you look at the Ports tab in VS Code, there is one application running:
![image](https://user-images.githubusercontent.com/22838513/144737177-905477ba-4e34-4f6e-ac07-3cddb7996b12.png)

However, if you access it directly through your web browser you will see a authentication screen. What you should do is run the following command **inside your container** to list all Jupyter servers running in your machine:<br>

``` jupyter notebook list ```

With the following output we are able to access Jupyter directly through browser if you click the link:
![image](https://user-images.githubusercontent.com/22838513/144737167-065a163e-1d74-4d73-8819-b2a139dd12fc.png)

Since we are using VS Code, **you can create .ipynb files whithin your Container and any changes made will be translated to the files located in WSL2** (Or to whatever folder you have run your build command).

For now, our Container just contains the necessary files to build our technology stack. There are no python or jupyter notebook files.

## Create Firehose data stream
We can achieve this through

```
|Project root folder
├── .devcontainer
│   ├── .aws
│   ├── Dockerfile
│   ├── devcontainer.json
│   ├── library-scripts
│   └── requirements.txt
├── .gitignore
├── README.md
├── create-stream.py
├── data_generator
│   └── send_captains_to_cloud.py
├── env
├── notebooks
│   └── tests.ipynb

```
# References
https://www.youtube.com/watch?v=rYbS5ihk_xg<br>
https://docs.aws.amazon.com/solutions/latest/aws-streaming-data-solution-for-amazon-kinesis<br>
https://aws.amazon.com/kinesis/getting-started/?nc=sn&loc=3<br>
https://faun.pub/apache-kafka-vs-apache-kinesis-57a3d585ef78<br>
https://ruslanmv.com/blog/Real-Time-Data-Analysis-with-Kinesis-in-EC2<br>
https://www.ioconnectservices.com/insight/using-lambda-and-the-new-firehose-console-to-transform-data<br>
