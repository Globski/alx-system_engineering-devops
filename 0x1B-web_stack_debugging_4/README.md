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
