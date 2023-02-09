# cisco-device-configuration-extractor

This code is written in Python and it's purpose is to extract information from a Cisco router through SSH (Secure Shell) protocol using Paramiko library. The code establishes a connection to the device using the IP address of the router, username and password, then opens a shell on the device and sends commands such as enable, terminal length 0, and show run to retrieve the configuration information. The output of the commands is decoded and stored in the variable output.

The code then opens a new CSV file named cisco_data.csv and writes the header row. It then parses the output and uses regular expressions to extract specific information such as the hostname, IOS version, username, and configuration commands and settings. This information is then written to the CSV file as a new row.

Once the information has been extracted and written to the CSV file, the code closes the SSH connection.
