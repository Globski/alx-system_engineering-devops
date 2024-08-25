# System Engineering Devops - Web stack debugging #4

## Description
This project focuses on debugging a web stack, specifically improving the performance of an Nginx web server under load and adjusting OS configurations for user limits. The tasks involve identifying and fixing errors in a given configuration using Puppet manifests.

## Project Structure
| Task                               | Description                                                                 | Source Code                                |
|------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| 0. Sky is the limit, let's bring that limit higher | Debug the Nginx web server to handle 2000 requests with 100 concurrent connections using ApacheBench. | [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp)           |
| 1. User limit                      | Modify the OS configuration to allow the `holberton` user to log in and open files without encountering "Too many open files" error. | [1-user_limit.pp](./1-user_limit.pp)                          |

## Features
- Fix Nginx server performance issues under load.
- Modify OS configuration for user limits.

## Learning Objectives

- Understanding web stack debugging.
- Using ApacheBench for performance testing.
- Applying Puppet for automating system configurations.
- Modifying OS-level configurations to handle system limits.

## Environment

- **Operating System:** Ubuntu 20.04 LTS
- **Web Server:** Nginx 1.4.6
- **Tools:** ApacheBench 2.3, Puppet v3.4

## Requirements
- All files end with a new line.
- Puppet manifests are checked with **Puppet v3.4**.
- Puppet manifests must:
  - Pass `puppet-lint` version 2.1.1 without any errors.
  - Run without error.
  - End with the `.pp` file extension.
- **Nginx:** The server should be running and properly configured for benchmarking.
- **ApacheBench:** Install ApacheBench for performance testing.

### How to Use
### Installation

1. **Install Puppet:**
   ```bash
   apt-get install -y puppet
   ```

2. **Install Puppet-lint:**
   ```bash
   apt-get install -y ruby
   gem install puppet-lint -v 2.1.1
   ```
   To check a Puppet manifest for lint errors:

  ```bash
  $ puppet-lint [filename].pp
  ```

### Applying Manifests

1. **Fix Nginx configuration:**
   ```bash
   sudo puppet apply 0-the_sky_is_the_limit_not.pp
   ```

2. **Change OS file limits:**
   ```bash
   puppet apply 1-user_limit.pp
   ```

### Testing

- **Benchmark Nginx:**
  Use ApacheBench to send 2000 requests with 100 concurrent connections to test the server's performance.
  ```bash
  ab -c 100 -n 2000 localhost/
  ```

- **Check file limits for user:**
  Log in as `holberton` and check for any errors when opening files.
  ```bash
  su - holberton
  head /etc/passwd
  ```

## Tasks

### 0. Sky is the limit, let's bring that limit higher
- **Objective:** Debug the Nginx web server to handle 2000 requests with 100 concurrent connections using ApacheBench.
- **Details:** We observed that the server is not performing well under pressure with 943 failed requests. The task involves using Puppet to fix the server's configuration to achieve 0 failed requests.
- **Commands:**
  ```bash
  ab -c 100 -n 2000 localhost/
  puppet apply 0-the_sky_is_the_limit_not.pp
  ```
- **Directory:** `0x1B-web_stack_debugging_4`
- **0-the_sky_is_the_limit_not.pp:** Puppet script to fix Nginx server under load.

### 1. User limit
- **Objective:** Modify the OS configuration to allow the `holberton` user to log in and open files without encountering the "Too many open files" error.
- **Details:** The task involves using Puppet to adjust the system limits so the user can operate without restrictions.
- **Commands:**
  ```bash
  su - holberton
  puppet apply 1-user_limit.pp
  ```
- **Directory:** `0x1B-web_stack_debugging_4`
- **1-user_limit.pp:** Puppet script to modify OS configuration for user limits.



# System Engineering Devops - Web stack debugging #3

## Project Description
This project involves debugging an Apache server that is returning a 500 Internal Server Error. Using `strace`, you will diagnose the issue, apply a fix manually, and then automate the fix using Puppet.

## Objective
- Debug a Wordpress website running on a LAMP stack (Linux, Apache, MySQL, PHP).

## Project Structure

| Task                               | Description                                                        | Source Code                                |
|------------------------------------|--------------------------------------------------------------------|--------------------------------------------|
| **0. Strace is Your Friend**       | Use `strace` to find why Apache returns a 500 error. Fix the issue and automate it using Puppet. | [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp) |

## Learning Objectives

- Use `strace` to diagnose issues with web servers.
- Fix and automate server issues using Puppet.
- Understand and manage Apache server errors.

## Environment

- **OS:** Ubuntu 14.04 LTS
- **Tools:**
  - `strace` for tracing system calls
  - `curl` for simulating HTTP requests
  - Puppet for automation

## Requirements
- **Files:** Should end with a new line
- **Puppet Manifests:**
  - Must pass `puppet-lint` version 2.1.1 without errors
  - Must run without errors
  - The first line must be a comment explaining the manifest
  - Must end with the `.pp` extension
  - Files will be checked with Puppet v3.4


## How to Use

### 1. Install Puppet-lint

**Step 1: Install Ruby**

Ensure Ruby is installed, as `puppet-lint` requires it.

```bash
sudo apt-get install -y ruby
```

**Step 2: Install Puppet-lint**

Install `puppet-lint`, a tool to check your Puppet manifests for style guide compliance.

```bash
gem install puppet-lint -v 2.1.1
```

### 2. Diagnose and Fix Apache 500 Internal Server Error

**Step 1: Use `strace` to Trace the Apache Process**

1. **Identify Apache's Process IDs (PIDs):**

   First, find the Apache process ID (PID). Typically, Apache runs multiple processes under the user `www-data`, and the master process under `root`.

   ```bash
   ps aux | grep apache2
   ```

   This command will list several processes, like:

   ```bash
   root       1155  0.0  0.5  345656  12152 ?        Ss   09:12   0:00 /usr/sbin/apache2 -k start
   www-data   1159  0.0  0.4  353260  10364 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
   ```

2. **Attach `strace` to the Apache Processes:**

   Attach `strace` to the identified PIDs to monitor system calls. Start by attaching to the `root` process:

   ```bash
   sudo strace -p 1155 -o strace_root.log
   ```

   Then, in another terminal, attach `strace` to the `www-data` process:

   ```bash
   sudo strace -p 1159 -o strace_www.log
   ```

   **Note:** Keep `strace` running in the `www-data` terminal as you'll need to capture system calls during an HTTP request.

**Step 2: Simulate the 500 Error Using `curl`**

In another terminal, trigger the 500 Internal Server Error by making a request to the Apache server:

```bash
curl -sI 127.0.0.1
```

This command sends a request to the server and retrieves only the headers. If Apache is returning a 500 error, it will be captured in the response.

**Step 3: Analyze the `strace.log` to Identify the Issue**

Open the `strace.log` file and look for errors related to file access, permissions, or syntax issues that might be causing the 500 error.

```bash
less strace.log
```

**Step 4: Apply the Fix**

Suppose you found an issue where a PHP file has a typo in the extension, such as `.phpp` instead of `.php`. Here's how you would fix it:

1. **Locate the File:**

   Use `grep` to search for the typo:

   ```bash
   sudo grep -ro "phpp" /var/www
   ```

2. **Edit the File:**

   Once the file is located, open it in `vi` for editing:

   ```bash
   sudo vi /var/www/html/wp-settings.php
   ```

   In `vi`, search for the typo using:

   ```bash
   /phpp
   ```

   Correct the typo and save the file with the correct extension.

**Step 5: Restart Apache to Apply the Fix**

Restart the Apache server to apply the changes:

```bash
sudo service apache2 restart
```

**Step 6: Verify the Fix**

Run the `curl` command again to check if the 500 error is resolved:

```bash
curl -sI 127.0.0.1
```

You should now receive a `200 OK` response, indicating the issue is resolved.

### 3. Automate the Fix Using Puppet

**Step 1: Apply the Puppet Manifest**

Use the provided Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix:

```bash
sudo puppet apply 0-strace_is_your_friend.pp
```

**Step 2: Verify the Fix**

After applying the fix, verify that the 500 Internal Server Error is resolved by making another request to the server.

```bash
curl -sI 127.0.0.1
```

You should receive a `200 OK` response, indicating the issue is resolved.

---

### Additional Notes

**Common Issues to Look For:**

- **File Permissions:** Look for "Permission denied" errors.
- **Syntax Errors:** In PHP files, look for "Parse error" or "syntax error".
- **Missing Files:** Look for "No such file or directory".
- **Misconfigured PHP Paths:** Check for incorrect paths or filenames.

## Tasks
### Task 0: Strace is Your Friend
Use `strace` to identify and fix the issue causing Apache to return a 500 Internal Server Error. Automate the fix using Puppet.

#### Hint:
- strace can attach to a current running process
- You can use tmux to run strace in one window and curl in another one

**Requirements:**
- Your 0-strace_is_your_friend.pp file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix

**Example:**
```bash
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#
```
- **Directory:** `0x17-web_stack_debugging_3`
- **File:** `0-strace_is_your_friend.pp`
