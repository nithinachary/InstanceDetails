import boto3
from botocore.config import Config
import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
        
    logger.info('Started fetching Ec2 instances details per region')
    
    regions = []
    client = boto3.client("ec2")
    try:
        response = client.describe_regions()
        for item in response["Regions"]:
            regions.append(item["RegionName"])
    
        # List all EC2 in each region
        instanceInfo={}
        for region in regions:
            # Change regions with config
            my_config = Config(region_name=region)
            client = boto3.client("ec2", config=my_config)
            response = client.describe_instances(Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["*"],
            }
            ]).get("Reservations")
            
            instance_ids = []
            
            # When 0 Instances found in a region
            if len(response) == 0:
                instance_ids.append('Found None')
                instanceInfo[region] = {
                    'Instances' : instance_ids
                }
            else:
                for instance_detail in response:
                    group_instances = instance_detail['Instances']
            
                    for instance in group_instances:
                        instance_id = instance['InstanceId']
                        instance_ids.append(instance_id)
                        
                    instanceInfo[region] = {
                        'InstanceIds' : instance_ids
                    }     
        
        res = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(instanceInfo,indent=4)
        }
        return res
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }