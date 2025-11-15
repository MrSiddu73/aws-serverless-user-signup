import json
import boto3

sqs = boto3.client('sqs')
QUEUE_URL = "https://sqs.<region>.amazonaws.com/<account-id>/UserSignupQueue"

def lambda_handler(event, context):

    # Parse body from API Gateway
    body = json.loads(event['body'])

    # Basic validation
    if 'email' not in body or 'name' not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "name and email are required"})
        }

    message = {
        "name": body["name"],
        "email": body["email"]
    }

    # Push message to SQS
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Signup received and queued"})
    }
