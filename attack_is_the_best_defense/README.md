# System-Engineering DevOps - Attack is the Best Defense

## Description

This project focuses on network security and practical applications for sniffing unencrypted traffic and performing dictionary attacks. It involves two main tasks: sniffing unencrypted traffic to find a password and performing a dictionary attack on an SSH account. It aims to enhance understanding of network security, Docker, and authentication methods.

## Project Structure


| Task | Description | Source Code |
|------|-------------|-------------|
| **0** | **Network Sniffing**: Sniff network traffic and analyze it for sensitive information using tcpdump and Wireshark. | [0-sniffing](./0-sniffing) |
| **1** | **Dictionary Attack**: Perform a dictionary attack on an SSH service running inside a Docker container using Hydra. | Docker Image: `sylvainkalache/264-1` |


**Environment Setup:**
- Ubuntu version
- Network configuration


## Learning Objectives

- Understand and apply network sniffing techniques.
- Perform ARP spoofing (conceptual understanding) and analyze unencrypted traffic.
- Use Docker to simulate network services and attacks.
- Implement dictionary attacks to test password strength.
- Develop skills using tools such as `tcpdump`, `hydra`, and Docker.


## How to Use

### Task 0. Network Sniffing

1. **Install Required Tools:**
   - Ensure you have `tcpdump` installed on your Linux machine. Install it using:
     ```bash
     sudo apt-get update
     sudo apt-get install tcpdump
     ```

2. **Download and Prepare the Script:**
   - Download the `user_authenticating_into_server` script from the GitHub repository:
     ```bash
     wget https://github.com/Globski/alx-system_engineering-devops/blob/master/attack_is_the_best_defense/user_authenticating_into_server
     ```
   - Make the script executable:
     ```bash
     chmod +x user_authenticating_into_server
     ```

3. **Setup the Environment:**
   - Run the script to initiate the authentication process:
     ```bash
     ./user_authenticating_into_server
     ```
4. **Wireshark Installation Instructions:**
   - Install Wireshark, which is necessary for analyzing `.pcap` files:
     ```bash
     sudo apt-get install wireshark
     ```
5. **Start Sniffing Traffic:**
   - Open a new terminal and start sniffing the network traffic with `tcpdump`:
     ```bash
     sudo tcpdump -i any -w capture.pcap
     ```
  - After running the script, you should see the authentication process in `tcpdump`.
  - Analyze the `capture.pcap` file using Wireshark or similar tools to extract the base64-encoded credentials.
  - Decode the base64 string to find the password.

### Task 1. Dictionary Attack
- Perform a dictionary attack on an SSH account in a Docker container to find the password.
- Use `hydra` to brute force the SSH account.
1. **Install Docker:**
   - Install Docker on your Ubuntu machine:
     ```bash
     sudo apt-get update
     sudo apt-get install docker.io
     ```

2. **Run the Docker Container:**
   - Pull and run the Docker image:
     ```bash
     sudo docker run -p 2222:22 -d -ti sylvainkalache/264-1
     ```

3. **Prepare Password Dictionary:**
   - Find or create a password dictionary file for the brute force attack. You can use common password lists online or create your own.

4. **Password Dictionary Examples:**
   - Offer links or examples of common password dictionaries to use with Hydra. For instance, you might refer to well-known lists like [SecLists](https://github.com/danielmiessler/SecLists).
5. **Install and Use Hydra:**
   - Install `hydra`:
     ```bash
     sudo apt-get install hydra
     ```
   - Run `hydra` to perform the dictionary attack:
     ```bash
     hydra -l sylvain -P <path_to_password_dictionary> ssh://127.0.0.1:2222
     ```
- Once `hydra` completes the attack, it will display the correct password.

## Tasks

#### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

**Description:**

In this task, you will sniff network traffic to extract sensitive information by using ARP spoofing and tcpdump. Although ARP spoofing itself is not covered, you will use tcpdump to intercept and analyze unencrypted traffic.

**Steps:**

1. **Setup:**
   - Ensure you are using an Ubuntu Vagrant machine or another Linux system.
   - Download the provided script `user_authenticating_into_server` from [here](https://intranet.alxswe.com/rltoken/GE_FoAUArlVccQlt7CuBGA)

2. **Execution:**
   - Run the script `user_authenticating_into_server` to simulate the authentication process.
   - Use tcpdump to capture network traffic:
     ```bash
     sudo tcpdump -i any -w capture.pcap
     ```
   - Analyze the `capture.pcap` file to extract the sensitive information. You can use tools like Wireshark for this purpose:
     ```bash
     wireshark capture.pcap
     ```
   - Look for the base64 encoded authentication credentials in the tcpdump output.

3. **Submission:**
   - Paste the extracted password in your answer file.

**Resources:**
- `tcpdump` for capturing network packets.
- `wireshark` for analyzing captured packets.
- Information on network sniffing and ARP spoofing.

**Example Usage:**
```bash
./user_authenticating_into_server
sudo tcpdump -i any -w capture.pcap
```

#### Task 1: Dictionary Attack

**Description:**

In this task, you will perform a dictionary attack to find a password for an SSH account running inside a Docker container. The dictionary attack will be executed using `hydra`.

**Steps:**

1. **Setup Docker:**
   - Install Docker on your Ubuntu machine if not already installed:
     ```bash
     sudo apt update
     sudo apt install docker.io
     ```
   - Pull and run the Docker image:
     ```bash
     docker run -p 2222:22 -d -ti sylvainkalache/264-1
     ```

2. **Prepare Password Dictionary:**
   - Obtain or create a password dictionary. You can find sample dictionaries online or create your own.

3. **Execute Dictionary Attack:**
   - Install `hydra` if it is not installed:
     ```bash
     sudo apt install hydra
     ```
   - Run `hydra` to perform the dictionary attack on the SSH service:
     ```bash
     hydra -l sylvain -P /path/to/password_dictionary.txt ssh://127.0.0.1:2222
     ```

4. **Submission:**
   - Once you find the correct password, paste it into your answer file.

**Resources:**
- `docker` for running the container.
- `hydra` for performing the dictionary attack.
- A password dictionary file.

**Example Usage:**
```bash
docker run -p 2222:22 -d -ti sylvainkalache/264-1
hydra -l sylvain -P /path/to/password_dictionary.txt ssh://127.0.0.1:2222
```

**Troubleshooting Tips:**
**What to do if `tcpdump` isn't capturing traffic.**
- If tcpdump is not capturing traffic, ensure you have proper permissions and check network interfaces.
**Issues with Docker container setup and how to resolve them.**
- For Docker issues, verify that Docker is running and the container is properly started.


