# test_r2.py
# Tests the Cloudflare R2 connection by uploading a text file to an R2 bucket and retrieving it to verify object storage works.

import os
import boto3
from dotenv import load_dotenv

# Loads environment variables from the .env file.
load_dotenv()

# Retrieves Cloudflare R2 credentials and bucket configuration.
account_id = os.environ["R2_ACCOUNT_ID"]
access_key = os.environ["R2_ACCESS_KEY_ID"]
secret_key = os.environ["R2_SECRET_ACCESS_KEY"]
bucket_name = os.environ["R2_BUCKET_NAME"]

# Creates an S3-compatible client configured to communicate with Cloudflare R2.
client = boto3.client(
  "s3",
  endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
  aws_access_key_id=access_key,
  aws_secret_access_key=secret_key,
  region_name="auto",
)

# Uploads a test text file to the configured R2 bucket.
client.put_object(
  Bucket=bucket_name,
  Key="framework-test.txt",
  Body=b"Cloudflare R2 connection successful",
  ContentType="text/plain",
)

# Retrieves the uploaded test file from the R2 bucket.
response = client.get_object(
  Bucket=bucket_name,
  Key="framework-test.txt",
)

# Reads and prints the retrieved file contents to verify the upload succeeded.
print(response["Body"].read().decode())