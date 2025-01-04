# This is code sample to showcase CodeWhisperer
# It is not a complete solution, but it is a good starting point.

import boto3
import json

if __name__ == '__main__':
    # Establish connection to AWS account,  using IAM role
    # If you are not using IAM role, please replace the following line with
    # boto3.setup_default_session(profile_name='your_profile_name')
    boto3.setup_default_session(profile_name='gsq-magnus-devo')


    # Connect to S3 bucket at my AWS account
    s3 = boto3.resource('s3')
    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

    # Create a new bucket
    s3.create_bucket(Bucket='my-new-bucket')

    # Upload a file to the bucket
    data = open('code_whisperer_demo.py', 'rb')
    s3.Bucket('my-new-bucket').put_object(Key='code_whisperer_demo.py', Body=data)
    data.close()
    print('Upload complete')

    # Download a file from the bucket
    s3.Bucket('my-new-bucket').download_file('code_whisperer_demo.py', 'code_whisperer_demo_downloaded.py')

    print('Download complete')
    print('You can now run the following command:')
