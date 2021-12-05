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
