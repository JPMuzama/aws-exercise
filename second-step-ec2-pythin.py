import boto3
import time

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Parameters for launching the instance
instance_params = {
    'ImageId': 'ami-0abcdef1234567890',  # Replace with a valid AMI
    'InstanceType': 't2.micro',         # Instance type
    'MinCount': 1,
    'MaxCount': 1,
    'SecurityGroupIds': ['sg-0abcdef1234567890'],  # Replace with a valid Security Group ID
    'KeyName': 'your-key-pair'         # Replace with your key pair name
}

# Launch the instance
response = ec2.run_instances(**instance_params)
instance_id = response['Instances'][0]['InstanceId']

print(f"Instance {instance_id} launched successfully.")

# Wait for 5 minutes
print("Waiting for 5 minutes...")
time.sleep(300)

# Stop the instance
ec2.stop_instances(InstanceIds=[instance_id])
print(f"Instance {instance_id} stopped.")

# Optional: Terminate the instance
# ec2.terminate_instances(InstanceIds=[instance_id])
# print(f"Instance {instance_id} terminated.")