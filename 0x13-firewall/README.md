# System-Engineering Devops - Firewall
![image](https://github.com/user-attachments/assets/baa72ff9-108f-4300-95ab-043389eefdcc)

## Description
This project focuses on setting up and configuring firewall rules on a Linux server using UFW (Uncomplicated Firewall) to enhance security. The primary objectives are to secure the server by blocking all incoming traffic except for specific essential services and to implement port forwarding. By setting up and managing firewall rules, you will ensure secure and controlled access to your server.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Block all incoming traffic but | Configure ufw to block all incoming traffic except for TCP ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) on web-01. | [0-block_all_incoming_traffic_but](./0-block_all_incoming_traffic_but) |
| 1. Port forwarding | Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP. Include the modified ufw configuration file. | [100-port_forwarding](./100-port_forwarding) |

### Firewall

A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It establishes a barrier between a trusted internal network and untrusted external networks (like the internet).

## Learning Objectives

- Understand the purpose and functionality of a firewall.
- Learn how to install and configure UFW on a Linux server.
- Apply firewall rules to allow specific incoming traffic.
- Configure port forwarding using UFW.


## How to Use

**Install UFW (Uncomplicated Firewall)**
**Set up basic UFW rules**
**Verify the firewall configuration**

#### Steps:
1. **SSH into web-01:**

    ```bash
    ssh ubuntu@34.203.29.246
    ```

2. **Install UFW if it's not already installed:**

    ```bash
    sudo apt-get update
    sudo apt-get install ufw -y
    ```

3. **Reset UFW to default settings:**

    ```bash
    sudo ufw reset
    ```

4. **Allow necessary ports:**

    ```bash
    sudo ufw allow 22/tcp
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    ```
   You can also set up additional rules as needed:

   **Allow specific ports:**

   ```bash
   sudo ufw allow 8080/tcp
   ```

   **Deny specific ports:**

   ```bash
   sudo ufw deny 23/tcp
   ```
5. **Enable UFW and block all other incoming traffic:**

    ```bash
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw enable
    ```

6. **Verify the UFW status and rules:**

    ```bash
    sudo ufw status verbose
    ```

**Test open ports using telnet:**

From web-02, check if port 22 is open on web-01:

```bash
telnet web-01 22
```

You should see something like:

```
Trying 34.203.29.246...
Connected to 34.203.29.246.
Escape character is '^]'.
SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
```

Check a port that you know is closed:

```bash
telnet web-01 2222
```

You should see:

```
Trying 34.203.29.246...
^C
```

#### Add a rule to forward traffic from port 8080 to 80

**Edit the UFW configuration file to include port forwarding:**

    Open the UFW configuration file:

    ```bash
    sudo nano /etc/ufw/before.rules
    ```

    Add the following lines before the `*filter` line:

    ```bash
    *nat
    :PREROUTING ACCEPT [0:0]
    -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
    COMMIT
    ```

   **Restart UFW to apply the changes:**

    ```bash
    sudo service ufw restart
    ```

   **Verify the port forwarding setup:**

   ```bash
   curl -sI http://34.203.29.246:8080
   ```

### Important Considerations

- **Avoid locking yourself out:** When you install UFW, port 22 is blocked by default so you should unblock it immediately before logging out of your server. If you ever deny port 22/TCP and log out of your server you will not be able to reconnect to your server via SSH
- **Test from different origins:** If your school network has outgoing connection filters, SSH into web-02 to perform tests on web-01 to bypass the network firewall.
- **Use caution with rules:** Misconfiguring the firewall could block necessary traffic or lock you out of the server.

## Tasks

### Task 0: Block all incoming traffic but

#### Requirements:
- Block all incoming traffic except for TCP ports 22 (SSH), 80 (HTTP), and 443 (HTTPS).
- Apply these rules to `web-01`.

**File:** `0-block_all_incoming_traffic_but`

### Task 1: Port forwarding

#### Requirements:
- Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP.

**Verification:**

Use `netstat` and `curl` commands to verify the port forwarding:

```bash
# On web-01:
root@03-web-01:~# netstat -lpn

# On web-02:
ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80
ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
```

**Expected output:**

```bash
# netstat output showing nginx listening on port 80 and SSH on port 22

# curl output showing HTTP 200 response on both port 80 and port 8080
```

**File:** `100-port_forwarding`
