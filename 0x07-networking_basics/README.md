# System-Engineering Devops - Networking Basics #0

## Description
In this project, you'll dive into the fundamentals of networking, covering topics such as the OSI model, types of networks, MAC and IP addresses, TCP/UDP protocols, and more. By understanding these concepts, you'll gain insights into how data is transmitted across networks and how devices communicate with each other.

## Project Structure

| Task                     | Description                                                 | Source Code                  |
|--------------------------|-------------------------------------------------------------|------------------------------|
| OSI model                | Understand and explain the OSI model.                       | [0-OSI_model](0-OSI_model)  |
| Types of network         | Differentiate between LAN, WAN, and the Internet.          | [1-types_of_network](1-types_of_network)  |
| MAC and IP address       | Define MAC and IP addresses.                                | [2-MAC_and_IP_address](2-MAC_and_IP_address)  |
| UDP and TCP              | Understand the differences between UDP and TCP protocols.   | [3-UDP_and_TCP](3-UDP_and_TCP)  |
| TCP and UDP ports        | Identify listening ports and their associated programs.     | [4-TCP_and_UDP_ports](4-TCP_and_UDP_ports)  |
| Is the host on the network | Create a script to ping an IP address.                    | [5-is_the_host_on_the_network](5-is_the_host_on_the_network)  |

## Environment

- All Bash script files will be interpreted on Ubuntu 20.04 LTS.

## Requirements

- All files should end with a new line.
- All Bash script files must be executable.
- Bash script must pass shellcheck without any error.
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

## Learning Objectives
After completing this project, you should be able to explain:

- The OSI model and its layers.
- Different types of networks, such as LAN, WAN, and the Internet.
- The purpose and usage of MAC and IP addresses.
- The differences between UDP and TCP protocols.
- Commonly used TCP and UDP ports.
- Using ICMP to check if a host is reachable on the network.

## How to Use
- Clone the repository to your local machine.
- Navigate to the project directory 0x07-networking_basics.
- Ensure all scripts are executable using chmod +x script_name.
- Execute each script with appropriate arguments to perform the specified tasks.

## Tasks

### 0. OSI Model

**File:** `0-OSI_model`

**Description:** This task provides a conceptual understanding of the OSI (Open Systems Interconnection) model. The OSI model is a framework used to understand and design network communication by dividing it into seven layers, from physical transmission to application-specific communication.

**Questions:**

1. **What is the OSI model?**
   - The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology.

2. **How is the OSI model organized?**
   - From the lowest to the highest level.

**Usage:**
- Review the model's layers and their functions to better understand how networking processes are structured.

### 1. Types of Network

**File:** `1-types_of_network`

**Description:** This task explores different types of networks and their use cases.

**Questions:**

1. **What type of network is a computer in a local area connected to?**
   - LAN (Local Area Network).

2. **What type of network could connect an office in one building to another office in a building a few streets away?**
   - WAN (Wide Area Network).

3. **What network do you use when you browse www.google.com from your smartphone (not connected to the Wi-Fi)?**
   - Internet.

**Usage:**
- Understand different network types and their applications for better networking solutions.

### 2. MAC and IP Address

**File:** `2-MAC_and_IP_address`

**Description:** This task covers MAC (Media Access Control) addresses and IP (Internet Protocol) addresses, explaining their roles in network communication.

**Questions:**

1. **What is a MAC address?**
   - The unique identifier of a network interface.

2. **What is an IP address?**
   - It is to devices connected to a network what a postal address is to houses.

**Usage:**
- Learn how MAC and IP addresses function as identifiers in a network.

### 3. UDP and TCP

**File:** `3-UDP_and_TCP`

**Description:** This task examines UDP (User Datagram Protocol) and TCP (Transmission Control Protocol), including their characteristics and use cases.

**Questions:**

1. **Which statement is correct for the TCP box?**
   - It is a protocol that is transferring data in a slow way but surely.

2. **Which statement is correct for the UDP box?**
   - It is a protocol that is transferring data in a fast way and might lose data along in the process.

3. **Which statement is correct for the TCP worker?**
   - Have you received boxes x, y, z?

**Usage:**
- Compare UDP and TCP to understand their differences in terms of speed and reliability.

### 4. TCP and UDP Ports

**File:** `4-TCP_and_UDP_ports`

**Description:** This task involves creating a Bash script to display listening TCP and UDP ports on a network device.

**Requirements:**
- Display only listening sockets.
- Show the PID and name of the program to which each socket belongs.

**Usage:**
1. Run the script with sudo:
   ```bash
   sudo ./4-TCP_and_UDP_ports
   ```

**Example Output:**
```
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
...

Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
...
```

### 5. Is the Host on the Network

**File:** `5-is_the_host_on_the_network`

**Description:** This script pings a specified IP address and checks network connectivity.

**Requirements:**
- Accepts an IP address as an argument.
- Displays usage instructions if no argument is provided.
- Ping the IP address 5 times.

**Usage:**
1. Run the script with an IP address:
   ```bash
   ./5-is_the_host_on_the_network 8.8.8.8
   ```
2. If no IP address is provided:
   ```bash
   ./5-is_the_host_on_the_network
   ```

**Example Output:**
```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
...
--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
```
