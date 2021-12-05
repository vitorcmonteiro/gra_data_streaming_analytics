# Simple script to create a kinesis stream
# create-stream.py
import boto3

client = boto3.client('firehose')

s3_config = {
   'BucketARN': 'arn:aws:s3:::streaming-analytics-gra',
   'RoleARN': 'arn:aws:iam::009176705115:role/service-role/KinesisFirehoseServiceRole-PUT-S3-zUZXi-us-east-1-1638602963072',
   'BufferingHints': {
      'IntervalInSeconds': 60,
   },
}

response = client.create_delivery_stream(
   DeliveryStreamName='vcm_analytics_gra_stream',
   DeliveryStreamType='DirectPut',
   ExtendedS3DestinationConfiguration=s3_config
)