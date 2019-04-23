import boto3

from pzdata.urltos3 import S3UrlImporter
from pzdata.wrangler import Ml100kWrangler


# TODO: Tie it all together
'''
SOURCE_DATA_URL = 'http://files.grouplens.org/datasets/movielens/ml-100k.zip'
TEMP_S3_BUCKET = 'pzdata-temp-' + boto3.client('sts').get_caller_identity().get('Account')
DEST_KEY = '2019-04-23T04:02:25-pzdata.csv'
SOURCE_KEY = '2019-04-23T04:02:25-ml-100k.zip'
DEST_KEY = '2019-04-23T04:02:25-pzdata.csv'

s3UrlImporter = S3UrlImporter(SOURCE_DATA_URL, TEMP_S3_BUCKET)
s3UrlImporter.destroy_bucket()
response = s3UrlImporter.url_to_s3()

ML100K_KEY = response.split('/')[-1]

ml100Wrangler = Ml100kWrangler(BUCKET, SOURCE_KEY, DEST_KEY)
ml100Wrangler.pzdata_etl()
'''


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
