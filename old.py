import json
import boto3
import paramiko

def lambda_handler(event, context):
    # boto3 client
    client = boto3.client("ec2")
    s3_client = boto3.client("s3")

    # getting instance information
    describeInstance = client.describe_instances()
    
    # Initialize all required variables
    drWorkStationPublicIP = ""
    drAppPrivateIP = ""
    drAppPublicIP = ""
    drDBPrivateIP = ""
    drWorkStationName = "Dr-Chef-Workstation"
    drAppServerName = "PetClinic-App" 
    drDBServerName = "PetClinic-DB"
    drWebServerName = "PetClinic-Web"
    
    # Get pubic or private IPs for the required machines
    for i in describeInstance["Reservations"]:
        for instance in i["Instances"]:
            if instance["State"]["Name"] == "running" and "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name" and tag["Value"] == drWorkStationName:
                        drWorkStationPublicIP = instance["PublicIpAddress"]
                        continue
            if instance["State"]["Name"] == "running" and "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name" and tag["Value"] == drAppServerName:
                        drAppPrivateIP = instance["PrivateIpAddress"]
                        continue
            if instance["State"]["Name"] == "running" and "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name" and tag["Value"] == drDBServerName:
                        drDBPrivateIP = instance["PrivateIpAddress"]
                        continue
            if instance["State"]["Name"] == "running" and "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Name" and tag["Value"] == drWebServerName:
                        drWebPrivateIP = instance["PrivateIpAddress"]
                        continue
    print("DR Workstation public IP: " + drWorkStationPublicIP)
    print("DR PetClinic-DB private IP: " + drDBPrivateIP)
    print("DR PetClinic-App private IP: " + drAppPrivateIP)
    print("DR PetClinic-Web private IP: " + drWebPrivateIP)