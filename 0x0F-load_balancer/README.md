
# System-Engineering Devops - Load Balancer

## Description
This project aims to implement a load balancer using HAProxy for redundancy and scalability in a web server environment. It involves setting up multiple web servers behind the load balancer and configuring them to serve HTTP requests with custom headers.

## Project Structure

| Task                              | Description                                                                 | Source Code                               |
|-----------------------------------|----------------------------------------------------------------------------|-------------------------------------------|
| Task 0: Double the number of webservers | Configure web-02 identical to web-01. Add custom Nginx response header `X-Served-By`. | [0-custom_http_response_header](https://github.com/yourusername/alx-system_engineering-devops/blob/main/0x0F-load_balancer/0-custom_http_response_header) |
| Task 1: Install your load balancer | Install and configure HAProxy on lb-01. Distribute traffic using round-robin algorithm. | [1-install_load_balancer](https://github.com/yourusername/alx-system_engineering-devops/blob/main/0x0F-load_balancer/1-install_load_balancer) |
| Task 2: Add a custom HTTP header with Puppet | Use Puppet to automate `X-Served-By` header creation in Nginx responses. (Advanced) | [2-puppet_custom_http_response_header.pp](https://github.com/yourusername/alx-system_engineering-devops/blob/main/0x0F-load_balancer/2-puppet_custom_http_response_header.pp) |

### Learning Objectives
- Implement load balancing for redundancy and scalability.
- Automate server configurations using Bash and Puppet.
- Manage HTTP headers to track server responses.

### Environment
- Ubuntu 16.04 LTS on all servers (web-01, web-02, lb-01).
- HAProxy installed on lb-01.

### Requirements
- Scripts must be executable (`#!/usr/bin/env bash`).
- Follow Shellcheck guidelines for script validation.

### How to Use

   - Ubuntu 16.04 LTS installed on all servers (web-01, web-02, lb-01).
   - HAProxy installed on lb-01 server.

   - Clone the repository: `git clone https://github.com/yourusername/alx-system_engineering-devops`
   - Navigate to the project directory: `cd 0x0F-load_balancer`

## Tasks

1. **Task 0: Double the number of webservers**
   - Configure web-02 identical to web-01.
   - Add a custom Nginx response header `X-Served-By` with the hostname of the server.
   - Script: `0-custom_http_response_header`

2. **Task 1: Install your load balancer**
   - Install and configure HAProxy on lb-01.
   - Distribute traffic using round-robin algorithm to web-01 and web-02.
   - Ensure HAProxy can be managed via an init script.
   - Script: `1-install_load_balancer`

3. **Task 2: Add a custom HTTP header with Puppet (Advanced)**
   - Use Puppet to automate the creation of `X-Served-By` header in Nginx responses.
   - Script: `2-puppet_custom_http_response_header.pp`
