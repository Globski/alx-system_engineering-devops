# System-Engineering Devops - Networking Basics #1

## Description
In this project, you'll continue to explore networking basics, focusing on topics such as localhost, IP addressing, and network interfaces. By understanding these concepts, you'll be better equipped to configure network settings and troubleshoot connectivity issues.

## Project Structure

| Task                          | Description                                          | Source Code                           |
|-------------------------------|------------------------------------------------------|---------------------------------------|
| Change your home IP           | Configure localhost and specific domain resolution. | [0-change_your_home_IP](0-change_your_home_IP) |
| Show attached IPs             | Display all active IPv4 IPs on the machine.         | [1-show_attached_IPs](1-show_attached_IPs) |
| Port listening on localhost   | Write a Bash script to listen on port 98 on localhost. | [100-port_listening_on_localhost](100-port_listening_on_localhost) |

## Environment

- All files will be interpreted on Ubuntu 20.04 LTS.

## Requirements

- All files should end with a new line.
- All Bash script files must be executable.
- Your Bash script must pass Shellcheck without any errors.
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Learning Objectives
After completing this project, you should be able to explain:

- The significance of localhost (127.0.0.1) and 0.0.0.0.
- The purpose of the /etc/hosts file.
- How to display active network interfaces on a machine.

## Additional Note

- Remember to revert any changes made to localhost IP settings after completing your testing to avoid disrupting system functionality.

## How to Use

- Clone the repository to your local machine.
- Navigate to the project directory 0x08-networking_basics_2.
- Ensure all scripts are executable using chmod +x script_name.
- Execute each script with appropriate arguments to perform the specified tasks.

## Tasks

### 0. Change Your Home IP

**Script:** `0-change_your_home_IP`

**Description:** This script modifies the `/etc/hosts` file to change the IP addresses associated with `localhost` and `facebook.com`.

**Requirements:**
- `localhost` should resolve to `127.0.0.2`.
- `facebook.com` should resolve to `8.8.8.8`.

**Usage:**
1. Run the script with sudo privileges to make changes:
   ```bash
   sudo ./0-change_your_home_IP
   ```
2. Verify the changes:
   ```bash
   ping localhost
   ping facebook.com
   ```

**Notes:** If running on a machine you'll continue to use, revert `localhost` to `127.0.0.1` after testing.

### 1. Show Attached IPs

**Script:** `1-show_attached_IPs`

**Description:** This script displays all active IPv4 IP addresses on the machine.

**Usage:**
1. Run the script:
   ```bash
   ./1-show_attached_IPs
   ```

**Example Output:**
```
10.0.2.15
127.0.0.1
```

### 2. Port Listening on Localhost

**Script:** `100-port_listening_on_localhost`

**Description:** This script listens on port 98 on `localhost` and displays any received data.

**Usage:**
1. Start the script in one terminal:
   ```bash
   sudo ./100-port_listening_on_localhost
   ```
2. Connect to the port using `telnet` in another terminal:
   ```bash
   telnet localhost 98
   ```
3. Type some text and press enter to send it:
   ```
   Hello world
   test
   ```
