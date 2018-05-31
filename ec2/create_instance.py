#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
        ImageId = 'ami-6bc56f13',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        NetworkInterfaces=[{'SubnetId': 'subnet-3154ea7a', 'DeviceIndex': 0, 'AssociatePublicIpAddress':            False, 'Groups': ['sg-c24a82b3']}] 
       )
instance[0].wait_until_running()
print instance[0].id
