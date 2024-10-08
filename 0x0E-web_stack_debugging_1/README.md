# System-Engineering Devops - Web stack debugging #1

## Description

This project focuses on diagnosing and fixing issues in a simple web stack environment, specifically related to ensuring that the Nginx web server is properly configured and running on port 80. The primary goal is to apply debugging skills to resolve common network and server issues that may prevent Nginx from functioning correctly.

## Project Structure

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
   
4. **Verify Nginx Status:**
   - After running the scripts, you can check Nginx's status using:
   ```bash
   service nginx status
   ```
   - To confirm that Nginx is listening on port 80, run:
   ```bash
   curl 0:80
   ```

### Debugging Section

- **Issue Diagnosis:**
  - If Nginx fails to start or listen on port 80, common issues might include:
    - Incorrect configuration in `/etc/nginx/sites-available/default`.
    - Missing or incorrect symlink between `/etc/nginx/sites-available/default` and `/etc/nginx/sites-enabled/default`.
    - Another service might be occupying port 80.

- **Troubleshooting Steps:**
  1. **Check Nginx Configuration:**
     - Inspect `/etc/nginx/sites-available/default` for the correct `listen` directive.
     - Ensure the file is properly linked in `/etc/nginx/sites-enabled/`.
  2. **Restart Nginx:**
     - Use `service nginx restart` to apply changes and restart the service.
  3. **Check Port 80 Usage:**
     - Run `sudo lsof -i :80` to see if another process is using port 80.

---

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
