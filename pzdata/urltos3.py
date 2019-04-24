import datetime

import boto3
from botocore.exceptions import ClientError
import requests


class S3UrlImporter:
    def __init__(self, url, bucket_name):
        self.url = url
        self.bucket_name = bucket_name

    def destroy_bucket(self):
        try:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(self.bucket_name)

            if bucket.creation_date:
                bucket.objects.all().delete()
                bucket.delete()
                print('[destroy_bucket] ' + self.bucket_name + ' deleted.')
        
        except:
            print(ClientError)

    def url_to_s3(self):
        timestamp = datetime.datetime.utcnow().isoformat(timespec='seconds')
        s3_key = timestamp + '-' + self.url.split('/')[-1]
        
        r = requests.get(self.url, stream=True)
        mb = '{:.1f}'.format((int(r.headers.get('content-length')) / 1048576))

        try:
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(self.bucket_name)

            bucket.create()
            print('[url_to_s3] ' + self.bucket_name + ' created.')

            print('[url_to_s3] Transferring file of size ' + mb + ' MB...')
            bucket.upload_fileobj(r.raw, s3_key)
            print('[url_to_s3] Done.')

            return s3_key
        
        except:
            print(ClientError)






'''
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
'''