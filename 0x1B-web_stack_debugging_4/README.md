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

## Additional Notes
**Benchmarking** is the process of measuring and evaluating the performance of a system, application, or component under a specific workload.
- The goal is to assess how well the system performs under various conditions, often comparing it against a standard or against other systems.
- Benchmarking helps identify bottlenecks, optimize performance, and ensure that the system meets the required performance standards.

- **Identify Performance Bottlenecks:** Helps in locating where the system slows down under stress.
- **Optimize Resources:** Ensures that resources (CPU, memory, network) are used efficiently.
- **Capacity Planning:** Helps in planning for future growth by understanding the limits of the current setup.
- **Compare Systems:** Evaluate different systems or configurations to determine the best option.

**ApacheBench** (often abbreviated as `ab`) is a popular benchmarking tool that allows you to simulate multiple HTTP requests to a web server and measure how well the server performs. It is particularly useful for stress testing and performance tuning of web servers.

- **Simulate Multiple Users:** ApacheBench can simulate many users making requests to the server at the same time.
- **Measure Response Times:** It provides detailed statistics on how long it takes for the server to respond to requests.
- **Test Server Limits:** Helps determine the maximum number of requests a server can handle before performance degrades.
- **Assess Throughput:** Measures how many requests per second the server can handle.

#### How ApacheBench Works:

ApacheBench works by sending a specified number of HTTP requests to a web server and then collecting performance data. For example, you can use ApacheBench to simulate 1000 requests with 100 concurrent users. The tool will report back with statistics such as:

- **Requests per second:** How many requests the server handled per second.
- **Time per request:** The average time taken for the server to respond to a single request.
- **Transfer rate:** The amount of data the server transferred per second.

#### Example Command:

```bash
ab -n 1000 -c 100 http://example.com/
```

- **-n 1000:** The total number of requests to perform (1000 requests in this case).
- **-c 100:** The number of multiple requests to perform at a time (100 concurrent users).
- **http://example.com/**: The target URL to which the requests will be sent.

#### Output Analysis:

After running ApacheBench, you'll receive an output similar to this:

```
Concurrency Level:      100
Time taken for tests:   3.567 seconds
Complete requests:      1000
Failed requests:        0
Requests per second:    280.43 [#/sec] (mean)
Time per request:       356.72 [ms] (mean)
Transfer rate:          123.67 [Kbytes/sec] received
```

- **Requests per second:** Indicates the throughput of the server.
- **Time per request:** Shows how long, on average, it took to complete a request.
- **Transfer rate:** Indicates the data rate of the responses.

