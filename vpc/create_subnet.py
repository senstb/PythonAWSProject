#!/usr/bin/env python

import boto3 

ec2 = boto3.resource("ec2")

for vpc in ec2.vpcs.all():
    subnet = ec2.create_subnet(VpcId = vpc.id, CidrBlock = "10.0.0.0/16", AvailabilityZone='us-west-2b')
    print(subnet.id)
