import os
import boto3
from botocore.exceptions import NoCredentialsError

# Replace 'your-bucket-name' with the name of your S3 bucket
BUCKET_NAME = 'trickedex-training-data'

# Initialize a session using your AWS credentials and create a boto3 S3 client
session = boto3.Session()
s3 = session.client('s3')

def upload_to_s3(local_file, s3_key):
    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_key)
        print(f"Uploaded {local_file} to s3://{BUCKET_NAME}/{s3_key}")
    except NoCredentialsError:
        print("Error: Unable to locate AWS credentials.")

def upload_clips_to_s3(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.mp4'):
                local_file = os.path.join(root, file)
                s3_key = os.path.relpath(local_file, folder).replace('\\', '/')
                upload_to_s3(local_file, s3_key)

if __name__ == "__main__":
    upload_clips_to_s3('clips')
