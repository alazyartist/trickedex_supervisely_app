import boto3
import labelbox
import os

# Initialize a session using your AWS credentials and create a boto3 S3 client
session = boto3.Session()
s3 = session.client('s3')

# Set up Labelbox credentials
LABELBOX_API_KEY = 'YOUR_API_KEY'
client = labelbox.Client(api_key=LABELBOX_API_KEY)

# Set up dataset information
DATASET_NAME = 'YOUR_DATASET_NAME'
DATASET_DESCRIPTION = 'YOUR_DATASET_DESCRIPTION'
DATASET_TYPE = labelbox.enums.DatasetType.VIDEO_DATA

# Create the dataset in Labelbox
dataset = client.create_dataset(name=DATASET_NAME, type=DATASET_TYPE, description=DATASET_DESCRIPTION)

# Set up S3 bucket information
S3_BUCKET_NAME = 'YOUR_BUCKET_NAME'
S3_PREFIX = 'YOUR_PREFIX'

# List all files in the S3 bucket with the specified prefix
response = s3.list_objects_v2(Bucket=S3_BUCKET_NAME, Prefix=S3_PREFIX)

# Loop through each file in the bucket and upload it to the Labelbox dataset
for obj in response['Contents']:
    file_name = obj['Key']
    file_url = f's3://{S3_BUCKET_NAME}/{file_name}'
    data_row = labelbox.DataRow(row_data=file_url)
    dataset.create_data_rows([data_row])