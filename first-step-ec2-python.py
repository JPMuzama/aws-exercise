import boto3
import time

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Create a key pair
key_pair_name = 'my-key-pair'
print(f"Creating key pair: {key_pair_name}...")
key_pair = ec2.create_key_pair(KeyName=key_pair_name)
with open(f"{key_pair_name}.pem", "w") as key_file:
    key_file.write(key_pair['KeyMaterial'])
print(f"Key pair created and saved to {key_pair_name}.pem.")

# Create a security group
security_group_name = 'my-security-group'
print(f"Creating security group: {security_group_name}...")
security_group = ec2.create_security_group(
    GroupName=security_group_name,
    Description='Security group for EC2 instance'
)

# Add a rule to allow all inbound traffic
ec2.authorize_security_group_ingress(
    GroupId=security_group['GroupId'],
    IpPermissions=[
        {
            'IpProtocol': '-1',  # -1 means all protocols
            'FromPort': -1,      # -1 means all ports
            'ToPort': -1,        # -1 means all ports
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]  # Allow traffic from all IP addresses
        }
    ]
)
print(f"Security group created with ID: {security_group['GroupId']}.")

# Define instance parameters
instance_params = {
    'ImageId': 'ami-0e2c8ca4b6378d8c',  # Replace with a valid AMI
    'InstanceType': 't2.micro',         # Instance type
    'MinCount': 1,
    'MaxCount': 1,
    'KeyName': key_pair_name,           # Use the created key pair
    'SecurityGroupIds': [security_group['GroupId']],  # Use the created security group
    'TagSpecifications': [              # Add tags
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyPythonInstance'  # Custom name for the instance
                }
            ]
        }
    ]
}

# Launch the instance
print("Launching EC2 instance...")
response = ec2.run_instances(**instance_params)
instance_id = response['Instances'][0]['InstanceId']
print(f"Instance {instance_id} launched successfully.")

# Wait for the instance to be running
print("Waiting for the instance to be in 'running' state...")
waiter = ec2.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])
print(f"Instance {instance_id} is now running.")

# Wait for 5 minutes
print("Waiting for 5 minutes...")
time.sleep(300)

# Stop the instance
print(f"Stopping instance {instance_id}...")
ec2.stop_instances(InstanceIds=[instance_id])

# Wait for the instance to be stopped
print("Waiting for the instance to be in 'stopped' state...")
waiter = ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[instance_id])
print(f"Instance {instance_id} is now stopped.")

# Optional: Terminate the instance
# print(f"Terminating instance {instance_id}...")
# ec2.terminate_instances(InstanceIds=[instance_id])
# print(f"Instance {instance_id} terminated.")