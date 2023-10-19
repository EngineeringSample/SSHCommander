# SSHCommander
SSHCommander
### Tutorial: Using SSHCommander - A Python Script for SSH Automation

SSHCommander is a Python script that allows you to easily connect to multiple remote Linux servers via SSH, execute commands, and save the command outputs to separate log files for each server. This tutorial will guide you through the steps of setting up and using SSHCommander.

#### Prerequisites

Before you get started, make sure you have the following prerequisites in place:

1. Python installed on your local machine.
2. The Paramiko library installed. You can install it using `pip install paramiko`.

#### Getting the SSHCommander Script

You can obtain the SSHCommander script from its GitHub repository. The script is available at this URL: [SSHCommander.py](https://raw.githubusercontent.com/YuanLiuchang/SSHCommander/main/SSHCommander.py). You can either download it or clone the repository.

#### Usage Instructions

1. Open a terminal or command prompt on your local machine.

2. Navigate to the directory where you've placed the SSHCommander script.

3. Run the script by using the following command:

   ```
   python SSHCommander.py
   ```

4. The script will prompt you for the following information:

   - The number of servers you want to connect to.
   - For each server:
     - IP address of the server.
     - SSH port (default is 22, but you can specify a different port).
     - SSH username.
     - SSH password.
     - Command to execute on the server.
     - Log file name to save the output.

5. The script will then connect to each server, execute the specified command, and save the output to a log file in the current directory. The log file name will include the server's IP address for easy identification.

6. You can review the log files in the current directory to see the output from each server.

#### Security Considerations

Please keep in mind that storing passwords in plaintext within scripts can be a security risk. A more secure approach is to use SSH key-based authentication. You should only use this script in a trusted and secure environment.

That's it! You now know how to use SSHCommander to automate SSH connections to multiple servers and execute commands with ease.
