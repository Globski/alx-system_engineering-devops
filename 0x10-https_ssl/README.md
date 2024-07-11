ystem-Engineering Devops - 

## Description
The project focuses on web server management and security using Ubuntu, HAproxy and SSL/TLS encryption. Tasks include configuring DNS for domain zones, setting up HAproxy for SSL termination and HTTP to HTTPS redirection, and ensuring secure traffic management across web servers. The project aims to enhance understanding of HTTPS/SSL roles, encryption benefits, and practical skills in system administration and web security practices.

| Task | Description | Source Code |
|------|-------------|-------------|
| Task 0: World Wide Web | Configure domain zone and create a Bash script to display subdomain information. | [0-world_wide_web](0-world_wide_web) |
| Task 1: HAproxy SSL Termination | Setup HAproxy to terminate SSL for `www` subdomain and serve encrypted traffic. | [1-haproxy_ssl_termination](1-haproxy_ssl_termination) |
| Task 2: No Loophole in Your Website Traffic | Configure HAproxy to redirect HTTP traffic to HTTPS. | [100-redirect_http_to_https](100-redirect_http_to_https) |

## Learning Objectives:
By the end of the project, you should be able to explain:
- The main roles of HTTPS and SSL.
- The purpose of encrypting traffic using SSL/TLS.
- What SSL termination involves in the context of web servers.

## Environment:
- Ubuntu 16.04 LTS
- HAproxy 1.5 or higher
- `certbot` for SSL certificate generation

## Requirements:
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash

## How to Use

### Task 0: World Wide Web

1. **Configure Domain Zone**:
   - Update your domain's DNS settings to point the following subdomains to their respective IP addresses:
     - `www` to your load-balancer IP (`lb-01`)
     - `lb-01` to your load-balancer IP (`lb-01`)
     - `web-01` to your `web-01` IP address
     - `web-02` to your `web-02` IP address

2. **Bash Script (`0-world_wide_web`)**:
   - Navigate to the directory containing `0-world_wide_web`.
   - Run the script using `./0-world_wide_web domain_name [subdomain]`.
   - Replace `domain_name` with your actual domain and optionally provide `subdomain` to get specific information.
   - Example usage:
     ```bash
     ./0-world_wide_web holberton.online
     ./0-world_wide_web holberton.online web-02
     ```

### Task 1: HAproxy SSL Termination

1. **Generate SSL Certificate**:
   - Use `certbot` to generate an SSL certificate for the `www` subdomain.

2. **HAproxy Configuration (`1-haproxy_ssl_termination`)**:
   - Update HAproxy configuration (`/etc/haproxy/haproxy.cfg`) with the settings provided in `1-haproxy_ssl_termination`.
   - Ensure HAproxy is listening on TCP port 443 and configured to terminate SSL for the `www` subdomain.
   - Restart HAproxy after updating the configuration.

### Task 2: No Loophole in Your Website Traffic

1. **Update HAproxy Configuration (`100-redirect_http_to_https`)**:
   - Replace the existing HAproxy configuration (`/etc/haproxy/haproxy.cfg`) with the settings provided in `100-redirect_http_to_https`.
   - Ensure HAproxy redirects all HTTP traffic to HTTPS transparently with a `301 Moved Permanently` response.
   - Restart HAproxy to apply the new configuration.

# Tasks

## Task 0: World Wide Web

### Requirements:
- Configure your domain zone so that:
  - `www` points to your load-balancer IP (`lb-01`)
  - `lb-01` points to your load-balancer IP (`lb-01`)
  - `web-01` points to your web-01 IP
  - `web-02` points to your web-02 IP

### Bash Script (`0-world_wide_web`):
- Accepts 2 arguments:
  - `domain`: Domain name to audit
  - `subdomain` (optional): Specific subdomain to audit
- Outputs information about subdomains in the format:
  ```
  The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
  ```
- When only `domain` is provided, display information for `www`, `lb-01`, `web-01`, and `web-02` subdomains in that order.

Example:
```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

## Task 1: HAproxy SSL Termination

### Requirements:
- Create an SSL certificate using `certbot` for the `www` subdomain.
- Configure HAproxy to:
  - Listen on TCP port 443
  - Accept SSL traffic
  - Serve encrypted traffic for `www` that returns the root of your web server with "Holberton School"
  
### Configuration File:
- Save HAproxy configuration as `1-haproxy_ssl_termination` in `/etc/haproxy/haproxy.cfg`

Example:
```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```

## Task 2: No Loophole in Your Website Traffic

### Requirements:
- Configure HAproxy to automatically redirect HTTP traffic to HTTPS.
- Ensure:
  - Transparent redirection
  - HTTP requests are redirected to HTTPS with a `301 Moved Permanently` response
  
### Configuration File:
- Save updated HAproxy configuration as `100-redirect_http_to_https` in `/etc/haproxy/haproxy.cfg`
Certainly! Here's how you can structure the tasks, including additional notes, project structure, environment setup, requirements, learning objectives, and additional information:

Example:

```
sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
```
