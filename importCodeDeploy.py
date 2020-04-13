from __future__ import print_function
import json
import boto3
import time

print('Loading function')

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    x=0

    
    codedeployClient = boto3.client('codedeploy')
    snsClient = boto3.client('sns')

    while (x<5):
        deploymentResponse = codedeployClient.get_deployment(
            deploymentId= message['deploymentId']
        )

        res = json.loads(depoymentResponse)

        if res['deploymentInfo']['status'] == 'Succeeded':
            print("Success")
            snsPublish = snsClient.publish(
                topicArn = 'arn:aws:sns:us-east-1:1234567890:SuccessfulDeployment',
                message = 'Example'
            )
            return true
        else:
            time.sleep(10)
            x+=1
    print("Deployment Timeout, check: " + message['deploymentId'])
    return false 

