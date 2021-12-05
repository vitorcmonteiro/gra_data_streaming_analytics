# Simple script to create a kinesis stream
# create-stream.py
import boto3

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName='vcm_analytics_gra_stream',
   ShardCount=1
)