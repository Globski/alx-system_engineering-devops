# Web Infrastructure Design

## Description
This project focused on designing and understanding different web infrastructure setups. The tasks involved creating diagrams and explanations for various web architectures, starting from a simple single-server setup to a more complex and secure multi-server infrastructure.

## Project Structure

| Task                   | Description                                                          | Deliverable                  |
|------------------------|----------------------------------------------------------------------|------------------------------|
| Simple web stack       | Design a one server web infrastructure.                              | [0-simple_web_stack](0-simple_web_stack), [0-simple_web_stack.jpg](0-simple_web_stack.jpg), [0-simple_web_stack.md](0-simple_web_stack.md) |
| Distributed web infrastructure | Design a three server web infrastructure.                           | [1-distributed_web_infrastructure](1-distributed_web_infrastructure), [1-distributed_web_infrastructure.png](1-distributed_web_infrastructure.jpg), [1-distributed_web_infrastructure.md](1-distributed_web_infrastructure.md)  |
| Secured and monitored web infrastructure | Design a secured and monitored web infrastructure.                           | [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure), [2-secured_and_monitored_web_infrastructure.png](2-secured_and_monitored_web_infrastructure.jpg), [2-secured_and_monitored_web_infrastructure.md](2-secured_and_monitored_web_infrastructure.md)  |
| Scale up               | Scale up the existing web infrastructure.                           | [3-scale_up](3-scale_up), [3-scale_up.jpg](3-scale_up.jpg), [3-scale_up.md](3-scale_up.md)  |


## Requirements

- Diagrams should be clear and detailed.

## Background Context
Web infrastructure design is crucial for building scalable, reliable, and efficient web applications. Understanding the various components and their interactions helps in designing robust systems.

## Learning Objectives
After completing this project, you should be able to explain:

- DNS
- Monitoring
- Web Server
- Network basics
- Load balancer
- Server
- Draw a diagram covering the web stack you built with the sysadmin/devops track projects.
- Explain what each component is doing.
- Explain system redundancy.
- Know all the mentioned acronyms: LAMP, SPOF, QPS.

## Tasks
### 0. Simple web stack
**#mandatory**

Design a one server web infrastructure that hosts the website reachable via www.foobar.com.  
**Requirements:**
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
- Explain some specifics about this infrastructure:
  - What is a server
  - What is the role of the domain name
  - What type of DNS record www is in www.foobar.com
  - What is the role of the web server
  - What is the role of the application server
  - What is the role of the database
  - What is the server using to communicate with the computer of the user requesting the website
- Explain what the issues are with this infrastructure:
  - SPOF
  - Downtime when maintenance needed
  - Cannot scale if too much incoming traffic

**Deliverable:** 
- Diagram showing the infrastructure
- Detailed explanation

**Repo:**
- GitHub repository: alx-system_engineering-devops
- Directory: 0x09-web_infrastructure_design
- File: 0-simple_web_stack

### 1. Distributed web infrastructure
**#mandatory**

Design a three server web infrastructure that hosts the website www.foobar.com.  
**Requirements:**
- 2 additional servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)
- Explain some specifics about this infrastructure:
  - For every additional element, why you are adding it
  - What distribution algorithm your load balancer is configured with and how it works
  - Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
  - How a database Primary-Replica (Master-Slave) cluster works
  - What is the difference between the Primary node and the Replica node in regard to the application
- Explain what the issues are with this infrastructure:
  - Where are SPOF
  - Security issues (no firewall, no HTTPS)
  - No monitoring

**Deliverable:** 
- Diagram showing the infrastructure
- Detailed explanation

**Repo:**
- GitHub repository: alx-system_engineering-devops
- Directory: 0x09-web_infrastructure_design
- File: 1-distributed_web_infrastructure

### 2. Secured and monitored web infrastructure
**#mandatory**

Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.  
**Requirements:**
- 3 firewalls
- 1 SSL certificate to serve www.foobar.com over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)
- Explain some specifics about this infrastructure:
  - For every additional element, why you are adding it
  - What are firewalls for
  - Why is the traffic served over HTTPS
  - What monitoring is used for
  - How the monitoring tool is collecting data
  - Explain what to do if you want to monitor your web server QPS
- Explain what the issues are with this infrastructure:
  - Why terminating SSL at the load balancer level is an issue
  - Why having only one MySQL server capable of accepting writes is an issue
  - Why having servers with all the same components (database, web server, and application server) might be a problem

**Deliverable:** 
- Diagram showing the infrastructure
- Detailed explanation

**Repo:**
- GitHub repository: alx-system_engineering-devops
- Directory: 0x09-web_infrastructure_design
- File: 2-secured_and_monitored_web_infrastructure

### 3. Scale up
**#advanced**

Scale up the existing web infrastructure.  
**Requirements:**
- 1 additional server
- 1 load-balancer (HAproxy) configured as a cluster with the other one
- Split components (web server, application server, database) with their own server
- Explain some specifics about this infrastructure:
  - For every additional element, why you are adding it

**Deliverable:** 
- Diagram showing the infrastructure
- Detailed explanation

**Repo:**
- GitHub repository: alx-system_engineering-devops
- Directory: 0x09-web_infrastructure_design
- File: 3-scale_up
