import boto3
import os

dynamoclient = boto3.client('dynamodb', region_name='eu-central-1',
    aws_access_key_id='KEY_ID',
    aws_secret_access_key='SECRET_KEY')

dynamotargetclient = boto3.client('dynamodb', region_name='eu-central-1',
    aws_access_key_id='KEY_ID',
    aws_secret_access_key='SECRET_KEY')

dynamopaginator = dynamoclient.get_paginator('scan')
tabname='TableName'
targettabname='TableName'
dynamoresponse = dynamopaginator.paginate(
    TableName=tabname,
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='NONE',
    ConsistentRead=True
)
for page in dynamoresponse:
    for item in page['Items']:
        dynamotargetclient.put_item(
            TableName=targettabname,
            Item=item
        )
