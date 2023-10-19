import paramiko
import os

def ssh_connect(server, port, username, password, command, log_file):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, port=port, username=username, password=password)

        print(f"Output from {server} (Logged to {log_file}):")
        with open(log_file, 'w') as log:
            stdin, stdout, stderr = ssh.exec_command(command)
            for line in stdout.readlines():
                print(line.strip())
                log.write(line)

        ssh.close()
    except Exception as e:
        print(f"Failed to connect to {server}: {str(e)}")

def main():
    num_servers = int(input("Enter the number of servers to connect to:"))
    servers = []

    for i in range(num_servers):
        server = input(f"Enter the IP address of server {i+1}:")
        port = int(input(f"Enter the SSH port of server {i+1}:"))
        username = input(f"Enter the SSH username of server {i+1}:")
        password = input(f"Enter the SSH password of server {i+1}:")
        command = input("Enter the command to execute in bulk:")
        log_file = f"log_{server}.txt"  # Use different file names to distinguish between machines
        servers.append((server, port, username, password, command, log_file))

    for server, port, username, password, command, log_file in servers:
        ssh_connect(server, port, username, password, command, log_file)

if __name__ == "__main__":
    main()
