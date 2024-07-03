# System-Engineering Devops - Web server

## Description
This project involves setting up and configuring a web server using various tasks, including file transfer, installing Nginx, configuring domain names, redirection, custom error pages, and automating server configuration with Puppet. The objective is to understand the role of web servers, DNS, HTTP requests, and automation tools in a real-world scenario.


## Project Structure

| Task | Description | Source Code |
|------|-------------|-------------|
| 0 | Transfer a file to your server | [0-transfer_file](0-transfer_file) |
| 1 | Install Nginx web server | [1-install_nginx_web_server](1-install_nginx_web_server) |
| 2 | Setup a domain name | [2-setup_a_domain_name](2-setup_a_domain_name) |
| 3 | Redirection | [3-redirection](3-redirection) |
| 4 | Not found page 404 | [4-not_found_page_404](4-not_found_page_404) |
| 5 | Install Nginx web server (w/ Puppet) | [7-puppet_install_nginx_web_server.pp](7-puppet_install_nginx_web_server.pp) |

#### Learning Objectives

- Understand the role of web servers and how to configure them.
- Learn about DNS and different record types.
- Use Puppet to automate server configuration.
- Implement HTTP redirection and custom error pages.

#### Environment

- Ubuntu 16.04 LTS
- Puppet 4.10 or higher
- Nginx 1.10 or higher

#### Requirements

- Scripts must pass Shellcheck (version 0.3.7) without any errors.
- All scripts must be executable.
- All files must end with a new line.

#### How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Follow the instructions for each task to configure your server as required.
4. **Ensure Your Bash Script is Executable:**
   ```bash
   chmod +x 88-script_example
   ```
### Tasks
#### Task 0: Transfer a File to Your Server

**Description:**
Write a Bash script that transfers a file from a client to a server using `scp`.

**Requirements:**
- Accepts 4 parameters: path to the file, server IP, username for `scp` connection, path to SSH private key.
- Displays usage instructions if less than 4 parameters are provided.
- Transfers the file to the user's home directory (`~/`) on the server.
- Disables strict host key checking for `scp`.

**Example Usage:**
```bash
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

#### Task 1: Install Nginx Web Server

**Description:**
Install Nginx on an Ubuntu server (`web-01`), configure it to listen on port 80, and verify functionality.

**Requirements:**
- Use `-y` on the `apt-get` command for non-interactive installation.
- Ensure Nginx serves a page with the string "Hello World!" when queried at `/`.
- Script should be able to run on the server itself.

**Example Usage:**
```bash
./1-install_nginx_web_server > /dev/null 2>&1
curl localhost   # Should return "Hello World!"
```

#### Task 2: Setup a Domain Name

**Description:**
Register and configure a `.tech` domain to point to your `web-01` server's IP address.

**Requirements:**
- Provide the domain name (e.g., `example.tech`).
- Configure DNS records with an A entry for the root domain to point to `web-01`'s IP.
- Verify domain propagation.

**Example:**
```text
myschool.tech
```
Ensure the domain is registered with the registrar "Dotserve Inc".

#### Task 3: Redirection

**Description:**
Configure Nginx so that `/redirect_me` redirects to another page with a "301 Moved Permanently" status.

**Requirements:**
- Use `sed` to replace a line with multiple lines in the Nginx configuration.
- Implement a 301 redirection from `/redirect_me` to another URL.

**Example:**
```bash
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```

#### Task 4: Not Found Page 404

**Description:**
Configure Nginx to display a custom 404 page with the text "Ceci n'est pas une page".

**Requirements:**
- Ensure Nginx returns a 404 error code and displays the specified text.
- Implement using configuration commands similar to Task 3.

**Example:**
```bash
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

#### Task 5: Install Nginx Web Server (w/ Puppet)

**Description:**
Install and configure Nginx on an Ubuntu server using Puppet, ensuring it listens on port 80 and redirects `/redirect_me` with a 301 status.

**Requirements:**
- Write a Puppet manifest (`7-puppet_install_nginx_web_server.pp`) to automate installation and configuration.
- Verify Nginx serves the "Hello World!" page at `/` and implements the redirection.

**Example:**
```puppet
include nginx
```

## Terms 
**Child Process:**
   - A child process is a process created by another process (the parent process). Child processes inherit most of their attributes from their parent but execute independently.

   - A child process is created by a parent process using system calls like `fork()`. It is used to perform tasks concurrently with the parent process. Web servers use child processes to handle multiple client requests simultaneously.


**Main Role of a Web Server:**
   - The primary role of a web server is to serve web pages to clients. This includes serving static content like HTML, CSS, and JavaScript files, and dynamic content generated by server-side scripts or applications.

**Parent and Child Processes in Web Servers:**
   - Web servers have a parent process to manage child processes. The parent process spawns child processes to handle incoming requests, allowing for concurrent processing and better performance.

**Main HTTP Requests:**
   - The main HTTP requests are GET, POST, PUT, DELETE, PATCH, and HEAD. GET requests data from a resource, POST submits data to be processed, PUT updates a resource, DELETE removes a resource, PATCH applies partial modifications, and HEAD retrieves headers.

**DNS (Domain Name System):**
   - DNS stands for Domain Name System. Its main role is to translate human-readable domain names into IP addresses that computers use to identify each other on the network.

**DNS Record Types:**
   - **A (Address) Record:** Maps a domain to an IPv4 address.
   - **CNAME (Canonical Name) Record:** Maps an alias domain name to a canonical domain name.
   - **TXT (Text) Record:** Allows domain administrators to insert arbitrary text into a DNS record.
   - **MX (Mail Exchange) Record:** Specifies the mail server responsible for receiving email on behalf of a domain.


