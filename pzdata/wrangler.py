import zipfile
import io

import boto3
import pandas


class Ml100kWrangler:
    def __init__(self, bucket_name, source_key, dest_key):
        self.bucket_name = bucket_name
        self.source_key = source_key
        self.dest_key = dest_key
    
    def pzdata_etl(self):

        def extract_zip_into_memory():
            s3 = boto3.resource('s3')
            s3_object = s3.Object(self.bucket_name, self.source_key)

            print('[extract_zip_into_memory] Loading zip file from s3 into memory.')

            zip_bytes = io.BytesIO(s3_object.get()['Body'].read())

            return zipfile.ZipFile(zip_bytes)
        
        def transform_into_pzdata(zip_object):
            csvfile = 'ml-100k/u.data'

            print('[transform_into_pzdata] Running Pandas transforms.')
            udata = zip_object.open(csvfile)

            data = pandas.read_csv(udata, sep='\t', names=['USER_ID', 'ITEM_ID', 'RATING', 'TIMESTAMP'])
            data = data[data['RATING'] > 3.6]
            data = data[['USER_ID', 'ITEM_ID', 'TIMESTAMP']]

            return data.to_csv(index=False)

        def upload_pzdata(pzdata):
            s3 = boto3.resource('s3')
            s3_object = s3.Object(self.bucket_name, self.dest_key)

            print('[upload_pzdata] Loading generated data into S3.')
            s3_object.put(Body=pzdata)
            print('[upload_pzdata] Done.')

        zip_object = extract_zip_into_memory()
        pzdata = transform_into_pzdata(zip_object)
        upload_pzdata(pzdata)


