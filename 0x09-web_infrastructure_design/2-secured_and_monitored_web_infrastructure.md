# Secured and monitored web infrastructure

## What are firewalls for
A firewall is a security system that monitors and controls incoming and outgoing network traffic based on pre-defined security rules. It acts as a barrier between your internal network and external threats.
Firewall Protect each server (Web Server, Application Server, Database Server) from unauthorized access. Implement a firewall to protect each server (web server, application server, database server) from unauthorized access and to filter out malicious traffic.

## Why is the traffic served over HTTPS
**HTTPS:** HTTPS (Hypertext Transfer Protocol Secure) is an extension of HTTP that provides secure communication over a computer network by encrypting data using SSL/TLS protocols.
It is the secure version of HTTP (Hypertext Transfer Protocol), the primary protocol used for transferring data between a web browser and a website. HTTPS encrypts the data exchanged between the browser and the server to ensure that communications remain confidential and secure.
Implement HTTPS to encrypt data transmitted between users and your server, ensuring secure communication and protecting sensitive information from interception and tampering.

## What monitoring is used for
Monitoring tools gather performance data, alerting administrators to potential issues. Implementing monitoring tools can help track the performance, health, and usage of the infrastructure components, allowing for proactive maintenance and quick issue resolution.
Implement comprehensive monitoring solutions to continuously track system health and activity, detect issues early, and ensure timely responses to potential problems.
- Monitoring provides insights into system performance, including resource usage, response times, and traffic patterns.
- Utilize monitoring tools to gather performance data, analyze trends, and make informed decisions regarding resource allocation and capacity planning.
- Monitoring helps in identifying and responding to security threats and suspicious activities.
- Implement security monitoring to detect and respond to potential threats and unauthorized activities promptly.

## How the monitoring tool is collecting data
Monitoring tools collect data such as CPU usage, memory usage, disk space, and network traffic. They can also monitor specific metrics like QPS (Queries Per Second) on a web server. Tools like Sumo Logic to collect and analyze data on server performance and security. 
- **Examples**: Prometheus with Grafana for real-time data visualization.

## Explain what to do if you want to monitor your web server QPS
To monitor QPS, you can use tools like Prometheus with Grafana, which collects and visualizes real-time data on how many queries your web server is handling.

## Why terminating SSL at the load balancer level is an issue
SSL Termination at the Load Balancer level means traffic between the load balancer and the web servers is unencrypted which could introduce a potential security vulnerability. When SSL termination occurs at the load balancer, the traffic between the load balancer and the backend servers (such as web servers, application servers, and databases) is transmitted in plaintext, rather than being encrypted. This means that the sensitive data within the internal network is exposed to potential interception or eavesdropping.
The recommended approach is to implement end-to-end encryption by allowing SSL termination to occur at the backend servers rather than at the load balancer. This ensures that the traffic between the load balancer and the backend servers remains encrypted, providing a higher level of security for the internal network. Additionally, the use of secure communication protocols, such as TLS, should be enforced to protect data in transit. 

## Why having only one MySQL server capable of accepting writes is an issue
Having a single MySQL server for writes creates a bottleneck and a SPOF. If this server fails, no writes can be performed until it's restored, potentially causing data loss.

## Why having servers with all the same components (database, web server and application server) might be a problem
This allows each component to be scaled independently, improves performance, and reduces the likelihood of a single failure taking down the entire system.
If all servers have the same components, resource allocation can be inefficient and failures can affect multiple services. This architecture lacks flexibility and scalability. Each server becomes an SPOF and it becomes more difficult to scale specific components independently. Splitting these roles across different servers allows for more efficient scaling and reduces the risk of failures affecting the entire system.
To ensure redundancy and reduce SPOF, improving the system’s availability and resilience.  A clustered load balancer setup ensures that if one load balancer fails, the other can take over, maintaining traffic distribution and avoiding downtime.
