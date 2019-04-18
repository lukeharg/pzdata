import datetime

import requests
import boto3
from botocore.exceptions import ClientError


SOURCE_DATA_URL = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
TEMP_S3_BUCKET = 'pzdata-temp-' + boto3.client('sts').get_caller_identity().get('Account')


# TODO: Download datafile from URL to S3 bucket
def url_to_s3(url, bucket_name):
    S3_KEY = url.split('/')[-1]
    r = requests.get(url, stream=True)

    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)

        if bucket.creation_date:
            response = bucket.objects.all().delete()
            print(response)
            response = bucket.delete()
            print(response)
        
        response = bucket.create()
        print(response)

        response = bucket.upload_fileobj(r.raw, S3_KEY)
        print(response)
    
    except:
        print(ClientError)





# TODO: Wrangle user data into Personalize Format

# TODO: Create a Personaize campaign

#print(datetime.datetime.utcnow())

url_to_s3(SOURCE_DATA_URL, TEMP_S3_BUCKET)


''' print('Hi')
TIMESTAMP = '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now())

s3 = boto3.resource('s3')
client = boto3.client('s3')

bucket_iterator = s3.buckets.all()
response = client.list_buckets()

for bucketname in response['Buckets']:
    print(bucketname['Name'])


personalize = boto3.client(service_name='personalize', endpoint_url='https://personalize.us-east-1.amazonaws.com', region_name='us-east-1')
personalize_runtime = boto3.client(service_name='personalize-runtime', endpoint_url='https://personalize-runtime.us-east-1.amazonaws.com', region_name='us-east-1')

list_recipes_response = personalize.list_datasets()

print(list_recipes_response)

print(boto3.client('sts').get_caller_identity().get('Account')) '''
