
import boto3
import json

personalize = boto3.client(service_name='personalize', endpoint_url='https://personalize.us-east-1.amazonaws.com', region_name='us-east-1')
personalize_runtime = boto3.client(service_name='personalize-runtime', endpoint_url='https://personalize-runtime.us-east-1.amazonaws.com', region_name='us-east-1')

schema = {
    "type": "record",
    "name": "Interactions",
    "namespace": "com.amazonaws.personalize.schema",
    "fields": [
        {
            "name": "USER_ID",
            "type": "string"
        },
        {
            "name": "ITEM_ID",
            "type": "string"
        },
        {
            "name": "TIMESTAMP",
            "type": "long"
        }
    ],
    "version": "1.0"
}

class PzBuilder:

    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.schema = schema
    
    def destroy_build(self):
        pass

    def create_schema(self, schema):
        schema_name = self.name + '-schema'

        create_schema_response = personalize.create_schema(
            name=schema_name,
            schema=json.dumps(schema)
        )

        print(json.dumps(create_schema_response, indent=2))

        return create_schema_response['schemaArn']



# TODO: Create a dataset group

# TODO: Create a dataset

# TODO: Prepare, Create, and Wait for Dataset Import Job

# TODO: Select a recipe

# TODO: Create a solution

# TODO: Create a campaign

# TODO: Get recommendations


pzBuilder = PzBuilder('test', 'data')
print(pzBuilder.schema)