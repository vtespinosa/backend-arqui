import boto3
import json
from django.conf import settings

class LambdaConnect:
    def __init__(self, region='us-east-1', **kwargs):
        self.__client = boto3.client(
            'lambda', 
            region_name=region,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
    def lambda_invoker(self, **kwargs):
        return self.__client.invoke(
            FunctionName=kwargs.get('function_name'),
            InvocationType=kwargs.get('invokation_type', 'Event'),
            Payload=json.dumps(kwargs.get('payload', {})),
        )