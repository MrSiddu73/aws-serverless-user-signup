import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:<region>:<account-id>:WelcomeEmailTopic"

def lambda_handler(event, context):

    # Each message in SQS is in event['Records']
    for record in event['Records']:
        message = json.loads(record['body'])

        name = message["name"]
        email = message["email"]

        welcome_msg = f"Hello {name}, welcome to our platform!"

        # Publish message to SNS
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Welcome to Our Platform!",
            Message=welcome_msg
        )

        print(f"Processed user: {name}, {email}")

    return {
        "status": "success"
    }
