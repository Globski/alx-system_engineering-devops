# System-Engineering Devops - Firewall

## Description
This project focuses on setting up and configuring firewall rules on a Linux server using UFW (Uncomplicated Firewall) to enhance security. The primary objectives are to secure the server by blocking all incoming traffic except for specific essential services and to implement port forwarding. By setting up and managing firewall rules, you will ensure secure and controlled access to your server.

## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0. Block all incoming traffic but | Configure ufw to block all incoming traffic except for TCP ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) on web-01. | `0-block_all_incoming_traffic_but` |
| 1. Port forwarding | Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP. Include the modified ufw configuration file. | `100-port_forwarding` |

### Firewall

A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It establishes a barrier between a trusted internal network and untrusted external networks (like the internet).

## Learning Objectives

- Understand the purpose and functionality of a firewall.
- Learn how to install and configure UFW on a Linux server.
- Apply firewall rules to allow specific incoming traffic.
- Configure port forwarding using UFW.


