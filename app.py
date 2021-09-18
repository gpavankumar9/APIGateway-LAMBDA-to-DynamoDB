import json
import boto3
import os

# import requests


def lambda_handler(event, context):
    print(event)
    if os.getenv("AWS_SAM_LOCAL"):
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb:8000")
    else:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ContactRequests')
    id = event['queryStringParameters']['id']
    name = event['queryStringParameters']['name']
    print(id)
    print(name)
    if event['httpMethod'] == "POST":
      
        response = table.put_item(
            Item={
                'id': id,
                'name': name,
                'email': "testEmail@gmail.com"
                }
            )
        print("DynamoDB loaded with data")
        print("response: " + str(response))
    else:
        response = table.get_item(
            Key={
                'id': id,
                'name': name
            }
        )
        item = response['Item']
        print(item)

    
    """Sample pure Lambda function
    
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world test-lambda",
            # "location": ip.text.replace("\n", "")
        }),
    }
