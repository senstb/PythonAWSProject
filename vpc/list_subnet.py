#!/usr/bin/env python

import boto3 

ec2 = boto3.resource("ec2")

for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
        print(vpc, subnet)
