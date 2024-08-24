System Engineering Devops - Web stack debugging #3

## Project Description
This project involves debugging an Apache server that is returning a 500 Internal Server Error. Using `strace`, you will diagnose the issue, apply a fix manually, and then automate the fix using Puppet.

## Objective
- Debug a Wordpress website running on a LAMP stack (Linux, Apache, MySQL, PHP).

## Project Structure

| Task                               | Description                                                        | Source Code                                |
|------------------------------------|--------------------------------------------------------------------|--------------------------------------------|
| **0. Strace is Your Friend**       | Use `strace` to find why Apache returns a 500 error. Fix the issue and automate it using Puppet. | [0-strace_is_your_friend.pp](path/to/0-strace_is_your_friend.pp) |

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


### Installation of Puppet-lint
1. **Install Ruby:**
   Ensure Ruby is installed, as `puppet-lint` requires it.
   ```bash
   $ apt-get install -y ruby
   ```
3. **Install puppet-lint:**
   Install `puppet-lint`, a tool to check your Puppet manifests for style guide compliance.
   ```bash
   $ gem install puppet-lint -v 2.1.1
   ```

5. **Diagnosing the Apache 500 Error:** **Use `strace` to trace the Apache process**
   Identify the cause of the 500 Internal Server Error by attaching `strace` to the Apache process.
   - First, find the Apache process ID (PID):
   ```bash
   ps aux | grep apache2
   ```
   - Attach `strace` to the identified PID:
   ```bash
   sudo strace -p <PID> -o strace.log
   ```
   - Replace `<PID>` with the actual PID of the Apache process. This command will log all system calls made by Apache to `strace.log`.

   **Simulate the Error with `curl`:**
   Trigger the error by making a request to the Apache server.
   ```bash
   curl -sI 127.0.0.1
   ```
   - This command sends a request to the server and retrieves only the headers. If Apache is returning a 500 error, it will be captured in the response.
   
   **Analyze the `strace.log` to identify the issue.:**
   Open the `strace.log` file and look for any errors related to file access, permissions, or syntax issues that might be causing the 500 error.
   ```bash
   less strace.log
   ```

7. **Apply the Fix:**
   Implement the necessary fix manually to verify the issue is resolved.
   - Example fix might include setting correct file permissions
   - Replace `/path/to/file` with the actual path that was causing the issue.
   ```bash
   sudo chmod 755 /path/to/file
   ```

8. **Automate with Puppet:**
   Use the provided Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix:
   ```bash
   sudo puppet apply 0-strace_is_your_friend.pp
   ```
9. **Verify the fix by checking the Apache server status:**
   After applying the fix, verify that the 500 Internal Server Error is resolved by making another request to the server.
   ```bash
   curl -sI 127.0.0.1
   ```

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
