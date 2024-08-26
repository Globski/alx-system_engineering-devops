# System-Engineering Devops - Web stack debugging #1

## Description

This project involves web stack debugging, where you will be diagnosing and fixing issues in a simple web stack. The main focus will be on understanding network basics and applying debugging skills to resolve common issues that may arise in a web stack environment.

## Tasks Table

| Task | Description | Source Code |
|------|-------------|-------------|
| Task 0: Nginx likes port 80 | Using debugging skills to fix Nginx not listening on port 80. Write a Bash script to automate the fix. | [0-nginx_likes_port_80](./0-nginx_likes_port_80) |
| Task 1: Make it sweet and short | Simplify the fix from Task 0 into a Bash script that is 5 lines or less. Ensure Nginx is installed, running on port 80, and the service status reflects this. | [1-debugging_made_short](./1-debugging_made_short) |

## Requirements
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- All Bash script files must be executable
- Bash scripts must pass `Shellcheck` without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- `wget` is not allowed

## How to Use

1. Ensure you are on an Ubuntu 20.04 LTS environment.
2. Make the scripts executable using the command:
   ```bash
   chmod +x script_name.sh
   ```
3. Run the scripts with:
   ```bash
   ./script_name.sh
   ```

## Tasks

### Task 0: Nginx likes port 80 (mandatory)
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Write a Bash script with the minimum number of commands to automate your fix.

Requirements:
- Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs

```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 > /dev/null 2&>1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
```

### Task 1: Make it sweet and short (#advanced)
Using what you did for task #0, make your fix short and sweet.

Requirements:

- Your Bash script must be 5 lines long or less
- There must be a new line at the end of the file
- You must respect usual Bash script requirements
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)
- service (init) must say that nginx is not running ← for real

```
root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# cat -e 1-debugging_made_short | wc -l
5
root@966c5664b21f:/# ./1-debugging_made_short
root@966c5664b21f:/# curl 0:80
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
root@966c5664b21f:/#
root@966c5664b21f:/# service nginx status
 * nginx is not running
root@966c5664b21f:/#
```
