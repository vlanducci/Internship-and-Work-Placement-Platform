import os
import boto3
from dotenv import load_dotenv

load_dotenv()

account_id = os.environ["R2_ACCOUNT_ID"]
access_key = os.environ["R2_ACCESS_KEY_ID"]
secret_key = os.environ["R2_SECRET_ACCESS_KEY"]
bucket_name = os.environ["R2_BUCKET_NAME"]

client = boto3.client(
  "s3",
  endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
  aws_access_key_id=access_key,
  aws_secret_access_key=secret_key,
  region_name="auto",
)

client.put_object(
  Bucket=bucket_name,
  Key="framework-test.txt",
  Body=b"Cloudflare R2 connection successful",
  ContentType="text/plain",
)

response = client.get_object(
  Bucket=bucket_name,
  Key="framework-test.txt",
)

print(response["Body"].read().decode())