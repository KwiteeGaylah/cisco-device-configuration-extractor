import paramiko
import getpass
import time
import csv
import re

#ask user for input
HOST = input("Enter the IP Address of Router:")
username = input("Enter your username:")

# Use these variables and comment the above corresponding variables if you don't want to to be ask for input.
#HOST = 'Device-IP'
#username = 'Device-Password'

#store users input in the password variable
#password = getpass.getpass()
password = 'namal'

#establish connection with the device
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=username, password=password)

#if connection is successful, print a succes message
print("Successfully Connected\n")

#establish a shell on the device
remote_connection = ssh_client.invoke_shell()

#send commands to the remote device
remote_connection.send("enable\n")
remote_connection.send("namal\n")
remote_connection.send("terminal length 0\n")
remote_connection.send("show run\n")

#display the output of all commands send/
output = remote_connection.recv(18999).decode('ascii')

#making sure that all the command output are returned
while "end" not in output:
    time.sleep(0.5)
    output += remote_connection.recv(18999).decode('ascii')
    #print(output)


# Open a new CSV file to store the data
with open('cisco_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(["Device_name", "device_username", "IOS_version", "Configuration_commands", "Configuration_settings", "Timestamp", "Device_type", "Device_model", "Device_location"])

#   Iterate over the configuration data and extract the necessary information
    for line in output.split("\n"):
        if "hostname" in line:
            device_name = line.split(" ")[1]
        if "version" in line:
            ios_version = line.split(" ")[1]
        if "username" in line:
            device_username = line.split(" ")[1]
        if re.search("^interface|line",line):
            config_command = line
            config_setting = output.split("\n")[output.split("\n").index(line) + 1]
            timestamp = "2022-09-01 14:00:00"
            device_type = "Switch"
            device_model = "Cisco2921"
            device_location = "India"
            # Write the extracted information to the CSV file
            csvwriter.writerow([device_name, device_username, ios_version, config_command, config_setting, timestamp, device_type, device_model, device_location])



#time.sleep(1)
# output = remote_connection.recv(18999).decode('ascii')

ssh_client.close
