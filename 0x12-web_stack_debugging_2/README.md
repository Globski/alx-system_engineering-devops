# System-Engineering Devops - Web stack debugging #2

## Description
This project focus on debugging and configuring a web stack to enhance security and functionality. You'll work on running processes as different users, configuring Nginx to operate under specific conditions, and simplifying your configuration script.

## Project Structure
| Task                             | Description                                                                                     | Source Code                      |
|----------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------|
| Task 0: Run Software as Another User | Write a Bash script to run the whoami command as another user specified by an argument.       | [0-iamsomeoneelse](0-iamsomeoneelse) |
| Task 1: Run Nginx as Nginx        | Configure Nginx to run as the nginx user and listen on port 8080.                             | [1-run_nginx_as_nginx](1-run_nginx_as_nginx) |
| Task 2: 7 Lines or Less           | Simplify the Task 1 script to 7 lines or less, adhering to specified constraints.                | [100-fix_in_7_lines_or_less](100-fix_in_7_lines_or_less) |.

**Debugging**:
   - Troubleshoot and resolve issues related to the web stack, which could involve configuration problems, service issues, or other system-level ### Task 0: Run Software as Another User

## Learning Objectives
- Understand how to run processes as different users in a Unix-like environment.
- Configure and secure web servers to run under non-root users.

## Environment
- All files should be interpreted on Ubuntu 20.04 LTS.

## Requirements
- All files should end with a new line.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck without any error.
- Bash scripts must run without errors.
- The first line of all Bash scripts should be #!/usr/bin/env bash.

## How to Use
1. **Task 0:**
   - Run the script with a username as an argument to check whoami for that user.
   
```bash
   ./0-iamsomeoneelse <username>
```

2. **Task 1:**
   - Run the script to configure Nginx.
   
```bash
   ./1-run_nginx_as_nginx
```

3. **Task 2:**
   - Run the simplified script to achieve the same configuration as Task 1 in fewer lines.
   
```bash
   ./100-fix_in_7_lines_or_less
```

## Tasks

### Task 0: Run Software as Another User
- **Description:** The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.
- **Requirements:**
  - Write a Bash script that accepts one argument.
  - The script should run the whoami command under the user passed as an argument.
  - Make sure to try your script by passing different users.
- **Example:**
  
```bash
  root@ubuntu:~# whoami
  root
  root@ubuntu:~# ./0-iamsomeoneelse www-data
  www-data
  root@ubuntu:~# whoami
  root
  root@ubuntu:~#
```

  - File: 0-iamsomeoneelse

### Task 1: Run Nginx as Nginx
- **Description:** The root user is a superuser that can do anything on a Unix machine, the top administrator. Security-wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break in to your server, the impact is limited by the permissions of the nginx user.
- **Requirements:**
  - Nginx must be running as the nginx user.
  - Nginx must be listening on all active IPs on port 8080.
  - You cannot use apt-get remove.
  - Write a Bash script that configures the container to fit the above requirements.
- **After Debugging:**
  
```bash
  root@ab6f4542747e:~# ps auxff | grep ngin[x]
  nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
  nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
  nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
  nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
  nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
  root@ab6f4542747e:~#
  root@ab6f4542747e:~# nc -z 0 8080 ; echo $?
  0
  root@ab6f4542747e:~#
```

  - File: 1-run_nginx_as_nginx

### Task 2: 7 Lines or Less
- **Description:** Using what you did for task #1, make your fix short and sweet.
- **Requirements:**
  - Your Bash script must be 7 lines long or less.
  - There must be a new line at the end of the file.
  - You must respect Bash script requirements.
  - You cannot use ;.
  - You cannot use &&.
  - You cannot use wget.
  - You cannot execute your previous answer file (Do not include the name of the previous script in this one).

  - File: 100-fix_in_7_lines_or_less
