#!/usr/bin/env python

import boto3
ec2 = boto3.resources('ec2')
for instances in ec2.instances.all():
    print instance.id, instance.state

