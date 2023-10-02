import json
import boto3

def lambda_handler(event, context):
    # Log the received event for debugging
    print(f"Received event: {json.dumps(event, indent=2)}")
    
    # Create a Lambda client
    lambda_client = boto3.client('lambda')

    # Invoke the second Lambda function asynchronously
    response = lambda_client.invoke(
        FunctionName='yourLambdaFunctionName',
        InvocationType='Event',  # Asynchronous invocation
        Payload=json.dumps(event)  # Pass the original event to the second Lambda function
    )
    
    # Create a response with status code 200 and body as JSON
    api_response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        }
    }
    
    return api_response